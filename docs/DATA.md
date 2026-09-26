# Data: `data/jev.json`

The single source of truth for both the website and the README. One JSON array,
rewritten daily by GitHub Actions.

## Entry schema

```json
{
  "name":      "jev-trader",                     // repo name
  "owner":     "jarrodwatts",                    // GitHub owner (lowercased display only in url)
  "url":       "https://github.com/jarrodwatts/jev-trader",
  "desc":      "One AI trade decision every Monad block…",  // GitHub's own description, ≤240 chars
  "stars":     2388,                             // refreshed daily (top 150 by stars)
  "lang":      "TypeScript",                     // primary language or null
  "added":     "2026-09-25",                     // date the catalog admitted the repo
  "pushedAt":  "2026-09-24",                     // last push (YYYY-MM-DD)
  "cross":     7,                                // # of community lists linking it (initial build)
  "topics":    ["jev", "trading"],               // GitHub topics, max 8
  "category":  "finance"                         // one of the ids below
}
```

Categories: `official`, `awesome`, `sdk`, `openmodels`, `agents`, `mcp`, `web`,
`devtools`, `games`, `chat`, `finance`, `safety`, `productivity`, `media`, `mobile`,
`home`, `more`. Sorting: newest `added` first, then stars descending — so "new today"
is always `added == max(added)`.

## Admission rules

A repo enters the catalog when **all** of these hold:

1. **Jev-relevant by its own metadata** — its name, description, topics, or homepage
   mentions `jev`, `System One`, or TypeSafe the company (`typesafe.ai`). The generic
   adjective "typesafe" (TypeScript utility libraries, Lightbend "Typesafe Config") is
   explicitly excluded.
2. **Not a generic fork** — forks are excluded unless they carry their own Jev work.
3. **Public GitHub repository** that resolves via the GitHub API (no 404s), and
   community lists link it, or it has ≥5 stars.
4. **Described** — GitHub description must be non-empty, so the catalog never shows a
   bare name.

The initial 1,200-entry seed was built by parsing 21 community awesome lists
([docs/AWESOME_LISTS.md](AWESOME_LISTS.md)), resolving every link through the GitHub
API, and applying the rules above.

## Daily pipeline (`.github/workflows/daily-update.yml`)

1. `scripts/update_list.py` — searches GitHub (`jev` in name/description/readme/topics,
   `topic:jev`, `topic:typesafe`), applies admission rules, refreshes stars on the top
   150, stamps `added`, sorts, writes `data/jev.json`.
2. `scripts/gen_readme.py` — regenerates the README between the `PROJECTS:BEGIN/END`
   markers (New-today section + top 50 per category).
3. `git-auto-commit-action` commits both files as `chore: daily catalog update`.
4. `pages.yml` deploys `index.html` + `data/` to GitHub Pages on every push to `main`.

The script runs unauthenticated-tolerant but prefers `gh` (higher rate limits). A
workflow run without `GITHUB_TOKEN` access will refresh fewer stars but never corrupts
the dataset — it only writes the JSON after a complete pass.

## Reproducing the initial seed locally

The build tooling lives in `scripts/` (development-time only; the daily pipeline needs
only `update_list.py` + `gen_readme.py`):

```
parse_signals.py   # parse harvested list markdown -> section-aware link signals
rebuild_refs.py    # flat cross-list link counts
fetch_graphql.py   # batched GitHub metadata resolution (needs gh auth)
fetch_topics.py    # GitHub topics for every candidate
build_finalsets.py # admission rules -> core set
build_dataset.py   # categorize, filter, dedupe -> data/jev.json
```
