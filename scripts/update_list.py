#!/usr/bin/env python3
"""Daily awesome-jev update: scrape GitHub for new Jev/TypeSafe repos, refresh
star counts, stamp `added` dates, and regenerate data/jev.json + index data.

Runs unauthenticated-friendly: uses `gh` CLI when available (higher rate
limits), else plain HTTPS. Safe to run every day from GitHub Actions.
"""
import json, os, re, subprocess, sys, time, urllib.request, datetime, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data', 'jev.json')
TODAY = datetime.date.today().isoformat()

CAT_RULES = [  # (category_id, name-regex) — first match wins
    ('official', r'^skills$|^typesafe-sdk'),
    ('awesome', r'awesome|catalog|gallery|usecase|use-case|showcase|radar|survey|directors?'),
    ('finance', r'trad|financ|monad|quant|crypto|hedge|stock|money|invoice|wallet'),
    ('games', r'game|mario|pokemon|craft|chess|rpg|poker|play'),
    ('chat', r'chat|reply|discord|slack|telegram|whatsapp|email|inbox|sms|message|jarvis'),
    ('mcp', r'\bmcp\b|plugin|skill|cli$|toolkit'),
    ('web', r'browser|browse|scrape|crawl|search|seo'),
    ('mobile', r'android|ios|macos|windows|keyboard'),
    ('home', r'home|drone|robot|iot|printer'),
    ('media', r'video|audio|music|image|podcast|youtube|spotify|voice|speech|tts'),
    ('productivity', r'todo|task|notion|obsidian|calendar|note|wiki|dash|bookmark'),
    ('safety', r'safety|guard|judge|verif|eval|audit|moderat|triage|risk|spam|fraud|route|routing|review'),
    ('devtools', r'code|repo|git|debug|lint|test|deploy|ci$|refactor|bug|sql|db|docker|kubernetes'),
    ('openmodels', r'nano|open|any|simple|kev$|laya|ollaya|system.?one|noul|decision|classif|train|llm|gpt|qwen|model'),
    ('sdk', r'sdk|client|adapter|gateway|router|proxy|api|litellm|bridge'),
    ('agents', r'agent|auto|swarm|crew|rpa|foreman|orchestrat|work|assist|bot'),
]

def gh_api(path):
    """GET a GitHub REST path via gh (token) when possible, else plain."""
    try:
        r = subprocess.run(['gh', 'api', path], capture_output=True, text=True, timeout=60)
        if r.returncode == 0:
            return json.loads(r.stdout)
    except Exception:
        pass
    req = urllib.request.Request('https://api.github.com' + path,
                                 headers={'Accept': 'application/vnd.github+json',
                                          'User-Agent': 'awesome-jev-updater'})
    with urllib.request.urlopen(req, timeout=60) as f:
        return json.load(f)

def search_repos(query):
    """Search repos, return list of REST items (up to 100)."""
    from urllib.parse import quote
    try:
        items = gh_api(f'/search/repositories?q={quote(query)}&sort=stars&per_page=100')
        return items.get('items', []) if isinstance(items, dict) else []
    except Exception as e:
        print('search failed', query, e, file=sys.stderr)
        return []

def classify(owner, repo, desc, topics):
    name = repo.lower()
    hay = (repo + ' ' + (desc or '') + ' ' + ' '.join(topics or [])).lower()
    for cid, rx in CAT_RULES:
        if re.search(rx, name):
            return cid
    for cid, rx in CAT_RULES:
        if re.search(rx, hay):
            return cid
    return 'more'

# same rules as scripts/build_finalsets.py: 'jev' substring anywhere (coined term),
# System One, or the company (typesafe.ai). Generic "typesafe <TS-lib word>" excluded.
JEV_RX = re.compile(r'jev', re.I)
SYS1_RX = re.compile(r'system[ -]?one\b', re.I)
TS_URL_RX = re.compile(r'typesafe\.ai', re.I)
NEG_RX = re.compile(r"typesafe[’']?s?\s*[ -]?(utils?\b|utilit|librar|type\b|types\b|enum|pattern|config|forms?\b|ipc|routing|router|rail|i18n|url\b|stack|defini|action|generat|prop|endpoint|graphql|sql|http|rest|fetch|routes?\b|doobie|gem\b|helper)", re.I)
TS_TOPIC_RX = re.compile(r'typesafe', re.I)

def relevant(it):
    text = ' '.join(filter(None, [it.get('name'), it.get('description')]))
    tops = ' '.join(it.get('topics') or [])
    if (it.get('owner') or {}).get('login', '').lower() in ('typesafe-ai', 'type-safe-ai', 'jev-chat', 'omnijev'):
        return True
    if it.get('fork') and not JEV_RX.search(text):
        return False
    if JEV_RX.search(text) or JEV_RX.search(tops):
        return True
    if SYS1_RX.search(text) or SYS1_RX.search(tops):
        return True
    if TS_URL_RX.search(text) or TS_URL_RX.search(it.get('homepage') or ''):
        return True
    if NEG_RX.search(text):
        return False
    # company proper-token required in the description (search_items has no
    # separate homepage/topic guarantee beyond the queries above)
    if re.search(r'(TypeSafe|[Tt]ype[Ss]afe AI|[Tt]ypesafe\.ai|[Ss]ystem One)', text):
        return True
    return False

def main():
    entries = json.load(open(DATA, encoding='utf-8'))
    by_url = {e['url'].lower(): e for e in entries}

    # 1) discover new candidates
    queries = ['jev in:name,description,topics',
               'topic:jev', 'topic:typesafe',
               'system one in:description']
    found = {}
    for q in queries:
        for it in search_repos(q):
            fn = it['full_name']
            if fn.lower() in (u.replace('https://github.com/', '') for u in by_url):
                continue
            if it.get('stargazers_count') < 5:
                continue
            if not relevant(it):
                continue
            found[fn] = it
        time.sleep(2)

    added = 0
    for fn, it in found.items():
        url = it['html_url'].lower()
        if url in by_url:
            continue
        e = {'name': fn.split('/')[1], 'owner': fn.split('/')[0],
             'url': it['html_url'], 'desc': (it.get('description') or '')[:240],
             'stars': it['stargazers_count'],
             'lang': it.get('language'), 'added': TODAY,
             'pushedAt': (it.get('pushed_at') or '')[:10],
             'cross': 0, 'topics': (it.get('topics') or [])[:8]}
        e['category'] = classify(e['owner'], e['name'], e['desc'], e['topics'])
        entries.append(e); by_url[url] = e; added += 1

    # 2) refresh stars on existing entries (top 150 by stars, rate-limit friendly)
    refreshed = 0
    for e in sorted(entries, key=lambda x: -x['stars'])[:150]:
        p = e['url'].replace('https://github.com/', '/repos/')
        try:
            meta = gh_api(p)
            e['stars'] = meta['stargazers_count']
            e['pushedAt'] = (meta.get('pushed_at') or e['pushedAt'])[:10]
            refreshed += 1
        except Exception:
            pass
        time.sleep(1)

    # 3) sort by date-added desc, then stars desc; stamp date
    entries.sort(key=lambda e: (e['added'], e['stars']), reverse=True)
    meta = {'generated': TODAY, 'count': len(entries),
            'today_new': sum(1 for e in entries if e['added'] == TODAY)}
    json.dump(entries, open(DATA, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(f'added={added} refreshed={refreshed} total={len(entries)} new_today={meta["today_new"]}')

if __name__ == '__main__':
    main()
