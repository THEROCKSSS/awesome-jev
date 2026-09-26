# Contributing

Want a project added, moved, or removed? Open an issue or a pull request.

## Adding a project

The catalog is machine-maintained: `data/jev.json` is regenerated daily and
hand-edits to it are overwritten. To get a project in, make sure it is
**discoverable**, then request it:

1. The repo must be public on GitHub and use, implement, or integrate
   Jev / TypeSafe System One (or be official TypeSafe tooling).
2. Put the Jev / TypeSafe System One connection in the GitHub repo **name,
   description, or homepage**. The daily scraper does not search README bodies.
   A `jev` topic helps discovery, but a topic alone does not establish relevance.
3. New repositories can have zero stars. The daily discovery checks multiple
   GitHub search orders, including recently created repositories, and requires
   a clear connection in the repo name, description, official owner, or homepage.

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

Report archived, renamed, or unrelated entries for review. The daily updater
discovers and refreshes projects; it does not automatically remove existing
entries. A corrected entry keeps its original `added` date.

## Ground rules

- No self-promotion spam: entries need a verifiable Jev / TypeSafe System One
  connection. Fresh zero-star repos can qualify when the connection is clear.
- Entries show GitHub's own description; we do not rewrite or endorse them.
- This catalog is community-run and **not affiliated with TypeSafe**.
