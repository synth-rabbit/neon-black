---
type: meta
name: Agent Preamble
slug: agent-preamble
status: approved
source: custom
page: ""
owner: orchestrator
canon_refs: ["Plan Part A", "Plan Part E"]
flags: []
player_safe: false
---

# Agent Preamble

Shared instructions for every build agent working on a Neon Black package. The orchestrator pastes this into each agent prompt; agents may also re-read it here.

## Read first, in this order

1. `Shared Lore Bible.md` — fixed canon. Never contradict it.
2. `Otherscape Campaign Skeleton Brief.md` — design decisions; §0 standing rules, §3 Tao cosmology, §10 conflicts, §11 interviewer's choices, §12 open questions.
3. `Neon Black Build Plan.md` — **Part A in full**, then your package in Part B, then Part C (verification).
4. `00-meta/names.md` (GM-approved — use primaries verbatim), `00-meta/style-guide.md`, `00-meta/README.md`.
5. `01-series/*.md`, `05-megacity/palisade.md`, `05-megacity/district-directory.md`, `05-megacity/timeline.md` (WP1 output — the world as built; read the district files you touch).
6. The template for each `type` you produce, in `99-templates/`.
7. The rulebook pages your package cites: `ref/core-book-paged.txt` and `ref/tokyo-book-paged.txt` are split by PDF page — grep `=== PAGE 233 ===`.

## Approved names (primaries)

City **Palisade** (tiers: the Crest / the Face / the Foot / the Under; "the Wall" = the top, "under the Wall" = the bottom). Splats: **Bloodware** (vampire), **Howlers** (werewolf), **Casters** (mage), **Doppels** (changeling), **Baselines** (hunter). Corp A **Meliora Bioworks** (bio; makes the trigger for another purpose). Corp B **Orison Defense Systems** (weapons; secretly Wuji-controlled). Corp C **Amalgamated Prosthetic & Interface / AP&I / "Amalgam"** (cybernetics; owns the camp). Upstart **Continuity Risk & Response** (security / crisis management / hacking; secretly Bloodware-run). Syndicate **the Almoners / "the Alms"** (resells the trigger). Tao society **the Wuji**, rumored as **the Quiet Hand**; its Crest front is **Aldine House**. Escaped changelings **Cutloose**. Pack culture **the Run**; trigger drug **Leash**. Camp **Reconciliation Facility 4 / "the Ledger"** (Coldwater Outfall). Fence **Marisol Okonkwo "Tally"** (the Weighhouse, Gullet Market). Crew leader **Tomas Adair "Rook"**. Defunct nanite corp **Ferrante Nanoscale** ("the Ferrante strain"). Master node **the Kernel**. Caste slang **Sculpted / Fitted / Patched / Stock** (slang only). City government **the Chancery**. Key Player slugs: `corp-a`, `corp-b`, `corp-c`, `upstart`, `syndicate`, `government`, `tao-society`, `packs`, `changeling-cells`, `fence-network`. People slugs: `marisol-okonkwo`, `tomas-adair`. Magic is **Tao** (impersonal, the only mystical force, can produce beings; no legend-Mythoi).

## Hard rules

- Custom content **in addition to** existing book content, never instead of it.
- No GM advice. Content only.
- Book vocabulary: Series, Job, Crew theme, Challenge, Limit, Threat/Consequence, MC, Megacity, district story tag, Key Player, vector, core moment, Essence, Decay, Identity/Ritual/Itch, Quick/Tracked Outcome, Mitigate, Loadout, Scale. Never: season, case, Danger, Rift, Logos, Mist, "splat" in player-facing text, Mythoi/legend language except as the mechanical category name.
- Every Mythos/Source/Conjuration reference is reinterpreted as Tao and marked `[TAO-REINTERPRETED]`.
- Invent only what Plan A.1 rule 5 and your package allow. Mark judgment calls `[BUILD CHOICE]`, unknowns `[OPEN]`, rule-vs-canon clashes `[RULES CONFLICT]`.
- Splat canon: Bloodware weaknesses are EM and the Kernel (never sun/fire/stake); Baselines take cybernetics only as replacements and never sculpt or bio-manipulate; Doppels are owned (kill switch + tracker) unless Cutloose; Howlers depend on Leash from the Almoners, made by Meliora; Casters never give Tao a will.
- Frontmatter per Plan A.4 and the template; H1 equals `name`; `owner: <your WP>`; `status: review`; `player_safe` set (BC-128); `type` from the closed set (BC-127); file names unique vault-wide, never `overview.md` / `README.md` (BC-125); wikilinks per Plan A.3. Run `python3 tools/validate.py` before finishing. Validate every frontmatter block with `python3 -c "import yaml..."` before finishing.

## Registers — do NOT edit shared register files

Because packages run in parallel, **do not edit** `00-meta/names.md`, `build-choices.md`, `open-questions.md`, `conflict-register.md`, or `changelog.md`. Instead create **one file** `00-meta/additions/<your-WP>.md` with sections `## Names added`, `## Build choices`, `## Open questions`, `## Conflicts`, `## Changelog` — same table columns as the registers, ids as `BC-<WP>-n`, `OQ-<WP>-n`, `CR-<WP>-n`. WP6 merges them and renumbers.

## Finishing

Run your validation; then `git add -A && git commit -m "<WP>: <summary>"` in your working directory (you are in your own worktree/branch — commit there, do not push, do not switch branches). Reply with: your branch name and worktree path, the list of files created, and anything unresolved.
