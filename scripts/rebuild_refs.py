# Rebuild refs.json counts from the 22 harvested list files (flat occurrence counts).
import re, json, os, glob, collections

base = os.environ['LOCALAPPDATA'] + '/Temp'
files = glob.glob(base + '/list_*.md') + glob.glob(base + '/lists/*.md')
pat = re.compile(r'\[([^\]]*)\]\((https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+))')
counts = collections.defaultdict(set)
for f in files:
    txt = open(f, encoding='utf-8', errors='replace').read()
    for m in pat.finditer(txt):
        owner, repo = m.group(3), m.group(4)
        if owner in ('sindresorhus', 'github'): continue
        counts[(owner + '/' + repo).lower()].add(os.path.basename(f))
counts = {fn: len(s) for fn, s in counts.items()}
json.dump({'counts': counts}, open(base + '/refs.json', 'w', encoding='utf-8'))
print('files:', len(files), 'repos:', len(counts), 'cross>=2:', sum(1 for c in counts.values() if c >= 2))
