---
type: meta
name: Integration Pass 2
slug: integration-2
status: review
source: custom
page: ""
owner: WP8
canon_refs: ["Plan Part B WP8", "Plan Part C", "Plan A.2–A.4", "Plan Part F WP-I", "Brief §7"]
flags: []
player_safe: false
---

# Integration Pass 2

WP8's report: what changed, why, the counts, and the short list of decisions that are the GM's before session one. Run on 2026-09-03 over the whole vault after WP7a–c. Verification is `python3 tools/validate.py` (Plan Part C, extended by BC-175); its final line at the end of this pass is in §7. Everything decided here is registered as **BC-171 to BC-180**, **OQ-55 and OQ-56**; nothing adds a setting fact.

## 1. The Job 1 → Job 2 handoff (BC-171)

WP7b and WP7c were written in parallel from the same brief and named the same records store twice. Job 1 ended at *the Second Shelf* — a bonded store leased by three law firms in a converted bank behind the Hill; Job 2 broke into the *Chancery Records Repository, Kilbride* — *the paper barn*, a leased bay in a distribution warehouse in the sprawl under a digitization contract, with a scanning crew, a collection-run countdown and a rival crew watching the apron. The heist is built on the warehouse; the Hill version lived in one scene, one clue-chain row and one quotation. **The paper barn stands; the Second Shelf is an alternate name only.**

| Reconciled | Files rewritten |
|---|---|
| The place Job 1's last scene names is the building Job 2's heist enters; Job 1 hands over a building, Job 2 opens by buying the lease, the bay, the date and the volume | [[investigation-09-what-the-book-cannot-say]] (the lead rewritten), [[investigation]] (row 9, third complication, canon), [[investigation-vectors]] §3 and §7, [[investigation-aftermath]] (cash table, "if the run cleared", the handoff quotation), [[the-counting-room]] *The Log Is A Page*; [[acquisition]] (hooks), [[acquisition-01-a-job-at-the-counter]], [[acquisition-02-the-lower-gate]] (the crew already know the building) |
| One supply line: the nine second copies Vann sold in Job 1 came up a chain from Boakye's lifted pages, two removes below him; nobody in the chain has met anyone two steps away | [[emeric-vann]] (his file said he did not know where the other list was; he now sells the building and has never been inside it), [[investigation-06-the-lower-gate]], [[investigation-vectors]] §3, [[acquisition-vectors]] §2 and §5, [[ileana-boakye]] |
| Vector faces agree: Vann (above); Boyce — Job 2's hire is what she did with the second-copy page Job 1 may have put on her desk; Novak — rival buyer in Job 1, the Contracts Office's arithmetic in Job 2, never initiates in either; the Continuity cell at Job 1's climax vs. Ekwueme's monitors in Job 2 — Job 2 no longer says Continuity "does not know the crew exist"; it knows them as, at most, a line in a cleanup report | [[acquisition-vectors]] §1 and §8, [[acquisition-aftermath]] (Key Player table; the Misfits-against-Continuity branch) |
| Two countdowns with one display name: WP7b's *The Collection Run* (the Factor's consignment) renamed **The Consignment Window**, `the-collection-run.md` → `the-consignment-window.md` (`git mv`), every link and slug list rewritten; WP7c's [[collection-run]] (the Repository's van) keeps its name | [[the-consignment-window]], twelve Job 1 files, [[jobs-index]], the registers |
| OQ-37 stays open at the canon level: WP7c's answer (the standing account is Continuity's) is BC-164, a registered proposal the GM may overrule without changing a line; every scene names a number, never a name — confirmed by reading all nine | no change; [[acquisition]], [[acquisition-07-the-coldwater-run]], [[acquisition-09-what-a-page-is-worth]] |

**The clock (BC-172).** The three aftermaths' notch tables were consistent with [[secret-war-goes-public]] but silent about stacking, and one Job 2 row gave a fight between two freelance crews `public-war-1`, which a Baseline could have done. Corrected, and the arithmetic tabled once in [[spine-and-clock]]: Job 0 adds 0; Job 1 adds 0–4; Job 2 adds 0–4; rows stack; *Cleanup Crews* may remove one tier between jobs; a table that plays every job loud can reach `public-war-6` at the end of Job 2. Whether the GM wants a per-job cap is **OQ-56**.

## 2. Job-folder conventions (BC-173, BC-174)

- Companions normalized to WP7a's convention across all three jobs: `-vectors`, `-aftermath`, `-roster` are `type: index` with `job:` and `companion:`; WP7b's and WP7c's companions were `type: job` with the job schema repeated. validate.py now counts `job=3`. Stated in [[jobs-index]] and Plan A.4.
- **Job-only NPCs live in `07-jobs/<job>/characters/<slug>.md`** as `npc` files (`player_safe: false`). Six created: [[wax]], [[anselm-boateng]] (`challenge: the-factor`), [[ivo-meszaros]]; [[margit-nakagawa]], [[ileana-boakye]], [[ilya-sarpong]] (`challenge: the-carters`). The vectors files keep want and push; the six are now wikilinked wherever they were bold text, counted (`npc=29`), and briefed for paper puppets. Plan A.2 amended.
- validate.py's pending list is empty (BC-175).

## 3. The whole-vault checks (Plan Part C)

| Check | Result |
|---|---|
| C.1 canon | No new setting fact in WP7 beyond the registered build choices; WP7's inventions all extend BC-101, BC-102, BC-122 or Bible §5–6. The one story edit in this pass (BC-171) chooses between two packages' versions of one place. |
| C.2 cosmology | Clean; no new `[TAO-REINTERPRETED]` needed — the jobs carry no Tao content beyond the Caster hard-choice hooks, which cite existing kits. |
| C.3 splat canon | Clean: the only one of the five in Job 0's roster is Rook (EM and the Kernel, nothing else); Job 1's second body is an EM kill and is never explained; the Baseline hooks offer an enhancement splice and never reward taking it. |
| C.4 kits | 35 kits, 10/4 tags, A is a title tag, motivation type matches category — unchanged from WP6. |
| C.5 Challenges | 48; every one has a role, ≥1 Limit at tier 2–6 (or immune), Scale, and Consequences on every Threat; the three job countdowns are job-level and never feed the series clock. |
| C.6 vocabulary | **Zero warnings.** The three lingering *case* warnings were resolved by rewording ([[baselines]] *casework*, [[extreme-case-tracker]] *a file*, [[bonded-tracker]] *investigations*); the ruling is that Plan C.6 forbids the word in prose and police work is not one of BC-136's exceptions. The kit name *Extreme-Case Tracker* is a GM-adopted primary and stands. |
| C.7 links | Zero unresolved; the pending register is empty. |
| C.8 player packet | New check: a `player_safe: true` file may link only to `player_safe: true` files. 159 violations found across 67 files and fixed (§4). |
| OQ-50 | Ruled: the three shared surnames are unrelated people unless the GM decides otherwise — a one-line note in [[names]]; no rename; the question stays open. |

## 4. The session-zero packet (BC-175 to BC-178)

- **The five overviews were split (BC-176):** each `## MC only` section moved verbatim into `<splat>-mc-notes.md` (`splat-overview`, `player_safe: false`), and the overview became `player_safe: true` with a one-line pointer.
- **[[palisade-player-primer]] (BC-177):** [[palisade]] is not player-safe (it places the camp, Continuity's ground and the Masquerade's machinery), so a primer of what any resident knows was written — tiers, caste slang, the eighteen districts by public face, the Big Three, Continuity and the Chancery as brands, the Kitchen and the Almoners, the Run, the Quiet Hand as a rumor, and the five things the crew know that the city does not. Every player-safe file that linked a district or a public Key Player now links the primer's section for it; registers, MC-only overlays and the Series files are cited in code spans; secret groups became plain text (`tools/wp8_pslinks.py`, 67 files, mechanical).
- **Loadout audit:** seven items are `player_safe: true` — [[ledger-issue-fatigues]], [[reclamation-worksheds-toolkit]], [[guard-baton-and-fob]], [[weighhouse-line-of-credit]], [[weighhouse-runner-favor]], [[weighhouse-pawned-piece]], [[weighhouse-salvage-crate]]. Leash cuts, kill-switch and anti-Bloodware gear, corp internal kit and Tao-touched items stay MC-only.
- **[[session-zero-packet]]** links every `player_safe: true` file in the vault — **91 files** — and nothing else: the primer; five overviews, 17 custom theme kits, five existing-kits lists, 10 tropes, 17 PC Specials and [[book-kits-index]]; 15 Self kits with [[self-kits-index]] and [[existing-self-kits]]; [[crew-index]], 3 crew kits and [[existing-crew-kits]], [[crew-motivations]], 4 Crew Theme Specials and [[existing-crew-specials]]; 7 loadout items. validate.py confirms no MC-only file is reachable from it.

## 5. What the GM must decide before session one

Short, in order of when a table will hit it:

1. **OQ-39 — which ending Rook gets** at [[breakout-05-a-name-and-a-place]] (into the van, or not on the road). Both are written; Job 1 inherits the answer.
2. **BC-140 — the Ledger's product** (reclaimed metal, strikeable). Session one's shed scenes read either way.
3. **OQ-56 — a per-job cap on the public-war clock**, before Job 1's climax can add up to four tiers.
4. **BC-164 — whose the standing account is** (Continuity's, proposed). Nothing in Job 2 changes if refused; the Misfits branch the table lands on does.
5. **OQ-49 — how much of a person a dosed Howler remains**, before the Run's Challenges are voiced.
6. **CR-16 — AP&I's mandatory augmentation vs. Baseline canon** (band-grade employment adopted provisionally), before any Baseline works the Stack.
7. **The names under "Added by WP7a–c" in [[names]]** — proposals, like every name since WP1; the six job NPCs and the paper barn are the ones a table will say aloud.

Everything else in the status boards is *open* by design and is answered in play or not at all.

## 6. Counts after the pass

| Type | Files | | Type | Files |
|---|---|---|---|---|
| theme-kit | 32 | | district (`districts/`) | 18 (+4 `district`-schema pages: [[palisade]], [[palisade-player-primer]], [[district-directory]], [[timeline]]) |
| crew-kit | 3 | | key-player | 10 |
| character-trope | 10 | | npc | 29 (23 + 6 job-only) |
| pc-special | 17 | | challenge | 48 (38 + 10 from the jobs) |
| crew-special | 4 | | power-set | 14 |
| loadout-item | 30 (7 player-safe) | | membership | 10 |
| series | 4 | | splat-overview | 10 (5 overviews + 5 MC-notes) |
| job | 3 | | scene | 25 |
| index | 42 (nine MOCs, six job companions, three rosters, the kit lists and reuse lists, [[book-kits-index]], [[manifest]]) | | meta | 14 |

327 content files + 13 templates = 340 validated files; 19 new (six job NPCs, five MC-notes, four MOCs, the primer, the packet, the reading order, this file), 1 renamed, 13 removed (`00-meta/additions/WP*.md`, merged), 138 modified (plus four tools). Registers: 180 BC rows, 56 OQ rows, 19 CR rows (WP6 counted 21 by a different rule; ids run CR-1 to CR-19). Player-safe files: 91. Image briefs: 66 + 22 = 88. Tools added: `tools/wp8_idmap.json`, `wp8_pslinks.py`, `wp8_moc.py`, `wp8_moc_build.py`.

## 7. Final validation

`python3 tools/validate.py` → **ERRORS: 0 · WARNINGS: 0** over 340 files (327 content + 13 templates). Every file that passes carries `status: review`; [[names]] and [[agent-preamble]] keep `approved`.
