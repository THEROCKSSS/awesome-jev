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
        r = subprocess.run(['gh', 'api', path], capture_output=True, text=True,
                           encoding='utf-8', errors='replace', timeout=60)
        if r.returncode == 0:
            return json.loads(r.stdout)
    except Exception:
        pass
    headers = {'Accept': 'application/vnd.github+json',
               'User-Agent': 'awesome-jev-updater'}
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = 'Bearer ' + token
    req = urllib.request.Request('https://api.github.com' + path, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as f:
        return json.load(f)

def search_repos(query, order):
    """Search repos, return list of REST items (up to 100)."""
    from urllib.parse import quote
    try:
        items = gh_api(f'/search/repositories?q={quote(query)}&sort={order}&order=desc&per_page=100')
        if not isinstance(items, dict) or not isinstance(items.get('items'), list):
            raise ValueError('Unexpected GitHub search response')
        return items['items']
    except Exception as e:
        print('search failed', query, order, e, file=sys.stderr)
        return None

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
# case-sensitive proper token: lowercase "the system one" is plain English ("replaces
# the system one"), not the TypeSafe product name.
SYS1_RX = re.compile(r'System[ -]?One\b|System 1\b')
TS_URL_RX = re.compile(r'typesafe\.ai', re.I)
NEG_RX = re.compile(r"typesafe[’']?s?\s*[ -]?(utils?\b|utilit|librar|type\b|types\b|enum|pattern|config|forms?\b|ipc|routing|router|rail|i18n|url\b|stack|defini|action|generat|prop|endpoint|graphql|sql|http|rest|fetch|routes?\b|doobie|gem\b|helper)", re.I)
TS_TOPIC_RX = re.compile(r'typesafe', re.I)
KNOWN_UNRELATED = {'gnlow/jevi', 'atom63/atom63-design-system'}

def relevant(it):
    # GitHub topics are self-applied and spammable (unrelated repos carry the
    # `jev` topic, e.g. docky, anything_about_game) — admission evidence is
    # name/description text, official owners, or a typesafe.ai homepage.
    # Topics are never admission evidence in the daily path.
    name = it.get('name') or ''
    description = it.get('description') or ''
    fields = (name, description)
    text = ' '.join(fields)
    home = it.get('homepage') or ''
    if (it.get('full_name') or '').lower() in KNOWN_UNRELATED:
        return False
    if (it.get('owner') or {}).get('login', '').lower() in ('typesafe-ai', 'type-safe-ai', 'jev-chat', 'omnijev'):
        return True
    if it.get('fork') and not any(JEV_RX.search(field) for field in fields):
        return False
    if any(JEV_RX.search(field) for field in fields):
        return True
    if any(SYS1_RX.search(field) for field in fields):
        return True
    if TS_URL_RX.search(text) or TS_URL_RX.search(home):
        return True
    if NEG_RX.search(text):
        return False
    if any(re.search(r'(TypeSafe|[Tt]ype[Ss]afe AI|[Tt]ypesafe\.ai|[Ss]ystem One)', field) for field in fields):
        return True
    return False

def main():
    entries = json.load(open(DATA, encoding='utf-8'))
    by_url = {e['url'].lower(): e for e in entries}
    known_names = {u.removeprefix('https://github.com/') for u in by_url}

    # 1) discover new candidates
    queries = ['jev in:name,description', 'topic:jev', 'topic:typesafe',
               'system one in:description', 'org:typesafe-ai']
    found = {}
    observed = {}
    successful = 0
    for q in queries:
        for order in ('stars', 'updated', 'created'):
            results = search_repos(q, order)
            if results is None:
                continue
            successful += 1
            for it in results:
                fn = it.get('full_name', '')
                if fn.lower() in known_names:
                    observed[fn.lower()] = it
                    continue
                if not relevant(it) or not it.get('html_url') or not fn.count('/') == 1:
                    continue
                found[fn] = it
            time.sleep(2)
    if successful == 0:
        raise RuntimeError('All GitHub discovery searches failed; catalog left untouched')

    added = 0
    for fn, it in found.items():
        url = it['html_url'].lower()
        if url in by_url:
            continue
        e = {'name': fn.split('/')[1], 'owner': fn.split('/')[0],
             'url': it['html_url'], 'desc': (it.get('description') or '')[:240],
             'stars': it.get('stargazers_count', 0),
             'lang': it.get('language'), 'added': TODAY,
             'pushedAt': (it.get('pushed_at') or '')[:10],
             'cross': 0, 'topics': (it.get('topics') or [])[:8]}
        e['category'] = classify(e['owner'], e['name'], e['desc'], e['topics'])
        entries.append(e); by_url[url] = e; known_names.add(fn.lower()); added += 1

    # 2) Refresh existing entries returned by discovery. Search results include
    # stars and push dates, avoiding hundreds of slow per-repo API requests.
    refreshed = 0
    for e in entries:
        fn = e['url'].removeprefix('https://github.com/').lower()
        meta = observed.get(fn)
        if meta:
            e['stars'] = meta.get('stargazers_count', e['stars'])
            e['pushedAt'] = (meta.get('pushed_at') or e.get('pushedAt') or '')[:10]
            refreshed += 1

    # 3) sort by date-added desc, then stars desc; stamp date
    entries.sort(key=lambda e: (e['added'], e['stars']), reverse=True)
    meta = {'generated': TODAY, 'count': len(entries),
            'today_new': sum(1 for e in entries if e['added'] == TODAY)}
    for path, value in ((DATA, entries), (os.path.join(ROOT, 'data', 'meta.json'), meta)):
        temp = path + '.tmp'
        with open(temp, 'w', encoding='utf-8') as f:
            json.dump(value, f, indent=1, ensure_ascii=False)
            f.write('\n')
        os.replace(temp, path)
    print(f'added={added} refreshed={refreshed} total={len(entries)} new_today={meta["today_new"]}')

if __name__ == '__main__':
    main()
