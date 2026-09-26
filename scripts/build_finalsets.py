# Build core candidate set: admit a repo only if its OWN metadata (name/description/
# topics/homepage) is Jev-relevant. List cross-counts alone are NOT sufficient —
# big awesome lists link generic repos inside project sections.
import json, os, re

base = os.environ['LOCALAPPDATA'] + '/Temp'
gq = json.load(open(base + '/gq.json', encoding='utf-8'))
topics = json.load(open(base + '/topics.json', encoding='utf-8'))
OFFICIAL = {'typesafe-ai', 'type-safe-ai', 'jev-chat', 'omnijev'}

# 'jev' is a coined term — substring anywhere (pocketjev, OmniJev, djev-run) is strong
JEV = re.compile('jev', re.I)
SYS1 = re.compile(r'system[ -]?one\b|system[ -]?1\b', re.I)
TS_URL = re.compile(r'typesafe\.ai', re.I)
TS_COMPANY = re.compile(r'typesafe', re.I)
# require the company's own name as a proper token (case-sensitive), not just
# the lowercase TS-ecosystem adjective next to generic words like "sdk"/"api"
COMPANY_CTX = re.compile(r'(TypeSafe|[Tt]ype[Ss]afe AI|[Tt]ypesafe\.ai|[Ss]ystem One)')
# "typesafe <TS/Java-ecosystem word>" = generic adjective or old Lightbend 'Typesafe Config',
# not TypeSafe the Jev company
NEG = re.compile(r"typesafe[’']?s?\s*[ -]?(utils?\b|utilit|librar|type\b|types\b|enum|pattern|config|forms?\b|ipc|routing|router|rail|i18n|url\b|stack|defini|action|generat|prop|endpoint|graphql|sql|http|rest|fetch|routes?\b|doobie|gem\b|helper|chess|comment)", re.I)

def relevant(fn, meta):
    owner, repo = fn.split('/')
    desc = meta.get('description') or ''
    tops = ' '.join(topics.get(fn, []))
    # generic forks of upstream repos are duplicates; a fork carrying its own Jev
    # work (jev in name/desc) is a project, not a duplicate
    if meta.get('isFork') and not JEV.search(repo) and not JEV.search(desc):
        return False
    if owner.lower() in OFFICIAL:
        return True
    if JEV.search(repo) or JEV.search(desc) or JEV.search(tops):
        return True
    if SYS1.search(desc) or SYS1.search(tops):
        return True
    if TS_URL.search(desc) or TS_URL.search(meta.get('homepageUrl') or ''):
        return True
    if NEG.search(desc):
        return False
    # a bare topic:typesafe is NOT evidence — the TS ecosystem uses that topic
    # heavily. Only the company signals above qualify.
    if TS_COMPANY.search(desc) and COMPANY_CTX.search(desc):
        return True
    return False

core = [fn for fn, meta in gq.items() if relevant(fn, meta)]
json.dump({'core': sorted(core), 'alts': []}, open(base + '/finalsets.json', 'w', encoding='utf-8'))
old_path = base + '/finalsets.bak.json'
if os.path.exists(old_path):
    old = set(json.load(open(old_path, encoding='utf-8'))['core'])
    print('core:', len(core), '| new:', len(set(core) - old), '| dropped-from-old:', len(old - set(core)))
    for fn in sorted(old - set(core))[:25]:
        print('  dropped:', fn)
else:
    print('core:', len(core))
