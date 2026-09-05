---
type: meta
name: README
slug: README
status: review
source: custom
page: ""
owner: WP0
canon_refs: ["Bible (all)", "Brief §0", "Brief §9.2", "Plan A.1–A.8", "Plan Part B", "Plan Part C"]
flags: []
player_safe: false
---

# README

**Neon Black** — a pilot campaign for *:Otherscape* (Mist Engine): a cyberpunk megacity in which technology makes the five classic World-of-Darkness creatures, an older force called Tao runs underneath, and a crew of escaped camp labor starts at the bottom of a caste ladder built out of their own bodies. This vault is an Obsidian vault first and a Foundry VTT module later ([[foundry-mapping]]). This page is the entry point; the Maps of Content below list every file.

![[assets/cover.png]]

## Where to start

| If you are… | Start at |
|---|---|
| the MC, reading before session one | [[reading-order]] — the dependency order of the files, about a day's reading; the first two sections are enough for session one |
| a player | [[session-zero-packet]] — every file you may be handed whole; nothing MC-only is linked from it |
| the GM deciding what is still yours | [[integration-2]] §5 (the short list), then [[open-questions]] and [[build-choices]] |
| the next build package or reviewer | [[integration-2]] (what WP8 changed), [[integration-1]] (what WP6 decided), then `python3 tools/validate.py` |
| the Foundry conversion (WP9) | [[foundry-mapping]] |

## Authority

Three source documents in the vault root are **canon and instructions**, in this order:

1. `Shared Lore Bible.md` — fixed setting canon. Nothing in the vault may contradict it.
2. `Otherscape Campaign Skeleton Brief.md` — design decisions, standing rules (§0), Tao cosmology (§3), the conflict register (§10), interviewer's choices (§11), open questions (§12), naming guidance (§9.4).
3. `Neon Black Build Plan.md` — conventions and schemas (Part A), work packages (Part B), verification (Part C), Foundry notes (Part D).

Everything under the numbered folders is **build output**. `ref/` holds the two rulebooks as paged text and the Foundry system's data model — reference material, not part of the vault.

## Maps of Content — one per folder

| Folder | Map of Content | What is in it |
|---|---|---|
| `00-meta/` | this page | The registers, the style guide, the integration reports, the image briefs, [[session-zero-packet]], [[reading-order]] — see "Registers" below |
| `01-series/` | [[series-index]] | [[series-concept]], [[pillars]], [[spine-and-clock]] (with the clock arithmetic of the three jobs), [[tone]] |
| `02-splats/` | [[splats-index]] | Five character packages — `vampire/` Bloodware, `werewolf/` Howlers, `mage/` Casters, `changeling/` Doppels, `hunter/` Baselines — each with a player-safe overview, an MC-notes file, theme kits, tropes, PC Specials and Power Sets; [[book-kits-index]] for every printed kit referenced |
| `03-self-kits/` | [[self-kits-index]] | Fifteen custom Self kits for Palisade's institutions and circumstances, plus [[existing-self-kits]] |
| `04-crew/` | [[crew-index]] | Crew kits, [[crew-motivations]], Crew Theme Specials, and the end-of-session-one procedure |
| `05-megacity/` | [[megacity-index]] | [[palisade]], [[palisade-player-primer]], [[district-directory]], [[timeline]], eighteen districts |
| `06-key-players/` | [[key-players-index]] | Ten Key Player folders: overview (with twist), membership, characters, Challenges, reuse list |
| `07-jobs/` | [[jobs-index]] | Three jobs — [[breakout]] (session one), [[investigation]], [[acquisition]] (the pivot) — each with vectors, scenes, Challenges, job-only characters and an aftermath |
| `08-challenges/` | [[challenges-index]] | The cross-cutting custom Challenges (including [[secret-war-goes-public]]), the Power Set overlays, and [[generic-reuse-map]] |
| `09-loadout/` | [[loadout-index]] | Street Catalog additions and [[existing-catalog]]; seven items are player-safe |
| `99-templates/` | — | One template per `type` (Plan A.4); `template: true`, never content |
| `assets/` | `assets/manifest.md` | Every image the vault expects, its brief, its target and its status (WP-I) |
| `tools/` | — | `validate.py` (Plan Part C, run before finishing any package); the `wp6_*` and `wp8_*` scripts that made the two integration passes; WP9's conversion scripts |

## How to read a file

- Every file has YAML frontmatter (schemas in Plan A.4, restated in [[foundry-mapping]] and instantiated in `99-templates/`), then a level-1 heading equal to its `name`. One entity per file; file names are unique vault-wide and `slug` is the file name (BC-125).
- Cross-references are `[[wikilinks]]` by slug ([[style-guide]] §8). A `player_safe: true` file links only to `player_safe: true` files (Plan C.8; BC-175) — it cites a register or an MC-only file in a code span instead.
- Four inline markers carry the vault's honesty: `[RULES CONFLICT]`, `[BUILD CHOICE]`, `[TAO-REINTERPRETED]`, `[OPEN]` — each paired with a register row ([[style-guide]] §7). Book page citations are `(Core p. 243)` and `(Tokyo p. 73)` and match the `=== PAGE n ===` markers in `ref/`.
- `status`: `draft` (owner still working), `review` (complete, awaiting integration or the GM), `approved` (GM-approved). `player_safe`: whether the whole file may be shown to a player (BC-128).

## Registers

| Register | What it holds | Row ids |
|---|---|---|
| [[names]] | Every proposed name and whether the GM adopted it; the specialty and caste proposals; the shared-surname note (OQ-50) | — (rows cite BC ids) |
| [[style-guide]] | Naming register, tag voice, motivation voice, tone words, forbidden terms, markers, wikilinks, slugs | — |
| [[build-choices]] | The interviewer's choices and every `[BUILD CHOICE]` since, grouped by package; WP8's rows are BC-171 to BC-180 | `BC-n` |
| [[open-questions]] | Every open question with a status board on top (open / proposal on file / GM decision needed / resolved) | `OQ-n` |
| [[conflict-register]] | Rules-vs-canon conflicts, with the same status board | `CR-n` |
| [[foundry-mapping]] | Frontmatter → Foundry data model; module skeleton; WP9's verification list | §8 items |
| [[changelog]] | Dated entries per package, newest first | — |
| [[integration-1]] · [[integration-2]] | The two integration reports: decisions, fixes, counts, what the GM must decide | — |
| [[image-briefs]] | One prompt block per image (pass 1: districts, Key Players, NPCs, splats; pass 2: scenes, job NPCs, cover) | `### <assets path>` |
| [[agent-preamble]] | The shared instructions every build agent worked under | — |

## Player-safe vs MC-only

The test for any single file is its `player_safe` field, and the packet is the list: [[session-zero-packet]] links every `player_safe: true` file in the vault and nothing else. In practice: the five splat overviews (their MC sections split into `<splat>-mc-notes`, BC-176), the kits, tropes and PC Specials, [[book-kits-index]], all of `03-self-kits/` and `04-crew/`, [[palisade-player-primer]], and seven Ledger-issue and Weighhouse loadout items. Everything else — `01-series/`, `05-megacity/` bar the primer, `06-key-players/`, `07-jobs/`, `08-challenges/`, every `power-sets/` folder, the rest of `09-loadout/`, and all of `00-meta/` including this page — is MC-only.

## Standing rules in one place (Plan A.1)

Existing book content **and** custom content, never one instead of the other. No GM advice. Flag, don't resolve. Invent only names, Key Player twists, Generator-derived district content, and the flagged specialty proposal. Book vocabulary only. Tao is the only mystical force; every legend reference is reinterpreted and marked.
