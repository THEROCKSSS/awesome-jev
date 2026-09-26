#!/usr/bin/env python3
"""Build the GitHub Pages artifact with a direct page for each catalog entry."""
import html
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "dist"
NAME = re.compile(r"^[A-Za-z0-9_.-]+$")
TOKENS = ("ROOT", "OWNER", "REPO", "TITLE", "DESCRIPTION", "CATEGORY", "STARS", "LANGUAGE", "PUSHED")


def render(template, entry):
    owner, repo = entry["owner"], entry["name"]
    if not NAME.fullmatch(owner) or not NAME.fullmatch(repo) or owner in (".", "..") or repo in (".", ".."):
        raise ValueError(f"Unsafe repository path: {owner}/{repo}")
    values = {"ROOT": "../../../", "OWNER": owner, "REPO": repo,
              "TITLE": f"{owner} / {repo}", "DESCRIPTION": entry.get("desc") or "Read this project's original README on Awesome Jev.",
              "CATEGORY": entry.get("category") or "more", "STARS": str(entry.get("stars") or 0),
              "LANGUAGE": entry.get("lang") or "Language not listed", "PUSHED": entry.get("pushedAt") or "unknown"}
    # One replacement pass prevents source text from being treated as a template.
    return re.sub(r"__(" + "|".join(TOKENS) + r")__", lambda match: html.escape(values[match.group(1)], quote=True), template)


def build():
    entries = json.loads((ROOT / "data/jev.json").read_text(encoding="utf-8"))
    template = (ROOT / "site/repo.html").read_text(encoding="utf-8")
    sanitizer = ROOT / "node_modules/dompurify/dist/purify.min.js"
    if not sanitizer.is_file():
        raise SystemExit("Run npm ci --ignore-scripts before building (DOMPurify is required).")
    expected = ROOT.resolve() / "dist"
    is_junction = getattr(DEST, "is_junction", lambda: False)()
    if DEST.resolve() != expected or DEST.is_symlink() or is_junction:
        raise SystemExit("Unexpected dist path; refusing to replace it")
    if DEST.exists():
        shutil.rmtree(DEST)
    (DEST / "assets").mkdir(parents=True)
    shutil.copy2(ROOT / "index.html", DEST / "index.html")
    for asset in (ROOT / "assets").iterdir():
        if asset.is_file():
            shutil.copy2(asset, DEST / "assets" / asset.name)
    shutil.copy2(sanitizer, DEST / "assets/purify.min.js")
    (DEST / "data").mkdir()
    for name in ("jev.json", "meta.json"):
        shutil.copy2(ROOT / "data" / name, DEST / "data" / name)
    seen = set()
    for entry in entries:
        key = (entry["owner"].lower(), entry["name"].lower())
        if key in seen:
            raise ValueError(f"Duplicate repository: {entry['owner']}/{entry['name']}")
        seen.add(key)
        path = DEST / "repo" / entry["owner"] / entry["name"]
        path.mkdir(parents=True)
        (path / "index.html").write_text(render(template, entry), encoding="utf-8")
    (DEST / ".nojekyll").touch()
    print(f"Built {len(entries)} repository pages in {DEST}")


if __name__ == "__main__":
    build()
