# Section-aware parse of harvested awesome lists: which section each GitHub repo appears under.
import re, json, os, glob, collections

base = os.environ['LOCALAPPDATA'] + '/Temp'
files = glob.glob(base + '/list_*.md') + glob.glob(base + '/lists/*.md')

BAD_SEC = re.compile(r'related|see also|similar|more awesome|awesome lists|adjacent|other awesome|community curated|also awesome', re.I)
LIKE_SEC = re.compile(r'jev.?like|open (model|alternative)|alternative|unofficial (implementation|sdk)|reimplementation|reproduction|replica', re.I)
SKIP_OWNER = {'sindresorhus', 'awesome-repos', 'github', 'img.shields.io'}

pat = re.compile(r'\[([^\]]*)\]\((https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+))([^)]*)\)')

appear = collections.defaultdict(list)  # fn -> [(file, heading)]
for f in files:
    txt = open(f, encoding='utf-8', errors='replace').read()
    heading = ''
    for line in txt.splitlines():
        hm = re.match(r'^(#{1,4})\s+(.*)', line)
        if hm:
            heading = re.sub(r'[#*\[\]]', '', hm.group(2)).strip()
            continue
        for m in pat.finditer(line):
            owner, repo = m.group(3), m.group(4)
            if owner in SKIP_OWNER: continue
            fn = (owner + '/' + repo).lower()
            appear[fn].append((os.path.basename(f), heading))

# classify each appearance
def appearance_kind(fn, file, heading):
    if BAD_SEC.search(heading): return 'related'
    if LIKE_SEC.search(heading): return 'like'
    if re.search(r'awesome', fn.split('/')[1]) and 'jev' in fn: return 'list'
    return 'project'

strong = collections.Counter(); like = collections.Counter(); lists = collections.Counter()
for fn, apps in appear.items():
    kinds = [appearance_kind(fn, f, h) for f, h in apps]
    strong[fn] = sum(k == 'project' for k in kinds)
    like[fn] = sum(k == 'like' for k in kinds)
    lists[fn] = sum(k == 'list' for k in kinds)

json.dump({'strong': dict(strong), 'like': dict(like), 'lists': dict(lists)},
          open(base + '/signals.json', 'w', encoding='utf-8'))
print('repos seen:', len(appear))
print('strong>=2:', sum(1 for v in strong.values() if v >= 2), '>=1:', sum(1 for v in strong.values() if v >= 1))
print('like>=1:', sum(1 for v in like.values() if v >= 1))
