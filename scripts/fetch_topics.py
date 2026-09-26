# Signal pass 2: repo topics via GraphQL + README 'jev' mentions via search API.
import json, os, subprocess, urllib.request, time, sys

base = os.environ['LOCALAPPDATA'] + '/Temp'
gq = json.load(open(base + '/gq.json', encoding='utf-8'))
token = subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True).stdout.strip()

names = sorted(gq.keys())
try:
    topics = json.load(open(base + '/topics.json', encoding='utf-8'))
except Exception:
    topics = {}
names = [n for n in names if n not in topics]
print('topics todo:', len(names), flush=True)
B = 80
for i in range(0, len(names), B):
    chunk = names[i:i+B]
    lines = []
    for j, fn in enumerate(chunk):
        o, r = fn.split('/')
        lines.append(f'r{j}: repository(owner: "{o}", name: "{r}") {{ nameWithOwner repositoryTopics(first: 10) {{ nodes {{ topic {{ name }} }} }} }}')
    q = 'query { ' + ' '.join(lines) + ' }'
    body = json.dumps({'query': q}).encode()
    req = urllib.request.Request('https://api.github.com/graphql', data=body, headers={
        'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json', 'User-Agent': 'awesome-jev-build'})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print('batch', i, 'ERR', e, flush=True); continue
    for j, fn in enumerate(chunk):
        node = (data.get('data') or {}).get('r%d' % j)
        if node:
            topics[fn] = [n['topic']['name'] for n in node['repositoryTopics']['nodes']]
    if (i // B) % 5 == 0:
        json.dump(topics, open(base + '/topics.json', 'w', encoding='utf-8'))
        print('topics', len(topics), flush=True)
json.dump(topics, open(base + '/topics.json', 'w', encoding='utf-8'))
print('topics done:', len(topics))
