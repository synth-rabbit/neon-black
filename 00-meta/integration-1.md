---
type: meta
name: Integration Pass 1
slug: integration-1
status: review
source: custom
page: ""
owner: WP6
canon_refs: ["Plan Part B WP6", "Plan Part C", "Plan A.2–A.8", "Plan Part F WP-I"]
flags: []
player_safe: false
---

# Integration Pass 1

WP6's report: what was decided, what was fixed, what is owed by owners, what is escalated to the GM, and the vault's counts after the pass. Run on 2026-09-03 over WP0–WP5 output (WP7 and later were not yet written). Verification is `python3 tools/validate.py`, whose checks are the Part C list; its final line at the end of this pass was **0 errors, 4 warnings**, and the warnings are explained in §7.

## 1. Decisions taken

All registered in [[build-choices]] as **BC-125 to BC-138**; none adds a setting fact.

**The renaming convention (BC-125).** File names are unique vault-wide and `slug` equals the basename. No file is named `overview.md`, `README.md`, `reuse.md`, `membership.md`, `existing-kits.md`, `motivations.md`, `vectors.md` or `aftermath.md`. Applied:

| Before | After |
|---|---|
| `05-megacity/overview.md` | `05-megacity/palisade.md` |
| `02-splats/<splat>/overview.md` (×5) | `bloodware.md`, `howlers.md`, `casters.md`, `doppels.md`, `baselines.md` — the GM-adopted setting names, since these are the files players open |
| `02-splats/<splat>/theme-kits/existing-kits.md` (×5) | `<splat>-existing-kits.md` |
| `06-key-players/<kp>/overview.md` (×10) | `<kp>.md` (`corp-a.md` …) |
| `06-key-players/<kp>/membership.md` (×10) | `<kp>-membership.md` |
| `06-key-players/<kp>/challenges/reuse.md` (×10) | `<kp>-reuse.md` |
| `03-self-kits/README.md`, `04-crew/README.md`, `08-challenges/README.md`, `09-loadout/README.md` | `self-kits-index.md`, `crew-index.md`, `challenges-index.md`, `loadout-index.md` |
| `04-crew/motivations.md` | `crew-motivations.md` |
| `tao-society/challenges/wuji-operative.md`, `08-challenges/custom/anti-tao-countermeasure.md` | `wuji-operative-challenge.md`, `anti-tao-countermeasure-challenge.md` |

An NPC and their Challenge never share a slug: `<given-surname>-challenge.md` (`tomas-adair-challenge`) or a distinct title or handle (`chimney`, `six-at-the-hatch`, `vice-president-marchetti`); a Challenge that would share a Power Set's name takes `-challenge`. Templates carry placeholder slugs. 48 files moved with `git mv` (history preserved); every wikilink was rewritten (`tools/wp6_rename.py`); literal path mentions in prose and in the registers' *Where* columns were rewritten (`tools/wp6_paths.py`) — except in [[changelog]], which is history and keeps the paths of its day. Slugs are frozen from here ([[style-guide]] §8 rule 7). Plan A.2 was amended in place to state the rule; WP7's `breakout.md` / `breakout-vectors.md` / `breakout-aftermath.md` pattern follows it.

**Other conventions.** `book:<slug>` for printed theme kits with one index, [[book-kits-index]] (BC-126); a closed `type` set of eighteen values, eight package-coined values normalized into it (BC-127); `player_safe: true|false` on every file (BC-128); an optional `limits:` block on the `power-set` template (BC-129); [[image-briefs]] and `assets/manifest.md` conventions (BC-137); validate.py's documented vocabulary exceptions (BC-136).

**Register merge.** The ten `00-meta/additions/*.md` files were merged into [[names]], [[build-choices]], [[open-questions]], [[conflict-register]] and [[changelog]] and every package-local id renumbered vault-wide (`tools/wp6_renumber.py`, map in `tools/wp6_idmap.json`): BC-WP… → BC-31 to BC-124 (WP5 had already taken BC-27 to BC-30), OQ-WP… → OQ-22 to OQ-48 (WP4-trio3's Doppel-maker question merged into WP2-changeling's OQ-30), CR-WP… → CR-9 to CR-19. The additions files are kept as the packages' originals and are excluded from validation.

## 2. Fixes made

- **Duplicate Challenge pairs reconciled, not merged** (`tools/wp6_pairs.py`): the Ledger's routine vs. its electronic system (BC-131), the escapee list's detection vs. pricing layers (BC-132), the two Howler overlays (BC-133), and the overlay-plus-profile pairs for the anti-Tao countermeasure and the Wuji operative (BC-134). CR-17 and OQ-46 closed by these; the one wording difference between the Howler overlays became OQ-49.
- **Cross-trio reconciliation** (BC-135): alignment sentences in [[corp-a]], [[corp-c]], [[upstart]], [[syndicate]] and [[fence-network]] so the anti-Tao programmes (Adjunct Series, Field Assurance; BC-117), Continuity's purchase of concurrences (BC-122), and Orison hardware surfacing at the Kitchen and the Weighhouse read the same from every side. [[amalgam-stack]] aligned with the band-grade exemption (BC-130; CR-16 still the GM's).
- **Splat-canon greps** (Plan C.3) clean: no sun/fire/stake/garlic/silver weakness anywhere in Bloodware or Howler files; no sculpt or bio-manipulation in any hunter kit, trope or Special; no sentence giving Tao a will. validate.py runs these on every pass.
- **Stale `(pending WP#)` annotations** cleared where the target now exists: links into `06-key-players/*` and to Tally and Rook (WP1, WP2, WP3 files), the node-scanner ([[kernel-scanner-rig]]) and the Bloodware overlay ([[bloodware-power-set]]) in [[tomas-adair-challenge]], the countermeasure profile in [[casters]] and [[anti-tao-countermeasure]], the Baseline and Doppel PC Specials in [[corp-b-membership]] and [[changeling-cells-membership]], the Wuji Self kit in [[mage-existing-kits]]. WP7 targets (`[[breakout]]`, `[[investigation]]`, `[[acquisition]]`) stay pending and are the registered pending list in validate.py.
- **Cross-links the owners asked for**: [[doppels]] → [[cutloose-cell]], [[casters]] → [[wuji-initiate]] (WP3's note); [[howlers]] → [[pack-affiliation]] already existed.
- **Markers and flags** brought into agreement (Plan A.4, [[style-guide]] §7): four membership files dropped a `BUILD CHOICE` flag with no marker in the body; three pack Challenges and [[corp-c]] gained the inline `[TAO-REINTERPRETED]` their flags promised; three loadout items had markers in code spans (invisible to the check) rewritten in the bold form with their BC ids ([[guard-baton-and-fob]] BC-27, [[tao-null-round]] and [[null-field-emitter]] BC-29).
- **Frontmatter**: `type` normalized to the closed set on 33 files (eight package-coined values — `splat`, `kit-index`, `kit-list`, `power-set-list`, `challenge-reuse`, `reuse-map`, and `meta` outside `00-meta/`); `player_safe` added to the 241 files that lacked it; templates fixed to match (`template-key-player`, `template-job` placeholder slugs; `template-power-set` `limits:` block); every YAML block parses.
- **Transcription**: the *Wanted* crew kit's fourth weakness tag restored from Core p. 157 (BC-138).
- **Registers**: rows BC-125 to BC-138, OQ-49 and OQ-50 written; OQ-34, OQ-46, CR-15, CR-17 and CR-18 marked resolved with the resolving BC; the *Where* columns of merged rows point at the renamed files.
- **Templates**: every template carries the common fields of Plan A.4 including `player_safe`, validates, and instantiates to a unique slug.
- **Image briefs, pass 1**: [[image-briefs]] — style preamble finalized from [[tone]] and [[style-guide]] §4; 66 blocks (18 districts, 10 emblems, 10 territory shots, 23 NPC paper puppets, 5 splat images); `assets/manifest.md` pre-filled with every row at `not generated`.

## 3. Fixes required from owners

Nothing blocks WP7. The items below are for the owning package at its next touch, or for WP8:

| Owner | Item | Where |
|---|---|---|
| WP8 | Audit `player_safe` values file by file (WP6 set them by folder rule, BC-128) and decide how the five splat overviews' `## MC only` sections are excerpted for the session-zero packet. | [[README]] "Player-safe vs MC-only" |
| WP8 | Three in-world uses of *case* meaning police work remain as warnings (§7); decide whether Plan C.6 forbids the English word in a police context or only the scenario term, and either reword or widen the exception. | [[baselines]], [[extreme-case-tracker]], [[bonded-tracker]] |
| WP2-hunter | The *Unmade* movement name is a proposal awaiting the GM (BC-94); if renamed, two files and one names row change. | [[the-unmade]], [[unmade-cell]] |
| WP4 (any trio) | [[tomas-adair]] has no vector by design; if the GM answers OQ-10/OQ-17/OQ-39/OQ-40 the file is revised, not added to. | [[tomas-adair]] |
| WP9 | Whether a Power Set template's spectra (`limits:`) inherit through `template_ids` is UNVERIFIED (foundry-mapping §8-4); until verified each Challenge repeats its base tags. | [[foundry-mapping]] §4.2 |
| WP-I | Generate pass 1 from [[image-briefs]]; record `method` per puppet in `assets/manifest.md`; link each image from its target with `![[assets/...]]`. | `assets/` |

## 4. Conflicts escalated to the GM rather than resolved

- **OQ-50 — shared surnames across trios.** *Marchetti* (Solenne, Meliora / Constance, Aldine House), *Ferreira* (Ondine, Meliora / Adaeze, Orison), *Solano* (Reidar, Orison / Věra, the Ledger). No file asserts kinship; kinship would be new canon linking a corporation to the Wuji or to the camp. Not renamed: each name is a GM-adopted primary and a rename moves a file. Alternates are in [[names]].
- **OQ-49 — how much of a person a dosed Howler remains.** The two overlays agree on the fact and differ in voice; the GM's reading decides how the Run's Challenges are voiced.
- **CR-16 — AP&I's mandatory augmentation vs. the Baseline line.** The district and the membership file now agree on the band-grade exemption as the provisional reading (BC-106, BC-130); the three options remain the GM's.
- **OQ-30 — who makes Doppels.** Two packages' proposals merged into one row; no file decides.
- **Names still awaiting yes/no**: everything under "Added by WP2–WP5" in [[names]] is a proposal, as before; the five splat file names now use the adopted primaries, so a change there moves a file.

## 5. Counts after the pass

| Type | Files | | Type | Files |
|---|---|---|---|---|
| theme-kit | 32 | | district (`districts/`) | 18 (+3 `district`-schema index files: [[palisade]], [[district-directory]], [[timeline]]) |
| crew-kit | 3 | | key-player | 10 |
| character-trope | 10 | | npc | 23 |
| pc-special | 17 | | challenge | 38 |
| crew-special | 4 | | power-set | 14 |
| loadout-item | 30 | | membership | 10 |
| series | 4 | | splat-overview | 5 |
| index | 28 (incl. [[book-kits-index]], [[manifest]]) | | meta | 11 |

260 content files + 13 templates = 273 validated files; 48 renamed; 269 modified in the working tree; 4 new (`02-splats/book-kits-index.md`, `00-meta/image-briefs.md`, `00-meta/integration-1.md`, `assets/manifest.md`) plus `tools/`. Registers: 132 BC rows, 54 OQ rows, 21 CR rows. Book kits indexed: 112; `book:` references from tropes: 30. Image briefs: 66.

## 6. Tools

`tools/validate.py` (Part C checks; exit 1 on any error), `wp6_rename.py` (renames and link rewrites), `wp6_renumber.py` + `wp6_idmap.json` (register ids), `wp6_merge.py` (additions → registers), `wp6_bookkits.py` (book-kits index), `wp6_pairs.py` (duplicate Challenge pairs), `wp6_paths.py` (literal path mentions), `linkcheck.py` (link-only quick check). The WP6 scripts were run once and are kept as the record of what was done; validate.py is the one WP8 and WP9 run.

## 7. Final validation

`python3 tools/validate.py` → **ERRORS: 0 · WARNINGS: 4 in 4 files**:

1. [[crew-index]] — `[[breakout]]` pending WP7a (registered pending list; cleared when WP7a writes it).
2. [[baselines]] — "an off-duty Chancery investigator working a case nobody wants".
3. [[extreme-case-tracker]] — "before it becomes a case".
4. [[bonded-tracker]] — "the cases too extreme for a beat cop".

Items 2–4 are the English word for police work inside player-safe Baseline text, not the scenario term Plan C.6 forbids; validate.py reports them because they match its scenario cue and WP6 left them for WP8's ruling (§3) rather than reword an owner's prose. The kit name *Extreme-Case Tracker* is a GM-adopted primary and passes as a hyphenated title.
