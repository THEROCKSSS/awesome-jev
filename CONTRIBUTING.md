# Contributing

Want a project added, moved, or removed? Open an issue or a pull request.

## Adding a project

The catalog is machine-maintained: `data/jev.json` is regenerated daily and
hand-edits to it are overwritten. To get a project in, make sure it is
**discoverable**, then request it:

1. The repo must be public on GitHub and use, implement, or integrate
   Jev / TypeSafe System One (or be official TypeSafe tooling).
2. Its GitHub **description, topics, or homepage** should mention `jev`,
   `system one`, or `typesafe.ai` — the daily scraper reads those fields, not
   the README body. Add a `jev` topic to your repo if nothing else applies.
3. ≥5 stars, or linked from a community list.

Open an issue titled `Add: owner/repo` with a one-line reason. Maintenance PRs
that edit `data/jev.json` directly are only merged if they fix an admission
mistake (e.g. a non-Jev "typesafe" library that slipped in) — the daily run
must be able to reproduce the rest.

## Categories

Entries are auto-categorised by repo name + description keywords. If an entry
sits in the wrong category, open an issue — the classifier rules in
`scripts/build_dataset.py` (seed) and `scripts/update_list.py` (daily) get
updated, not individual rows.

## Removing / fixing entries

Projects that get archived, renamed, or turn out to be unrelated get removed on
the next scrape or by issue report. A repo renamed under the same owner keeps
its `added` date — renames don't reset "new".

## Ground rules

- No self-promotion spam: the ≥5-stars-or-2-lists bar exists so the list can't
  be filled with fresh zero-star repos.
- Entries show GitHub's own description; we do not rewrite or endorse them.
- This catalog is community-run and **not affiliated with TypeSafe**.
