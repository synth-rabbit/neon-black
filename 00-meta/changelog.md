---
type: meta
name: Changelog
slug: changelog
status: review
source: custom
page: ""
owner: WP0
canon_refs: ["Plan Part E"]
flags: []
player_safe: false
---

# Changelog

One dated entry per package run, newest first. Each entry lists every file created or changed, in full paths from the vault root, and any register rows added.

## 2026-09-03 — WP8 Integration pass 2

Report: [[integration-2]]. Registers: BC-171 to BC-180, OQ-55, OQ-56; the WP7a–c additions merged below and renumbered (`tools/wp8_idmap.json`: `BC-WP7a-1…12` → BC-139…150, `BC-WP7b-1…10` → BC-151…160, `BC-WP7c-1…10` → BC-161…170, `OQ-WP7a-1` → OQ-51, `OQ-WP7b-1…3` → OQ-52…54); `00-meta/additions/` reduced to its README.

**Created:** `00-meta/session-zero-packet.md`, `00-meta/reading-order.md`, `00-meta/integration-2.md`; `01-series/series-index.md`, `02-splats/splats-index.md`, `05-megacity/megacity-index.md`, `06-key-players/key-players-index.md`; `02-splats/<splat>/<name>-mc-notes.md` ×5 (BC-176); `05-megacity/palisade-player-primer.md` (BC-177); `07-jobs/01-investigation/characters/{wax,anselm-boateng,ivo-meszaros}.md` and `07-jobs/02-acquisition/characters/{margit-nakagawa,ileana-boakye,ilya-sarpong}.md` (BC-174); `tools/wp8_idmap.json`, `wp8_pslinks.py`, `wp8_moc.py`, `wp8_moc_build.py`.

**Renamed:** `07-jobs/01-investigation/challenges/the-collection-run.md` → `the-consignment-window.md` (BC-171).

**Changed — reconciliation (BC-171, BC-172):** `investigation.md`, `investigation-vectors.md`, `investigation-aftermath.md`, `investigation-06-the-lower-gate.md`, `investigation-09-what-the-book-cannot-say.md`, `the-counting-room.md`, `the-factor.md`, `the-consignment-window.md`; `acquisition.md`, `acquisition-vectors.md`, `acquisition-aftermath.md`, `acquisition-01-a-job-at-the-counter.md`, `acquisition-02-the-lower-gate.md`; `06-key-players/government/characters/emeric-vann.md`; `01-series/spine-and-clock.md` ("Clock arithmetic through Job 2"); `07-jobs/00-breakout/breakout.md`, `breakout-aftermath.md` (pending notes cleared; pointer to the arithmetic).

**Changed — conventions (BC-173–175):** the six job companions' frontmatter; the three rosters (`companion: roster`); every `07-jobs/` file's package-local ids renumbered and `additions/` pointers rewritten; `tools/validate.py` (empty pending list; player-safe link check); `Neon Black Build Plan.md` A.2 and A.4; `07-jobs/jobs-index.md` rewritten as the folder's MOC.

**Changed — player packet (BC-175–178):** the five overviews (`## MC only` removed, `player_safe: true`); `02-splats/hunter/baselines.md`, `theme-kits/extreme-case-tracker.md`, `tropes/bonded-tracker.md` (*case* reworded); seven `09-loadout/` items set `player_safe: true`; 67 player-safe files' links re-pointed by `tools/wp8_pslinks.py`; `03-self-kits/self-kits-index.md`, `04-crew/crew-index.md`, `08-challenges/challenges-index.md`, `09-loadout/loadout-index.md` refreshed with a full file table; `00-meta/README.md` rebuilt.

**Changed — registers and briefs:** `names.md` (WP7 rows merged; OQ-50 note; the reconciled place), `build-choices.md` (WP7 rows; WP8 rows; grouping note), `open-questions.md` (WP7 rows; OQ-55–56; status board), `conflict-register.md` (WP7 sections; status board), `00-meta/image-briefs.md` (pass 2: 22 blocks, BC-179), `assets/manifest.md` (22 rows).

**Validation:** `python3 tools/validate.py` → 0 errors, 0 warnings over 340 files. Not committed; the orchestrator commits.

## 2026-09-03 — WP7c (merged from `00-meta/additions/WP7c.md` by WP8)

| Date | Package | Change |
|---|---|---|
| 2026-09-03 | WP7c | Created `07-jobs/02-acquisition/`: the job *The Second Copy* (`acquisition`, 3 sessions, `series_pole: pivot`, `twist_for_pivot: true`), its vectors and aftermath, nine scenes, three custom Challenges and a roster. `[[acquisition]]` now resolves, so its row in `tools/validate.py`'s PENDING list is inert; **the row was deliberately not removed**, because `tools/validate.py` is WP6's shared file and WP7a/WP7b are editing the same object in parallel. WP8 should drop the `acquisition` row (and `breakout` / `investigation` once those exist). |
| 2026-09-03 | WP7c | Coined eight display names (BC-161) and three NPCs held in `acquisition-vectors.md` rather than in `npc` files, because the job folder layout has no `characters/` directory. |
| 2026-09-03 | WP7c | Answered nothing the Bible or Brief reserves; proposed an overrulable answer to OQ-37 (BC-164) and left every other open question as found. |

## 2026-09-03 — WP7b (merged from `00-meta/additions/WP7b.md` by WP8)

Same shape as [[changelog]].


**Created**

- `07-jobs/01-investigation/investigation.md` — **A Full Set of Names**: `job_type: [investigation]`, 2–3 sessions, `series_pole: paycheck`, `twist_for_pivot: false`; two hooks (the Weighhouse offer and the personal hook), the goal, the employer vector, the clue chain as a nine-row table, the two "goes deeper" points, core moments, set pieces, five per-splat hard-choice hooks, all three Investigation complications from Core p. 286, five Key Players and six districts.
- `07-jobs/01-investigation/investigation-vectors.md` — seven vectors with want, push and face: [[marisol-okonkwo]] (employer), [[the-factor]], [[emeric-vann]], [[halima-boyce]], [[rasheeda-novak]], a [[continuity-crisis-response-cell]], and [[the-consignment-window]] (renamed by WP8 from `the-collection-run`) as the faceless time-pressure vector; plus a vector map.
- `07-jobs/01-investigation/scenes/` — nine scenes: [[investigation-01-the-counter-door]] (briefing, Gullet), [[investigation-02-the-labyrinth-route]] and [[investigation-03-the-cold-room]] (the two "snooping around" scenes, Core p. 291), [[investigation-04-the-mirror-rig]] (cyberspace, core moment, goes deeper 1), [[investigation-05-the-back-room-at-lumen]] (set piece, Gallery), [[investigation-06-the-lower-gate]] (core moment, goes deeper 2, Hill), [[investigation-07-the-counting-room]] (confrontation set piece), [[investigation-08-the-cordon]] (climax, tension max, escape), [[investigation-09-what-the-book-cannot-say]] (the lead into Job 2).
- `07-jobs/01-investigation/challenges/` — [[the-factor]] (target, Scale 0), [[a-tag-still-answering]] (mystery, Scale 0), [[the-counting-room]] (barrier, Scale 2), [[the-consignment-window]] (renamed by WP8 from `the-collection-run`) (countdown, Scale 3), and [[investigation-roster]] (`type: index`) listing all twenty-five Challenges the Job fields by slug with role.
- `07-jobs/01-investigation/investigation-aftermath.md` — cash status table, loot catalog in the Core p. 293 format, information rewards, the "if the run cleared" branch, what each of six Key Players learns, the [[secret-war-goes-public]] notch table, seven denouement questions, six Credit Roll prompts, and the explicit handoff line to [[acquisition]].
- `00-meta/additions/WP7b.md` — this file.

**Changed:** nothing. No shared register was edited (agent preamble). No file outside `07-jobs/01-investigation/` and this additions file was touched.

**Register rows added:** BC-151 to -10; OQ-52 to -3; five name rows; no conflicts.

**Notes for WP8.**

1. **Pending links.** `[[acquisition]]` (WP7c) is linked from [[investigation]], [[investigation-09-what-the-book-cannot-say]], [[investigation-aftermath]] and [[the-counting-room]], and remains on validate.py's registered pending list until WP7c writes it. `[[breakout]]` is not linked from this package; the Job assumes the crew are already at the Weighhouse.
2. **The handoff is load-bearing.** [[acquisition]] was given the same text as [[investigation-aftermath]] §Handoff. If WP7c's target differs, the last scene of this Job and BC-153 must be reconciled, not both kept.
3. **Canon audit trail.** No file in this package asserts the Bloodware truth or anything about [[tomas-adair|Rook]]'s motives (OQ-10, OQ-17); the one EM kill is scenery with a refusal attached (BC-159); no file asserts Tao in cyberspace (OQ-15); no file gives Tao a will; the two splat-canon touchpoints (a Baseline offered an enhancement splice and refusing it being the correct read; Bloodware weakness as EM) are written the way WP2 wrote them.
4. **`type` on the two job companions.** `investigation-vectors.md` and `investigation-aftermath.md` carry `type: job`, because the closed set (BC-127) has no better value for a job-folder companion — they are neither an `index` nor a `scene` — and BC-125 names the `<job-slug>-vectors.md` / `<job-slug>-aftermath.md` pattern without assigning a type. For Foundry (foundry-mapping §5, "one JournalEntry per job, scenes as pages") they should convert as **pages inside the Job's entry**, not as three separate entries. WP8/WP9 may prefer a different value; if so it applies equally to WP7a's and WP7c's companions.
5. **Vocabulary.** The English word *case* is avoided throughout in favour of *Job*, including where Core p. 286's Investigation complication is quoted, which is restated as "the Job goes a lot deeper than first thought."

## 2026-09-03 — WP7a (merged from `00-meta/additions/WP7a.md` by WP8)

- **WP7a** — created `07-jobs/jobs-index.md` and `07-jobs/00-breakout/`: `breakout.md` (job), `breakout-vectors.md`, `breakout-aftermath.md`, `scenes/` (7 scene files, `breakout-01-lights-out` … `breakout-07-the-counter-door`), `challenges/` (`the-strike-hour.md`, `landing-stage-post.md`, `the-sludge-flats.md`, `breakout-roster.md`). Registered BC-139 to BC-150 and OQ-51 above. The pending link `[[breakout]]` (registered by WP6) now resolves; `[[investigation]]` and `[[acquisition]]` remain pending WP7b/WP7c. No file outside `07-jobs/` and this additions file was modified.

## 2026-09-03 — WP6 Integration pass 1

Report: [[integration-1]]. Registered BC-125 to BC-138, OQ-49, OQ-50; resolved OQ-34, OQ-46, CR-15, CR-17, CR-18. Categories of change, with the tool that made each:

- **Renames (BC-125)** — 48 files moved with `git mv` and every wikilink rewritten (`tools/wp6_rename.py`): `05-megacity/palisade.md`; the five splat overviews to their setting names and `<splat>-existing-kits.md`; every Key Player `overview` / `membership` / `challenges/reuse` to `<kp>.md` / `<kp>-membership.md` / `<kp>-reuse.md`; four folder `README.md` to `<folder>-index.md`; `04-crew/crew-motivations.md`; `wuji-operative-challenge.md`, `anti-tao-countermeasure-challenge.md`; placeholder slugs in two templates. Literal path mentions in prose and register *Where* columns rewritten (`tools/wp6_paths.py`; this changelog's earlier entries keep the paths of their day).
- **Register merge and renumbering** — the ten `00-meta/additions/*.md` merged into `names`, `build-choices`, `open-questions`, `conflict-register`, `changelog` (`tools/wp6_merge.py`); package-local ids renumbered vault-wide (`tools/wp6_renumber.py`, `tools/wp6_idmap.json`).
- **Book kits (BC-126)** — created `02-splats/book-kits-index.md` (112 printed kits) and normalized the ten tropes' `fixed_kits` / `choice_kits` to `book:<slug>` (`tools/wp6_bookkits.py`).
- **Frontmatter (BC-127, BC-128, BC-129)** — `type` normalized to the closed set on 33 files; `player_safe` added to 241 files; `99-templates/*` updated (common fields, `limits:` on the Power Set template).
- **Duplicate Challenge pairs (BC-131 to BC-134)** — scope paragraphs and cross-references in `ledger-line-security`, `ledger-security-system`, `escapee-recovery-desk`, `escapee-list`, `running-on-leash`, `running-shape`, `leash-frenzy-pack`, `anti-tao-countermeasure`, `anti-tao-countermeasure-challenge`, `wuji-operative`, `wuji-operative-challenge` (`tools/wp6_pairs.py`).
- **Reconciliation edits (BC-130, BC-135, BC-138)** — `amalgam-stack` development 2; standing-table sentences in `corp-a`, `corp-c`, `upstart`, `syndicate`, `fence-network`; the *Wanted* kit's fourth weakness tag in `existing-crew-kits`.
- **Pending annotations cleared** where the target now exists (WP7 targets stay pending): `tomas-adair-challenge`, `casters`, `mage-existing-kits`, `corp-b-membership`, `changeling-cells-membership`, `owned-asset`, and the WP1–WP3 links into `06-key-players/*`. Cross-links added: `doppels` → `cutloose-cell`, `casters` → `wuji-initiate`.
- **Markers and flags** — `changeling-cells-membership`, `corp-b-membership`, `government-membership`, `tao-society-membership` (flag dropped); `chimney`, `kiln-row`, `running-shape`, `corp-c` (inline `[TAO-REINTERPRETED]` added); `guard-baton-and-fob`, `tao-null-round`, `null-field-emitter` (markers rewritten in the bold form with BC ids).
- **Validator (BC-136)** — `tools/validate.py` written: Plan Part C checks, exit 1 on error; documented exceptions for *case*, *season* and `type: meta`. Final run: 0 errors, 4 warnings (see [[integration-1]] §7).
- **Image briefs (BC-137)** — created `00-meta/image-briefs.md` (style preamble; 66 pass-1 blocks: 18 districts, 10 emblems, 10 territory shots, 23 NPC paper puppets, 5 splat images) and `assets/manifest.md` (66 rows, `not generated`).
- **Meta** — `00-meta/README.md` (folder map, registers, links), `agent-preamble.md` (hard rules cite BC-125/127/128 and validate.py), `style-guide.md` §8–§10, `foundry-mapping.md` §2 and §4.2, `Neon Black Build Plan.md` A.2 / A.4 amended in place; every file left at `status: review`.

## 2026-09-03 — WP5 (merged from `00-meta/additions/WP5.md` by WP6)

- **WP5** — created `09-loadout/` (30 custom `loadout-item` files, `existing-catalog.md`, `README.md`) and populated `08-challenges/` (`generic-reuse-map.md`, 7 files in `custom/`, 3 files in `power-sets/`, `README.md`). Registered BC-27 through BC-30 above. No changes to `08-challenges/custom/secret-war-goes-public.md` (read only, per instructions).

## 2026-09-03 — WP4-trio3 (merged from `00-meta/additions/WP4-trio3.md` by WP6)

Same shape as [[changelog]].


**Created**

- `06-key-players/corp-b/overview.md` — Orison Defense Systems: base concept, the **Pattern Four** twist (invented), agenda, resources including the other corporations' anti-Tao countermeasures as a threat faced, motifs, territory, standing toward all nine other Key Players, what the destabilization means, hooks.
- `06-key-players/corp-b/characters/adaeze-ferreira.md` — VP Product Integrity, of the Wuji; **vector face**.
- `06-key-players/corp-b/characters/reidar-solano.md` — SVP Volume Munitions, not of the Wuji; the employer whose job is a betrayal of his own company.
- `06-key-players/corp-b/challenges/product-integrity-team.md` — pursuer, Scale 1; *Never Opens the Case*, *Buy First*, *Jurisdiction Arranged*, *No Report Was Filed*.
- `06-key-players/corp-b/challenges/reach-armory-seal.md` — barrier, Scale 2; *Reads As Dead*, *Nothing Leaves Open*, *The Shop Does Not Appear*, *Forty-One Faces*, *Drills, Not Alarms*.
- `06-key-players/corp-b/challenges/reuse.md`, `06-key-players/corp-b/membership.md`.
- `06-key-players/tao-society/overview.md` — the Wuji: the **containment** twist (invented), Tao resources (practitioners, Tao-worked items, Tao-made beings used once and unmade, an unwritten curriculum), the anti-Tao countermeasures faced, standing toward all nine others, hooks.
- `06-key-players/tao-society/characters/constance-marchetti.md` — Steward of Aldine House.
- `06-key-players/tao-society/characters/nasrin-vogel.md` — recruiter and talent-spotter; **vector face**.
- `06-key-players/tao-society/challenges/wuji-operative.md` — attacker, Scale 0; *The Condition*, *Worked, Not Willed*, *Buys First, Twice*, *Nothing Is Left Behind*.
- `06-key-players/tao-society/challenges/aldine-house.md` — temptation, Scale 1; *Nobody Is Thrown Out*, *The Offer Is Real*, *Being Seen Here Counts*, *The Morning Practice*, *A Refusal Is Not a No*.
- `06-key-players/tao-society/challenges/reuse.md`, `06-key-players/tao-society/membership.md`.
- `06-key-players/government/overview.md` — the Chancery: the **jurisdiction** twist (invented), the double-sold registry, standing toward all nine others, hooks.
- `06-key-players/government/characters/emeric-vann.md` — Deputy Registrar, bought; **vector face**.
- `06-key-players/government/characters/halima-boyce.md` — Superintendent, Office of Concurrent Jurisdiction; the corporate-security liaison.
- `06-key-players/government/challenges/chancery-process.md` — barrier, Scale 2; *Not On The Net*, *The Price Goes Up*, *Referred Onward*, *Two Copies*, *A Concurrence Is Sold Separately*.
- `06-key-players/government/challenges/envelope-detail.md` — attacker, Scale 1; *Whose Report Is The Record*, *Two Envelopes*, *Cheap and Corrupt, Not Stupid*, *Nothing Happens Under the Wall*.
- `06-key-players/government/challenges/reuse.md`, `06-key-players/government/membership.md` (no custom Self kit; Law Enforcement Core p. 199 and Corporate Citizenship Core p. 198).
- `06-key-players/changeling-cells/overview.md` — the Cutloose: the **queue** twist (invented), the Wall of Faces, standing toward all nine others, hooks.
- `06-key-players/changeling-cells/characters/odile-ferraz.md` — "Six", cell leader; **vector face**.
- `06-key-players/changeling-cells/characters/corin-alvarez.md` — "Tuesday", recent escapee.
- `06-key-players/changeling-cells/challenges/gallery-nine-watch.md` — watcher, Scale 1; *Anything That Transmits*, *The Pumps Are The Clock*, *Never The Same Face*, *Cannot Be Bought*, *Vouched*.
- `06-key-players/changeling-cells/challenges/fresh-cut.md` — target, Scale 0; *The Switch Is Out*, *Not Well*, *Wears What It Needs*, *Waiting To Be Told*, *Worth More Than They Know*.
- `06-key-players/changeling-cells/challenges/six-at-the-hatch.md` — barrier, Scale 0; Odile Ferraz's own profile (slug distinct from the NPC file's).
- `06-key-players/changeling-cells/challenges/reuse.md`, `06-key-players/changeling-cells/membership.md`.
- `00-meta/additions/WP4-trio3.md` — this file.

**Changed:** nothing. No shared register was edited (agent preamble).

**Register rows added:** BC-116 to -9; OQ-30 to -3; CR-19; nineteen name rows.

**Notes for WP6.**

1. **Pending links** used by this package and owed by other packages: `[[corp-a]]`, `[[corp-c]]`, `[[upstart]]`, `[[syndicate]]`, `[[packs]]`, `[[fence-network]]`, `[[marisol-okonkwo]]` (WP4 trios 1–2); `[[orison-citizenship]]`, `[[wuji-initiate]]`, `[[cutloose-cell]]` (WP3); the anti-Tao countermeasure Challenge in `08-challenges/custom/` (WP5); WP2's mage and changeling Power Sets and PC Specials, referenced by path rather than by wikilink so nothing guesses a slug.
2. **Slug collisions.** Four `overview.md` files in this package carry `slug: overview` per `template-key-player.md`, which collides with `05-megacity/overview.md` and with the other Key Player folders; WP1 already flagged this. All links here use the folder role code (`[[corp-b]]`, `[[tao-society]]`, `[[government]]`, `[[changeling-cells]]`) as the district files do. Separately, `challenges/six-at-the-hatch.md` was given a distinct slug so that the NPC file `characters/odile-ferraz.md` and her Challenge do not both answer to `[[odile-ferraz]]`; WP6 may want that as a vault-wide convention for named fighters.
3. **Cross-trio consistency to check.** (a) `corp-a`'s and `corp-c`'s overviews should agree that both corporations run anti-Tao programmes and neither has an explanation (BC-117, OQ-47). (b) `upstart`'s file should not contradict the Chancery selling Continuity advance and retroactive concurrences (BC-122). (c) `syndicate`'s and `fence-network`'s files should agree that the Weighhouse and the Kitchen are where Orison hardware surfaces. (d) Nothing in this package touches OQ-10, OQ-11, OQ-12, OQ-13, or OQ-17, and none of its Consequences can produce an answer to them.
4. **Canon audit trail.** No file here says the public knows Tao exists (OQ-6); no file asserts a Tao-dense place (OQ-14); no file gives Tao a will; every reuse of a Mythos-framed book element is marked `[TAO-REINTERPRETED]`; the Bloodware secret and Continuity's nature are not mentioned anywhere in this package's content, only as a standing they are on the other side of.

## 2026-09-03 — WP4-trio2 (merged from `00-meta/additions/WP4-trio2.md` by WP6)

**2026-09-03 — WP4-trio2 — Key Players: Meliora Bioworks, the Almoners, the Run.**

Created (all `status: review`, `owner: WP4-trio2`):

- `06-key-players/corp-a/overview.md`, `membership.md`, `characters/solenne-marchetti.md`, `characters/ondine-ferreira.md`, `challenges/vice-president-marchetti.md`, `challenges/sterile-field-unit.md`, `challenges/the-sterile-field.md`, `challenges/reuse.md`
- `06-key-players/syndicate/overview.md`, `membership.md`, `characters/bettina-alarcon.md`, `characters/halina-ansah.md`, `challenges/first-alms.md`, `challenges/almoners-volunteer.md`, `challenges/the-round.md`, `challenges/reuse.md`
- `06-key-players/packs/overview.md`, `membership.md`, `characters/teodora-sowande.md`, `characters/jarek-kovac.md`, `challenges/chimney.md`, `challenges/pack-on-the-run.md`, `challenges/uncle.md`, `challenges/kiln-row.md`, `challenges/running-shape.md`, `challenges/reuse.md`
- `00-meta/additions/WP4-trio2.md` (this file)

Changed: nothing. No shared register, template, or WP1 file was edited.

Pending links used (Plan A.3): `[[corp-b]]`, `[[corp-c]]`, `[[upstart]]`, `[[government]]`, `[[tao-society]]`, `[[changeling-cells]]`, `[[fence-network]]` (pending the other WP4 trios); `[[meliora-citizenship]]`, `[[almoners-associate]]`, `[[pack-affiliation]]` (pending WP3); WP2's werewolf Power Set is referenced in prose only, with no link, per OQ-46.

## 2026-09-03 — WP4-trio1 (merged from `00-meta/additions/WP4-trio1.md` by WP6)

**2026-09-03 — WP4 trio 1** (`06-key-players/upstart/`, `corp-c/`, `fence-network/`). All files `status: review`, `owner: WP4-trio1`.

Created:

- `06-key-players/upstart/overview.md` — Continuity Risk & Response (`key-player`; twist Bible-given, held in an MC-only section).
- `06-key-players/upstart/characters/hanne-oyelaran.md` — "Amber," strike lead, vector face.
- `06-key-players/upstart/characters/rosalind-ekwueme.md` — VP Client Continuity, second vector face.
- `06-key-players/upstart/characters/tomas-adair.md` — Rook; canon-only, with the open questions tabled and unanswered.
- `06-key-players/upstart/challenges/continuity-crisis-response-cell.md` — attacker.
- `06-key-players/upstart/challenges/the-cold-suite.md` — barrier (Harnessing floors and monitored Nearspace).
- `06-key-players/upstart/challenges/hanne-oyelaran-challenge.md` — pursuer, Movers and Shakers format.
- `06-key-players/upstart/challenges/tomas-adair-challenge.md` — asset, Movers and Shakers format, canon-bound.
- `06-key-players/upstart/challenges/reuse.md` — core/tokyo reuse with pages.
- `06-key-players/upstart/membership.md`.
- `06-key-players/corp-c/overview.md` — AP&I (`key-player`; twist invented, BC-101).
- `06-key-players/corp-c/characters/vera-solano.md` — "Nought," the Ledger's authority, vector face.
- `06-key-players/corp-c/characters/priya-halstead.md` — SVP Reconciliation & Recovery.
- `06-key-players/corp-c/characters/rasheeda-novak.md` — Recovery Analyst.
- `06-key-players/corp-c/challenges/ledger-line-security.md` — barrier.
- `06-key-players/corp-c/challenges/escapee-recovery-desk.md` — watcher.
- `06-key-players/corp-c/challenges/vera-solano-challenge.md` — watcher, Movers and Shakers format.
- `06-key-players/corp-c/challenges/reuse.md`.
- `06-key-players/corp-c/membership.md`.
- `06-key-players/fence-network/overview.md` — Tally's Weighhouse (`key-player`; twist invented, BC-102).
- `06-key-players/fence-network/characters/marisol-okonkwo.md` — "Tally," vector face, day-one contact.
- `06-key-players/fence-network/characters/dessa-rahimi.md` — "Chit," runner.
- `06-key-players/fence-network/characters/bohdan-adeyemi.md` — "Weights," the water door.
- `06-key-players/fence-network/challenges/the-weighhouse.md` — temptation location.
- `06-key-players/fence-network/challenges/weighhouse-muscle.md` — attacker.
- `06-key-players/fence-network/challenges/marisol-okonkwo-challenge.md` — temptation, Movers and Shakers format.
- `06-key-players/fence-network/challenges/bohdan-adeyemi-challenge.md` — barrier, Movers and Shakers format.
- `06-key-players/fence-network/challenges/reuse.md`.
- `06-key-players/fence-network/membership.md`.
- `00-meta/additions/WP4-trio1.md` — this file.

Changed: nothing outside these folders. No shared register was edited.

## 2026-09-03 — WP3 (merged from `00-meta/additions/WP3.md` by WP6)

**Created**

- `03-self-kits/existing-self-kits.md`
- `03-self-kits/README.md`
- `03-self-kits/meliora-citizenship.md`, `orison-citizenship.md`, `api-citizenship.md`, `continuity-contractor.md`, `almoners-associate.md`, `pack-affiliation.md`, `cutloose-cell.md`, `wuji-initiate.md` (Affiliation)
- `03-self-kits/the-ledger.md`, `caste-sorted.md`, `saw-something-i-shouldnt.md` (Troubled Past)
- `03-self-kits/weighhouse-credit.md` (Assets)
- `03-self-kits/climb-the-wall.md`, `fix-the-city.md`, `take-the-city.md` (Horizon)
- `04-crew/README.md`
- `04-crew/motivations.md`
- `04-crew/crew-kits/existing-crew-kits.md`
- `04-crew/crew-kits/scrape-by-together.md`, `we-take-the-city.md`, `we-owe-rook.md`
- `04-crew/crew-specials/existing-crew-specials.md`
- `04-crew/crew-specials/weighhouse-line.md`, `we-got-out-together.md`, `we-know-the-under.md`, `not-worth-the-bounty.md`
- `00-meta/additions/WP3.md` (this file)

**Register rows added:** BC-97 to BC-100; OQ-36. No new conflict-register rows (see "Conflicts" above for a non-register note to WP0/WP6).

**Notes for WP6.** (1) Every link into `06-key-players/*` (`corp-a`, `corp-b`, `corp-c`, `upstart`, `syndicate`, `tao-society`, `packs`, `fence-network`) and to `marisol-okonkwo`/`tomas-adair` is marked `(pending WP4)` on first use per file, per [[style-guide]] §8 rule 4. (2) `03-self-kits/pack-affiliation.md` and `cutloose-cell.md` are written to be linked from WP2's werewolf and changeling splat packages respectively (Brief §4.4); WP2 should confirm those links exist once its files land. (3) All fifteen custom Self kits and all three custom crew kits validate against Plan A.5 (ten power tags A–J with A as title, four weakness tags A–D, one motivation in category voice, a nascent form).

**Validation:** every frontmatter block parsed with `python3 -c "import yaml..."`; every H1 equals `name`; `status: review` and `owner: WP3` on all files; every inline marker has a matching `flags:` entry; every wikilink resolves within the vault, is marked `(pending WP4)`, or points to a file this same package created.

**Post-draft QC pass:** a forbidden-terms sweep (00-meta/README.md, [[style-guide]] §5) caught the word "splat" surviving in prose across most of `03-self-kits/` and one `04-crew/crew-specials/` file — card headers ("Splat: any") and several sentences ("any splat," "splat-agnostic," "splat package"). All instances in rendered body text were corrected to "any of the five" / "which of the five" / "none of the five," matching the required voice; the YAML `splat: any` frontmatter key itself was left untouched (it's vault-only metadata, not rendered prose) and folder-path references like `` `02-splats/werewolf/` `` were also left as-is (a literal path, not the forbidden word used in prose). A second wikilink-resolution pass, re-run after the wording fixes, also caught and corrected one real defect unrelated to the splat sweep: `04-crew/README.md` linked `[[crew-motivations]]`, but `04-crew/motivations.md`'s actual slug is `crew-motivations` — fixed to `[[crew-motivations|motivations]]` on first mention, plain text on the repeated table row.

## 2026-09-03 — WP2-hunter (merged from `00-meta/additions/WP2-hunter.md` by WP6)

**Created**

- `02-splats/hunter/overview.md` — player-safe canon (the "just human" pitch, three named archetype families plus room for more, a range of in-fiction reasons a Baseline holds the replacement-only line), mapping table, Essence targets Real/Cyborg with what each Essence Special gives a Baseline (Core p. 135), persistence note (only replacement cybernetics persist and only they can be removed), motivation rule, sheet notes, links to every file below, and an MC-only section on the scapegoat role.
- `02-splats/hunter/theme-kits/existing-kits.md` — recommended Self (Expertise, Affiliation, Assets) and Noise (Cutting Edge) book kits with page refs and re-flavor notes; a full Augmentation off-limits/borderline table for all eight printed Augmentation kits.
- `02-splats/hunter/theme-kits/extreme-case-tracker.md` — custom Expertise kit (splat-hunter's trade: reading the other four's tells via EM/chem/face/Tao-sense gear, without naming what any tell actually means).
- `02-splats/hunter/theme-kits/surplus-combat-rig.md` — custom Cutting Edge kit (a decommissioned mil-spec hardsuit/weapon-system).
- `02-splats/hunter/theme-kits/standard-issue-replacement.md` — custom Augmentation kit, every tag strictly replacement-framed, modeled on Tokyo's Cheap Prosthetic pattern.
- `02-splats/hunter/theme-kits/the-unmade.md` — custom Affiliation kit for the anti-cybernetic movement (optional per Brief §2.5, included rather than left pending).
- `02-splats/hunter/tropes/bonded-tracker.md` — custom trope, four Self kits, built toward Real.
- `02-splats/hunter/tropes/corporate-muscle.md` — custom trope, three Self kits plus the Cutting Edge kit, built toward Cyborg.
- `02-splats/hunter/pc-specials/cheap-prosthetic.md` — adapted from Tokyo's Cheap Prosthetic (Tokyo p. 73); the persistent, removable replacement condition.
- `02-splats/hunter/pc-specials/another-baseline-with-a-gun.md` — the public-scapegoat condition.
- `02-splats/hunter/pc-specials/just-human-and-thats-enough.md` — optional Real-only conviction Special.
- `02-splats/hunter/power-sets/corp-bonded-extraction-team.md` — MC-only NPC overlay, corp hunter team.
- `02-splats/hunter/power-sets/unmade-cell.md` — MC-only NPC overlay, radicalized anti-cyber cell.
- `00-meta/additions/WP2-hunter.md` — this file.

**Register rows added:** BC-89 to BC-96 (above); one Names row (the Unmade / Raw). No new conflict-register or open-questions rows.

**Notes for WP6.**
1. `overview` as a bare slug is now shared by `05-megacity/overview.md` (WP1, already flagged by WP1) and `02-splats/hunter/overview.md` (this package) — and will be shared by every future `02-splats/<splat>/overview.md` too. Every file in this package that needs to reference the hunter overview uses the display alias `[[baselines|Baselines]]`, and the megacity overview is referenced by file path rather than wikilink. WP6 should pick a permanent disambiguation (e.g. rename each splat overview file, or adopt a path-aware linking convention).
2. `02-splats/hunter/tropes/*.md` reference several existing book kits (Corporate Citizenship, Guns & More Guns, Trained Killer, Heist Gear, Meticulous Planner, Get Rich & Famous, Survived the Streets, Tough As Nails) by a kebab-case slug in `fixed_kits`/`choice_kits` frontmatter (e.g. `corporate-citizenship`) even though no vault file exists at that slug, since book kits aren't written as individual vault files anywhere in the Plan. This mirrors how `existing-kits.md` cites them by name and page rather than by wikilink. WP6/WP9 should confirm this is an acceptable Foundry-conversion convention (mapping to the system's built-in themekit compendium by name) or specify an alternative.
3. `02-splats/hunter/theme-kits/the-unmade.md` and `power-sets/unmade-cell.md` invent a movement name pending GM approval (BC-94); if the GM changes the name, only those two files and the Names row need updating — no other WP2-hunter file depends on it.

**Validation:** every frontmatter block in this package parsed with `yaml.safe_load`; every H1 equals `name`; `status: review` and `owner: WP2-hunter` on all fourteen files; every inline marker (`[BUILD CHOICE]`) has a matching `flags:` entry and vice versa; every custom theme kit has exactly ten power tags (A–J, A is the title tag) and four weakness tags (A–D); no hunter kit contains a sculpting or bio-manipulation tag; every wikilink resolves to a file created in this package, a file created by WP0/WP1, or is annotated where it references content pending another WP.

## 2026-09-03 — WP2-changeling (merged from `00-meta/additions/WP2-changeling.md` by WP6)

**Created**

- `02-splats/changeling/overview.md` — player-safe canon in setting voice; owned vs. Cutloose as the two ways to play; the "who makes Doppels" `[OPEN]` with a flagged proposal and two alternates; hybrid mapping (required Noise / Augmentation, optional Mythos / Exposure, with the Esoterica constraint); Essence minimum and Transhuman as the natural Essence (Core p. 135); persistence; the kit-fixed Itch; how a Doppel reads on the sheet; rarity; file index; an MC-only section.
- `02-splats/changeling/theme-kits/existing-kits.md` — book kits offered as printed, with pages and re-flavor lines: Impossibly Good Looks (Core p. 239), Hidden Gadgets (p. 239), Escaped Servitude (p. 218), Science Experiment (p. 219), Covert Agent (p. 206), Zeroed Identity (p. 247), Corporate Citizenship and Criminal Syndicate (p. 198), Cloaking Jumpsuit (p. 242), Safehouse (p. 203), Heist Gear (p. 202); the three usable Exposure kits and the four usable Esoterica kits with their Source/Ritual substitutions, and the ones not offered.
- `02-splats/changeling/theme-kits/borrowed-face-owned.md` — Augmentation / Noise; 10 power tags, 4 weakness tags (switch, tracker, slip, handler); Itch *Become someone else.*; the Special *Wear Them Long*.
- `02-splats/changeling/theme-kits/borrowed-face-cutloose.md` — the same ten power tags; weakness set scar / no fitter / slip / *hunted by my makers*; the swap-on-escape rule.
- `02-splats/changeling/theme-kits/held-shape.md` — Exposure / Mythos-OS; the Tao half; Ritual as a condition and a price; `[TAO-REINTERPRETED]` Source model; the Special *Set It Deeper*.
- `02-splats/changeling/theme-kits/deadman-rig.md` — Cutting Edge / Noise; the Cutloose survival kit (shroud, jammer, false ping, the switch-popping pulse, the scar over the socket); gear Itch; the Special *Counted Dead*.
- `02-splats/changeling/tropes/company-face.md` — owned trope; fixed [[borrowed-face-owned]] / [[held-shape]] / Zeroed Identity; built toward Transhuman.
- `02-splats/changeling/tropes/runaway-face.md` — Cutloose trope; fixed [[borrowed-face-cutloose]] / [[deadman-rig]] / Escaped Servitude; built toward Cyborg.
- `02-splats/changeling/pc-specials/switch-and-handler.md` — owned; the leash's resources and their price; the removal clause that turns a PC Cutloose.
- `02-splats/changeling/pc-specials/retrieval-contract.md` — Cutloose; hunted, as a stacking *traced* status.
- `02-splats/changeling/pc-specials/the-cells-will-answer.md` — Cutloose; the escapee network's reach and its ledger.
- `02-splats/changeling/pc-specials/the-face-doesnt-come-off.md` — either; the one you wore too long.
- `02-splats/changeling/power-sets/wearing-your-face.md` — Noise overlay for a Doppel NPC on a job; compared against *Shapechanger* (Core p. 331) and *Holographic* (p. 333).
- `02-splats/changeling/power-sets/owned-asset.md` — Self overlay for an owned Doppel NPC; the *turn-them* Limit, the tracker, and the switch.
- `00-meta/additions/WP2-changeling.md` — this file.

**Register rows added:** 6 name rows, BC-72 to -17, OQ-30 to -6, CR-12 to -3.

**Not created:** nothing outside `02-splats/changeling/` and this register file. No shared register was edited (Agent Preamble).

## 2026-09-03 — WP2-werewolf (merged from `00-meta/additions/WP2-werewolf.md` by WP6)

**2026-09-03 — WP2 Howlers (werewolf splat package)**

Created:

- `02-splats/werewolf/overview.md` — player-safe canon in setting voice; the knows / does-not-know line (BC-45); MC-only supply chain (Meliora → the Almoners → the packs) with OQ-3 left open; Hybrid mapping table; Essence minimum and likely Essences; the persistence rule against CR-7; the kit-fixed Itch rule; sheet notes; links.
- `02-splats/werewolf/theme-kits/existing-kits.md` — **Animalistic Modifications** (Core p. 238) and **Reflex Booster Implants** (Core p. 239) with re-flavor; **Street Gang** (Core p. 199) for the pack; sixteen further book kits across Augmentation, Cutting Edge, Affiliation, Troubled Past, Personality, Assets, Expertise, Horizon; a short "not for Howlers" list.
- `02-splats/werewolf/theme-kits/sculpted-beast.md` — custom kit, Augmentation / Noise, 10 power tags + 4 weakness tags + kit-fixed Itch; weaknesses carry the Leash dependency and the irreversible body; themebook Specials inherited.
- `02-splats/werewolf/theme-kits/a-line-on-leash.md` — custom kit, Cutting Edge / Noise (BC-48), 10 + 4 + Itch; two kit Specials (*Stretch It*, *Who Cut This*); Occult Blueprints excluded (BC-49).
- `02-splats/werewolf/tropes/run-enforcer.md` — three fixed kits, three choice kits, Loadout line, Cyborg.
- `02-splats/werewolf/tropes/off-the-run.md` — the Howler who left the pack and rations Leash; three fixed, three choice, Loadout line, Cyborg.
- `02-splats/werewolf/pc-specials/kept-on-leash.md` — the dependency loop off supply.
- `02-splats/werewolf/pc-specials/the-sculpt-does-not-come-off.md` — what it costs to try to pass.
- `02-splats/werewolf/pc-specials/kennel-bond.md` — the pack bond and its bill.
- `02-splats/werewolf/power-sets/running-on-leash.md` — Noise overlay, the hour the dose is working.
- `02-splats/werewolf/power-sets/pack-tactics.md` — Self overlay, the pack on its own ground without a dose.
- `00-meta/additions/WP2-werewolf.md` — this file.

Register rows added: BC-44 to -9; no new OQ rows; no new CR rows. Names: one table above, all proposals.

Pending links left for other packages: `[[pack-affiliation]]` (WP3), `[[packs]]`, `[[syndicate]]`, `[[corp-a]]` (WP4).

## 2026-09-03 — WP2-vampire (merged from `00-meta/additions/WP2-vampire.md` by WP6)

| Date | Package | Change |
|---|---|---|
| 2026-09-03 | WP2-vampire | Created `02-splats/vampire/`: `overview.md`; `theme-kits/existing-kits.md`, `the-ferrante-strain.md`, `hardened-kernel.md`, `interwoven-strain.md`; `tropes/scrap-fed-newblood.md`, `hundred-year-tenant.md`; `pc-specials/iron-hunger.md`, `field-bitten.md`, `where-the-kernel-sits.md`, `made-by-the-strain.md`; `power-sets/bloodware-power-set.md`; this register file. |

## 2026-09-03 — WP1 Series and Megacity

**Created**

- `01-series/series-concept.md` — crew concept (Bible §6), the sandbox statement, Series pole Paycheck → Misfits with the pivot mechanism (Brief §1.2, Core p. 281), Palisade as the whole world for play.
- `01-series/pillars.md` — Brief §1.3 table restated and ranked; **Tao Weaponized** defined with a book-element → Tao table `[TAO-REINTERPRETED]`.
- `01-series/spine-and-clock.md` — the upstart spine (Bible §5), a what-the-crack-offers prompt table for WP4, the inciting incident, the one confirmed clock and the kinds of event that advance it.
- `01-series/tone.md` — the four registers (Bible §4), influences as texture, palette / lighting / rendering / motif / negative-list words for image briefs, "what this campaign is not."
- `08-challenges/custom/secret-war-goes-public.md` — series-level Countdown Challenge, role countdown, Scale 4, progress Limit `public-war` at tier 6 (BC-5), four Specials, six Threat/Consequence pairs, notch guide 0–6, and the "maxed" statement (the corporate war is public; the splats stay secret).
- `05-megacity/overview.md` — Palisade: the tiered Wall (Crest / Face / Foot / Under) as a `[BUILD CHOICE]`, the Chancery, corporate security as legal as police, the caste system (slang only), the Masquerade as Noise plus cleanup citing Brief §4.1 (CR-4), the Big Three and Continuity, cyberspace as written with the OQ-15 hook.
- `05-megacity/district-directory.md` — the Megacity Generator run: 12-row directory, 18-row expansion with zone codes / tropes / concepts / story tags / caste bands, all 36 rolls (seed 20260903) with dispositions, chosen developments, the mandatory-placement map, Key Players by district.
- `05-megacity/districts/` — eighteen district files: `aurelian-crest`, `chancery-hill`, `meliora-terraces`, `orison-reach` (Crest); `amalgam-stack`, `the-lattice`, `corbel-gallery`, `halloran-circus` (Face); `suture-row`, `gullet-market`, `marlow-blocks`, `cinder-yards`, `relay-fields` (Foot); `kilbride-stretch`, `lowmere-sinks`, `foundation-galleries`, `ferrante-basin`, `coldwater-outfall` (Under). Each: central concept, developments (≥1; Mythoi results reinterpreted and marked), story tag, caste band, Key Players present, 3 scene locations, 3 hooks, canon and flags.
- `05-megacity/timeline.md` — relative future history (no absolute years), every line citing the Bible or marked BC-25; a ten-line summary.

**Changed**

- `00-meta/names.md` — "Added by WP1" table (BC-26): the four tiers, the Chancery, eighteen districts, Aldine House, the Weighhouse, the Marlow Relief Kitchen, Gallery Nine, and the major scene locations, each with alternates and a "reads as" line.
- `00-meta/build-choices.md` — BC-11 to BC-26 added.
- `00-meta/open-questions.md` — OQ-20 (age of Leash and the Run), OQ-21 (whether tier movement is controlled), and WP1 notes on OQ-6, 7, 14, 15, 18.
- `00-meta/changelog.md` — this entry.

**Register rows added:** BC-11 (`type: series` and index-file schema), BC-12 (Tao Weaponized specifics), BC-13 (Countdown specification), BC-14 (image palette words), BC-15 (tiered geography), BC-16 (the Chancery), BC-17 (Generator run), BC-18 (placement map; `fence-network/` folder), BC-19 (Aldine House), BC-20 (the Weighhouse), BC-21 (the Kitchen), BC-22 (Gallery Nine), BC-23 (Ferrante outbreak public / product secret), BC-24 (the Ledger's cover), BC-25 (relative dates), BC-26 (district and place names); OQ-20, OQ-21. No new conflict-register rows.

**Notes for WP6.** (1) `05-megacity/overview.md` has slug `overview`, which will collide with `06-key-players/*/overview.md` and `07-jobs/*/overview.md` for bare `[[palisade]]` links; WP1 links to it as `[[palisade|Palisade]]` and WP6 may want to rename the file or adopt a path convention. (2) The fence's network is given a tenth Key Player folder `fence-network/` (BC-18) pending WP4; links to `[[fence-network]]`, `[[marisol-okonkwo]]`, `[[tomas-adair]]`, the nine `kp_role` slugs, and `[[existing-crew-kits]]` are pending WP3/WP4. (3) The Wuji's control of Orison and Continuity's nature appear only in MC-only "Canon and flags" sections and are visible in no district's content.

**Validation:** every frontmatter block parsed with `yaml.safe_load`; every H1 equals `name`; `status: review` and `owner: WP1` on all files; every inline marker has a matching `flags:` entry and vice versa; every wikilink resolves or is in the pending list above; every district story tag is 2–5 words.

## 2026-09-03 — WP0 Foundation

**Created**

- `00-meta/README.md` — vault index, folder map, reading orders, player-safe vs MC-only note.
- `00-meta/style-guide.md` — naming register derived from the books' Key Players, tag voice, motivation voice, tone words, forbidden terms, marker conventions, wikilink and slug conventions.
- `00-meta/names.md` — proposals (primary + alternates, each with "reads as" and reasoning) for the city, the five splats, Corps A/B/C, the upstart, the syndicate, the Tao society (internal and rumor names), the escaped-changeling network, the pack culture, the trigger's street name, the work camp, the fence, the crew leader, the defunct nanite corporation, the master node's street name; the Corp A/B/C specialty proposal (BC-8); the caste-slang proposal (BC-9); the "Tao stays" note (BC-6).
- `00-meta/conflict-register.md` — CR-1 to CR-8 seeded verbatim from Brief §10 with resolution adopted, landing files, and status; empty "Added during build" section.
- `00-meta/build-choices.md` — BC-1 to BC-5 seeded verbatim from Brief §11 (interviewer's choices); BC-6 to BC-10 added by WP0; empty "Added during build" section.
- `00-meta/open-questions.md` — OQ-1 to OQ-16 seeded from Brief §12, OQ-17 to OQ-19 from Bible `[OPEN]` items the Brief did not restate, each with owner and landing file; empty "Added during build" section.
- `00-meta/foundry-mapping.md` — Plan A.4 schemas and Part D notes restated and cross-checked against `ref/city-of-mist/`; differences from the Plan marked; emission shapes; module skeleton and Sqyre install path; fifteen verification items for WP9.
- `00-meta/changelog.md` — this file.
- `99-templates/template-theme-kit.md`
- `99-templates/template-character-trope.md`
- `99-templates/template-pc-special.md`
- `99-templates/template-crew-special.md`
- `99-templates/template-crew-kit.md`
- `99-templates/template-district.md`
- `99-templates/template-key-player.md`
- `99-templates/template-npc.md`
- `99-templates/template-challenge.md`
- `99-templates/template-power-set.md`
- `99-templates/template-job.md`
- `99-templates/template-scene.md`
- `99-templates/template-loadout-item.md`

**Register rows added:** BC-6 (Tao stays), BC-7 (stable slugs), BC-8 (specialties A=bio, B=weapons, C=cybernetics), BC-9 (caste slang), BC-10 (`type: meta`, `template: true`); OQ-17, OQ-18, OQ-19 (Bible items not in Brief §12).

**Validation:** every frontmatter block parsed with `yaml.safe_load`; every H1 equals `name`; `status: review` and `owner: WP0` on all files.


## 2026-09-03 — GM review of WP0

- `names.md`: city → **Palisade** (alts Halcyon, Harrowgate); Corp B → **Orison Defense Systems** (alts Stillwater Armaments, Kestrel Ballistics); Tao-society alternates replaced (the Hollow Way / the Hush). All other primaries adopted; file status → approved.
- `build-choices.md`: BC-8 and BC-9 approved.

## 2026-09-03 — Orchestrator fix after WP1
- Renamed the Wuji front **Meridian House → Aldine House** everywhere (the GM struck "Meridian" as borrowed from another campaign). Alternates in names.md unchanged.


## 2026-09-03 — WP9 Foundry conversion dry run

- `tools/foundry/convert.py` and `check.py` emit five `_source` packs (35 themekits, 48 threats, 14 template threats, 30 loadout tags, 186 JournalEntries) and `build/module.json`; `check.py` 0/0; `build/` git-ignored.
- `00-meta/foundry-mapping.md` updated with the resolved verification items (Mythos vs Mythos-OS mapped at emit time; alias → prototypeToken.name; fade_type unread; Consequence markup rules).
- Register rows merged from `additions/WP9.md` and renumbered: BC-181, BC-182, BC-183, BC-184, BC-185, BC-186, BC-187, BC-188, BC-189, BC-190, BC-191, BC-192, BC-193, OQ-57, OQ-58, OQ-59, OQ-60, OQ-61, CR-20, CR-21, CR-22.


## 2026-09-04 — WP-I image integration

- 88 images generated (Gemini) and placed under `assets/`; `assets/manifest.md` filled by the image agent.
- 29 NPC puppets keyed from chroma green to alpha with `tools/keyout.py` (BC-194); originals in `assets/npcs-raw/`.
- Every image embedded as `![[assets/...]]` directly under the H1 of its target file (88 files touched); `tools/validate.py` now ignores embeds in the vocabulary sweep.
- `tools/foundry/convert.py`: assets shipped to `build/assets/`, `img`/token texture from embeds, NPC Challenges borrow puppets (BC-195); `check.py` 0/0; validate 0/0.
- Manifest note: `assets/splats/baselines.png` contains readable signage.
