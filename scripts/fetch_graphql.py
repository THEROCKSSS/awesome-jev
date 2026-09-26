# Fetch GitHub metadata via batched GraphQL (token from gh keyring, never printed).
import json, os, subprocess, urllib.request

base = os.environ['LOCALAPPDATA'] + '/Temp'
d = json.load(open(base + '/refs.json', encoding='utf-8'))
counts = d['counts']

cands = {fn for fn, c in counts.items() if c >= 2}
for fn in counts:
    if 'jev' in fn.split('/')[1] or 'typesafe' in fn.split('/')[1]:
        cands.add(fn)
for f in ['jev_name.json', 'ts_name.json', 'awesome_jev.json', 'sys1.json', 'tsai.json', 'jev2.json']:
    try:
        for r in json.load(open(base + '/' + f, encoding='utf-8')):
            cands.add(r['fullName'].lower())
    except Exception:
        pass
cands = sorted({c for c in cands if c.count('/') == 1})

try:
    out = json.load(open(base + '/gq.json', encoding='utf-8'))
except Exception:
    out = {}
todo = [fn for fn in cands if fn not in out]
print('candidates:', len(cands), 'resolved:', len(out), 'todo:', len(todo), flush=True)

token = subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True).stdout.strip()
assert token, 'no gh token'

B = 50
for i in range(0, len(todo), B):
    chunk = todo[i:i+B]
    lines = []
    for j, fn in enumerate(chunk):
        o, r = fn.split('/')
        lines.append(f'r{j}: repository(owner: "{o}", name: "{r}") {{ nameWithOwner description stargazerCount primaryLanguage {{ name }} pushedAt createdAt homepageUrl isFork owner {{ login }} licenseInfo {{ spdxId }} }}')
    q = 'query { ' + ' '.join(lines) + ' }'
    body = json.dumps({'query': q}).encode()
    req = urllib.request.Request('https://api.github.com/graphql', data=body, headers={
        'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json', 'User-Agent': 'awesome-jev-build'})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print('batch', i, 'ERR', e, flush=True)
        continue
    for j, fn in enumerate(chunk):
        node = (data.get('data') or {}).get('r%d' % j)
        if node:
            out[fn] = node
    json.dump(out, open(base + '/gq.json', 'w', encoding='utf-8'))
    print('batch', i, 'ok, total', len(out), flush=True)

json.dump(out, open(base + '/gq.json', 'w', encoding='utf-8'))
missing = [fn for fn in cands if fn not in out]
print('resolved:', len(out), 'missing:', len(missing))
json.dump(missing, open(base + '/gq_missing.json', 'w', encoding='utf-8'))
