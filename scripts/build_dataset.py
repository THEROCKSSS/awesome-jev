# Build final curated dataset from core set with better categorization.
import json, os, re, collections, datetime

base = os.environ['LOCALAPPDATA'] + '/Temp'
gq = json.load(open(base + '/gq.json', encoding='utf-8'))
topics = json.load(open(base + '/topics.json', encoding='utf-8'))
sig = json.load(open(base + '/signals.json', encoding='utf-8'))
strong = sig['strong']
final = json.load(open(base + '/finalsets.json', encoding='utf-8'))
core = final['core']

TODAY = '2026-09-25'

CATS = [
    ('official', 'Official Resources', 'Official TypeSafe repos, SDKs, docs tooling', [
        (lambda e: e['owner'] == 'typesafe-ai', 100),
        (r'\bofficial\b.*(sdk|api|client)', 40),
    ]),
    ('awesome', 'Awesome Lists & Catalogs', 'Curated lists and directories of Jev projects', [
        (r'awesome[-_]?(jev|typesafe)|jev.*(awesome|catalog|gallery|index|use.?cases?|usecases?|directory|survey|showcase|radar)|jevcatalog|awesomejev', 100),
        (r'\bawesome list\b.*jev|\bcatalog(ue|) of\b.*jev|\bcollection of\b.*jev.*(project|example|resource)', 60),
    ]),
    ('sdk', 'SDKs, APIs & Routers', 'Client libraries, adapters, gateways and routers', [
        (r'sdk|client librar|adapter|gateway|router|proxy|-api$|api-server|openai(-compatible)?|anthropic|litellm|bedrock|vercel.?ai|cohere', 40),
        (r'\bsdk\b|\bapi client\b|\bgateway\b|\brouter\b', 25),
    ]),
    ('openmodels', 'Open & Jev-like Models', 'Open reimplementations, local runners and research models', [
        (r'nanojev|openjev|anyjev|simple.?jev|playjev|kev$|ollaya|laya|system.?one|noul|decision.?model|classifier|fine.?tun|train', 35),
        (r'(open.?source|local|reimpl|replica|reproduc|open weight).*(decision|system.?one|jev)|run.*(jev|decision).*local', 30),
    ]),
    ('agents', 'Agents & Automation', 'Autonomous agents and automated workflows driven by Jev decisions', [
        (r'agent|autopilot|autonomous|swarm|crew|rpa|foreman|orchestrat|pipeline|workflow|automation|worker|assistant', 30),
    ]),
    ('mcp', 'MCP & Agent Tools', 'MCP servers, plugins, skills and CLI tools', [
        (r'\bmcp\b|model.?context.?protocol|claude(-code)?|plugin|skill|actionkit|toolkit|\bcli\b|vscode|neovim|cursor', 30),
    ]),
    ('web', 'Web & Browsing', 'Browsing, scraping, search and web-action agents', [
        (r'browser|browsing|scrape|crawl|web.?agent|search|seo|webaction|http', 30),
    ]),
    ('devtools', 'Developer Tools', 'Code review, CI, testing, databases and dev productivity', [
        (r'code|repo|review|pull.?request|\bpr\b|debug|lint|test|deploy|\bci\b|refactor|bug|compiler|migrat|database|\bsql\b|postgres|redis|docker|kubernetes', 30),
    ]),
    ('games', 'Games & Play', 'Games, simulations and playful demos', [
        (r'game|mario|pokemon|craft|chess|rpg|dungeon|quest|poker|tetris|snake|sim(ulation)?|play', 30),
    ]),
    ('chat', 'Chat & Messaging', 'Reply assistants, chatbots and messaging integrations', [
        (r'chat|reply|discord|slack|telegram|whatsapp|signal$|email|inbox|sms|message|dm|conversation|support.?ticket', 30),
    ]),
    ('finance', 'Finance & Trading', 'Trading, fintech and economic decision systems', [
        (r'trad(e|ing)|financ|money|crypto|stock|portfolio|hedge|monad|invoice|payment|bank|wallet', 30),
    ]),
    ('safety', 'Safety, Routing & Guardrails', 'Moderation, triage, verification, routing and eval harnesses', [
        (r'safety|guardrail|guard|judge|verif|eval|audit|moderat|triage|risk|spam|fraud|abuse|content.?filter|route|routing|score', 30),
    ]),
    ('productivity', 'Productivity & Knowledge', 'Notes, tasks, documents and knowledge tools', [
        (r'todo|task|notion|obsidian|calendar|note|knowledge|wiki|document|pdf|meeting|summariz|dash(board|board)?|bookmark', 25),
    ]),
    ('media', 'Media & Content', 'Video, audio, images and content pipelines', [
        (r'video|audio|music|image|podcast|youtube|spotify|photo|art|caption|transcri|subtitle|voice|speech|tts', 25),
    ]),
    ('mobile', 'Mobile & Desktop Apps', 'Native mobile and desktop applications', [
        (r'android|ios$|iphone|macos|windows$|desktop|flutter|swiftui|react.?native|keyboard', 25),
    ]),
    ('home', 'Home, IoT & Robotics', 'Smart home, drones, robots and physical-world integrations', [
        (r'home.?assistant|homekit|\biot\b|drone|robot|3d.?print|fridge|garden|camera|nest|mqtt|tesla', 25),
    ]),
]

def cat_of(owner, repo, fn, desc):
    name = repo.lower()
    hay = (repo + ' ' + (desc or '') + ' ' + ' '.join(topics.get(fn, []))).lower()
    # name-first rules (repo name is the strongest signal)
    NAME_RULES = [
        ('official', r'^skills$|^typesafe-sdk'),
        ('awesome', r'awesome|catalog|gallery|usecase|use-case|showcase|radar|survey'),
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
    for cid, rx in NAME_RULES:
        if re.search(rx, name):
            return cid
    best, best_s = 'more', 0
    for cid, name, _desc, rules in CATS:
        for rule, weight in rules:
            if callable(rule):
                s = weight if rule({'owner': owner, 'repo': repo}) else 0
            else:
                s = weight if re.search(rule, hay) else 0
            if s > best_s:
                best, best_s = cid, s
    return best if best_s >= 25 else 'more'

entries = []
for fn in core:
    meta = gq[fn]
    st = meta['stargazerCount']; cross = strong.get(fn, 0)
    desc = (meta.get('description') or '').strip()
    if not desc:
        continue
    if not (st >= 5 or cross >= 2):
        continue
    owner, repo = fn.split('/')
    e = {'name': repo, 'owner': owner, 'url': 'https://github.com/' + meta['nameWithOwner'],
         'desc': desc[:240], 'stars': st,
         'lang': (meta.get('primaryLanguage') or {}).get('name') if meta.get('primaryLanguage') else None,
         'added': TODAY, 'pushedAt': (meta.get('pushedAt') or '')[:10],
         'cross': cross, 'topics': topics.get(fn, [])[:8]}
    e['category'] = cat_of(owner, repo, fn, desc)
    entries.append(e)

entries.sort(key=lambda e: (-e['stars'], -e['cross']))
# dedupe case-variant repos (GitHub names are case-insensitive)
seen = {}
deduped = []
for e in entries:
    key = e['url'].lower()
    if key in seen:
        prev = seen[key]
        prev['cross'] = max(prev['cross'], e['cross'])
        prev['topics'] = sorted(set(prev['topics']) | set(e['topics']))[:8]
        if prev['category'] == 'more' and e['category'] != 'more':
            prev['category'] = e['category']
        continue
    seen[key] = e
    deduped.append(e)
entries = deduped
print('final entries:', len(entries))
cnt = collections.Counter(e['category'] for e in entries)
for cid, name, desc, _ in CATS:
    print(f"  {cnt.get(cid,0):4d}  {name}")
print(f"  {cnt.get('more',0):4d}  More projects")
json.dump(entries, open(base + '/dataset.json', 'w', encoding='utf-8'), indent=1)
for e in entries[:15]:
    print(e['stars'], e['url'].split('github.com/')[1], '|', e['category'])
