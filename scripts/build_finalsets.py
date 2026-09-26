# Build core candidate set: admit a repo only if its OWN metadata (name/description/
# homepage, or official owner) is Jev-relevant. List cross-counts alone are NOT
# sufficient — big awesome lists link generic repos inside project sections.
# GitHub topics are self-applied and spammable (unrelated repos carry the `jev`
# topic), so a topic match only counts as evidence when curators independently
# cross-referenced the repo in >=2 lists (grandfather rule for the seed build).
import json, os, re

base = os.environ['LOCALAPPDATA'] + '/Temp'
gq = json.load(open(base + '/gq.json', encoding='utf-8'))
topics = json.load(open(base + '/topics.json', encoding='utf-8'))
sig = json.load(open(base + '/signals.json', encoding='utf-8'))
OFFICIAL = {'typesafe-ai', 'type-safe-ai', 'jev-chat', 'omnijev'}

# 'jev' is a coined term — substring anywhere (pocketjev, OmniJev, djev-run) is strong
JEV = re.compile('jev', re.I)
# case-sensitive proper token: lowercase "the system one" is plain English, not the
# TypeSafe product name (see update_list.py note).
SYS1 = re.compile(r'System[ -]?One\b|System 1\b')
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
    if JEV.search(repo) or JEV.search(desc):
        return True
    if SYS1.search(desc):
        return True
    if TS_URL.search(desc) or TS_URL.search(meta.get('homepageUrl') or ''):
        return True
    if NEG.search(desc):
        return False
    # a bare topic:typesafe is NOT evidence — the TS ecosystem uses that topic
    # heavily. Only the company signals above qualify.
    if TS_COMPANY.search(desc) and COMPANY_CTX.search(desc):
        return True
    # topic-only match: keep only if curators cross-referenced the repo in >=2
    # independent lists (grandfather rule; topic alone is spammable). GitHub
    # topics are always lowercase, so match lowercase here.
    if (JEV.search(tops) or re.search(r'system[- ]?(one|1)\b', tops)) and sig['strong'].get(fn, 0) >= 2:
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
