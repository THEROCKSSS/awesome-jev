#!/usr/bin/env python3
"""Regenerate the README's project-list section from data/jev.json."""
import json, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARK = '<!-- PROJECTS:BEGIN -->'
END = '<!-- PROJECTS:END -->'
CATS = [
    ('official', 'Official Resources'), ('openmodels', 'Open & Jev-like Models'),
    ('sdk', 'SDKs, APIs & Routers'), ('agents', 'Agents & Automation'),
    ('mcp', 'MCP & Agent Tools'), ('web', 'Web & Browsing'),
    ('devtools', 'Developer Tools'), ('games', 'Games & Play'),
    ('chat', 'Chat & Messaging'), ('finance', 'Finance & Trading'),
    ('safety', 'Safety, Routing & Guardrails'), ('productivity', 'Productivity & Knowledge'),
    ('media', 'Media & Content'), ('mobile', 'Mobile & Desktop Apps'),
    ('home', 'Home, IoT & Robotics'), ('awesome', 'Awesome Lists & Catalogs'),
    ('more', 'More Projects'),
]

def main():
    entries = json.load(open(os.path.join(ROOT, 'data', 'jev.json'), encoding='utf-8'))
    top = entries[0]['added']
    lines = []
    fresh = [e for e in entries if e['added'] >= top]
    # seed day: every entry shares one date — don't dump the whole catalog as "new"
    if fresh and len(fresh) < len(entries):
        shown = fresh[:50]
        lines.append(f"### 🆕 New today ({top})\n")
        lines += [f"- [{e['name']}]({e['url']}) — {e['desc']} _(★{e['stars']})_" for e in shown]
        if len(fresh) > len(shown):
            lines.append(f"- *{len(fresh)-len(shown)} more on the [full catalog](https://therocksss.github.io/awesome-jev/)*")
        lines.append("")
    for cid, label in CATS:
        rs = [e for e in entries if e['category'] == cid]
        if not rs:
            continue
        rs.sort(key=lambda e: (-e['stars'], -e['cross']))
        lines.append(f"### {label} ({len(rs)})\n")
        shown = rs[:50]
        lines += [f"- [{e['name']}]({e['url']}) — {e['desc']} _(★{e['stars']}, {e['lang'] or 'n/a'})_" for e in shown]
        if len(rs) > len(shown):
            lines.append(f"- *{len(rs)-len(shown)} more — see the [full browsable catalog](https://therocksss.github.io/awesome-jev/)*")
        lines.append("")
    body = MARK + "\n\n" + "\n".join(lines) + "\n" + END
    path = os.path.join(ROOT, 'README.md')
    src = open(path, encoding='utf-8').read()
    a, b = src.index(MARK), src.index(END) + len(END)
    open(path, 'w', encoding='utf-8').write(src[:a] + body + src[b:])
    print(f'README regenerated: {len(entries)} entries')

if __name__ == '__main__':
    main()
