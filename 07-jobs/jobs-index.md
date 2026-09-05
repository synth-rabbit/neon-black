---
type: index
name: "Jobs Index"
slug: jobs-index
status: review
source: custom
page: "281, 284–293"
owner: WP7a
canon_refs: ["Bible §5", "Bible §6", "Brief §1.2", "Brief §7", "Core p. 281", "Core p. 284–293"]
flags: [BUILD CHOICE]
player_safe: false
---

# Jobs Index

The three jobs of the Neon Black pilot, in play order. The Series starts Paycheck and pivots to Misfits (Brief §1.2; [[series-concept]]); Job 0 is the thing that happened to the crew, Jobs 1 and 2 are the work Tally finds them, and Job 2 carries the twist that lets the table pivot. Job 1 hands to Job 2 through one building — the paper barn in [[kilbride-stretch]] — and one unnamed standing-account number (WP8 reconciliation, BC-171); the three aftermaths' effect on [[secret-war-goes-public]] is tabled in [[spine-and-clock]] (BC-172).

| # | Folder | Job | Type | Sessions | Pole | Pivot twist | Written by |
|---|---|---|---|---|---|---|---|
| 0 | `07-jobs/00-breakout/` | [[breakout]] — *Job 0: The Breakout*, the session-one escape from Reconciliation Facility 4 | extraction (subverted: the crew are the escapees) | 1 | paycheck (the job before the first paycheck) | no | WP7a |
| 1 | `07-jobs/01-investigation/` | [[investigation]] — *A Full Set of Names*: a missing runner, a bundle of the Book's pages, and a record of Palisade that disagrees with itself | investigation | 2–3 | paycheck | no | WP7b |
| 2 | `07-jobs/02-acquisition/` | [[acquisition]] — *The Second Copy*: a heist for one buckram volume out of the paper barn before it is pulped, and the two pages in it that carry the pivot | acquisition (heist) | 3 | paycheck → pivot | **yes** | WP7c |

## Job 0 files

- [[breakout]] — the job: hooks (none), goal, structure, vectors, core moments, the Flashback design, the Ledger's product (proposed), complications, ties.
- [[breakout-vectors]] — want / push / face for the strike lead, the camp authority, the crew leader (canon-bounded), and the security system as time running out.
- Scenes: [[breakout-01-lights-out]] · [[breakout-02-hand-under-the-elbow]] (core moment) · [[breakout-03-the-wire]] · [[breakout-04-the-causeway]] (climax) · [[breakout-05-a-name-and-a-place]] (core moment) · [[breakout-06-the-long-walk]] · [[breakout-07-the-counter-door]] (denouement; crew theme).
- Challenges: [[the-strike-hour]] · [[landing-stage-post]] · [[the-sludge-flats]] · [[breakout-roster]] (every reused Challenge by slug and role).
- [[breakout-aftermath]] — escapee-list status, what each Key Player learns, the public-war notch (0), denouement questions, Credit Roll, handoff.

## Job 1 files

- [[investigation]] — the job: two hooks, the goal, the nine-row clue chain with its two "goes deeper" points, core moments, set pieces, five per-splat hard choices, complications.
- [[investigation-vectors]] — Tally (employer), the Factor, Vann, Boyce, Novak (rival buyer, not the buyer), a Continuity cell with no face, and the consignment window as time running out.
- Scenes: [[investigation-01-the-counter-door]] · [[investigation-02-the-labyrinth-route]] · [[investigation-03-the-cold-room]] · [[investigation-04-the-mirror-rig]] (core moment) · [[investigation-05-the-back-room-at-lumen]] · [[investigation-06-the-lower-gate]] (core moment) · [[investigation-07-the-counting-room]] · [[investigation-08-the-cordon]] (climax) · [[investigation-09-what-the-book-cannot-say]] (the lead into Job 2).
- Challenges: [[the-factor]] · [[a-tag-still-answering]] · [[the-counting-room]] · [[the-consignment-window]] · [[investigation-roster]].
- Characters (job-only, BC-174): [[wax]] · [[anselm-boateng]] · [[ivo-meszaros]].
- [[investigation-aftermath]] — rewards, "if the run cleared", what each Key Player learns, the notch table (0–4), denouement questions, Credit Roll, the handoff to Job 2.

## Job 2 files

- [[acquisition]] — the job: four hooks, the goal, the heist beats with one complication each, Prep Sequence and Loading Up, five per-splat hard choices, the twist that carries the pivot, and the proposal for whose the number is (BC-164, overrulable).
- [[acquisition-vectors]] — Boyce through Nakagawa (employer), the Chancery through Vann, the Carters through Barrow, the collection run, Boakye (insider), Tally, Novak, Ekwueme (monitor); who backstabs whom.
- Scenes: [[acquisition-01-a-job-at-the-counter]] · [[acquisition-02-the-lower-gate]] · [[acquisition-03-the-scan-index]] · [[acquisition-04-thirtieth-deck]] · [[acquisition-05-the-prep-sequence]] · [[acquisition-06-the-paper-barn]] · [[acquisition-07-the-coldwater-run]] (core moment) · [[acquisition-08-collection-night]] (climax, core moment) · [[acquisition-09-what-a-page-is-worth]] (the pivot).
- Challenges: [[counterpart-stacks]] · [[the-carters]] · [[collection-run]] · [[acquisition-roster]].
- Characters (job-only, BC-174): [[margit-nakagawa]] · [[ileana-boakye]] · [[ilya-sarpong]].
- [[acquisition-aftermath]] — rewards, what each Key Player learns, the notch table (0–4), denouement questions, Credit Roll, and the pivot statement (stay Paycheck, or Misfits against Continuity, AP&I, or the Chancery).

## Conventions shared by the three folders

**[BUILD CHOICE]** (BC-150, BC-173, BC-174) — stated here and in Plan A.2 / A.4:

- File names per BC-125: `<job-slug>.md`, `<job-slug>-vectors.md`, `<job-slug>-aftermath.md`, `scenes/<job-slug>-<nn>-<slug>.md`, `challenges/<job-slug>-roster.md`, `characters/<given-surname>.md`.
- Companions (`-vectors`, `-aftermath`, `-roster`) carry `type: index` with `job: <slug>` and `companion: vectors|aftermath|roster`; a vectors companion carries `vectors: [slugs]`; an aftermath carries `advances_public_war:` (an integer, or a range pointing at its notch table). They convert as pages inside the Job's JournalEntry, never as Jobs.
- Job-only NPCs — people who belong to no Key Player folder — are `npc` files in the job's `characters/` folder (`player_safe: false`), linkable, counted, and briefed for images like any other NPC; the vectors file keeps their want and push.
- Every scene lists its district story tag, its Challenges by slug (book Challenges in `book_challenges:` by name and page), and its active vectors (Plan WP7 acceptance).
- The crew leader's motives stay unrevealed beyond canon in every job ([[tomas-adair]]; OQ-10). The buyer of provenance in bulk stays a number in every scene (OQ-37); WP7c's answer is a registered proposal (BC-164).
- Each aftermath states whether it advances [[secret-war-goes-public]] and by how much; rows stack; the running sum is in [[spine-and-clock]].

## Every file in this folder

One row per file (this index excepted); *P* marks a `player_safe: true` file that may be handed to a player whole. Descriptions are drawn from each file's frontmatter.

### `07-jobs/00-breakout/`

| File | Type | P | One line |
|---|---|---|---|
| [[breakout-aftermath]] | index | — | The denouement and aftermath of breakout (Core p. 292: "a moment of reflection on what just happened," and "some great big consequences that will need to be summed up"). |
| [[breakout-vectors]] | index | — | The forces in breakout, each with a want, a push, and a face (Core p. 290). |
| [[breakout]] | job | — | extraction, breakout; 1 session(s); pole paycheck; pivot twist False — Get out of Reconciliation Facility 4 alive while Continuity's strike is still the loudest thing in the Outfall, and reach the one name the crew is given — Tally, at the Weighhouse — before the Ledger's count catches up with them. |

### `07-jobs/00-breakout/challenges/`

| File | Type | P | One line |
|---|---|---|---|
| [[breakout-roster]] | index | — | Every Challenge breakout uses, by slug, with the role it plays in this job and the scenes it appears in. |
| [[landing-stage-post]] | challenge | — | attacker, Scale 1 — The guard post on the Ledger's barge landing stage: two AP&I contractors on a hardship rate, a rifle and a shotgun, a stun baton and a gate fob, a chain on a skiff — and the shortest line from the shed row to the water. |
| [[the-sludge-flats]] | challenge | — | barrier, Scale 2 — The Outfall's settling lagoons and sludge-flats, crossed at night: a crust that holds until it does not, a haze that hides the crew from the drone and the drone from the crew, culvert mouths the size of tunnels, and a tide coming in. Nobody walks out of the Ledger unaided. |
| [[the-strike-hour]] | challenge | — | countdown, Scale 2 — The hour between Continuity cutting the Ledger's mains and AP&I's generators coming up: everything the camp relies on fails at once except the causeway gate, a hundred people run, and the crew are part of what the strike is spending. |

### `07-jobs/00-breakout/scenes/`

| File | Type | P | One line |
|---|---|---|---|
| [[breakout-01-lights-out]] | scene | — | 1 · coldwater-outfall · The night count, half-read, on Block Three's yard speakers — and then no speakers, no floodlights, no readers, the block doors hanging open, and grey soft-shell coming through the wire at a walk. |
| [[breakout-02-hand-under-the-elbow]] | scene | — | 2 · coldwater-outfall · core moment · The yard between Block Three and the shed row, black except for torches and the far causeway light; a hundred people running one way; six people in grey walking the other, straight to Rook. |
| [[breakout-03-the-wire]] | scene | — | 3 · coldwater-outfall · The shed row and the fence line behind it, three ways through — the gap the cell cut and is holding, the landing-stage post by the water, and the fifth block's unfinished fence — with a diesel turning over somewhere behind the sheds. |
| [[breakout-04-the-causeway]] | scene | — | 4 · coldwater-outfall · The causeway gate, down, with a truck held on the far side and its engine running; a hundred people against it; and beyond it three kilometers of raised road with no cover — floodlit at the camp end, dark after, and the dark is where the Under begins. |
| [[breakout-05-a-name-and-a-place]] | scene | — | 5 · coldwater-outfall · core moment · The coast-road turn at the causeway's dark end: a grey van across the road with its side door already open, the cell loading, Rook standing beside it — and the last thing he says to the crew. |
| [[breakout-06-the-long-walk]] | scene | — | 6 · lowmere-sinks · Four in the morning on the coast road into the Sinks — stilt-walks locked at every landing, the pumps running late, the Wall a grey line with a gold top on the horizon — and a joint post where the road enters the Gullet's shore end, asking five people in camp fatigues for papers. |
| [[breakout-07-the-counter-door]] | scene | — | 7 · gullet-market · The second hour of the morning on the Gullet quay: a stone box with a water door and a counter door, a brass balance under the roof, a very large man in the water door, a chalk figure already on the Slate with five names beside it, and food on the back-room table before anyone has asked. |

### `07-jobs/01-investigation/challenges/`

| File | Type | P | One line |
|---|---|---|---|
| [[a-tag-still-answering]] | challenge | — | mystery, Scale 0 — An AP&I warranty tag left deliberately live in a body whose chrome has been cut out of it, so that a ledger somewhere would go on reading 'in good standing'. |
| [[investigation-roster]] | index | — | Every Challenge investigation fields, by slug, with its role and what it does in this Job. |
| [[the-consignment-window]] | challenge | — | countdown, Scale 3 — The Job's time-pressure vector: an assembled consignment, a booked haulier, and a delivery window nobody in the Job chose. It has a want and a push and no face. |
| [[the-counting-room]] | challenge | — | barrier, Scale 2 — A converted automat unit in the Stretch fitted out as a bonded store: one door that logs, a weigh-in desk, honest scales, and four hundred bundles of other people's history on numbered shelves. |
| [[the-factor]] | challenge | — | target, Scale 0 — Anselm Boateng: a man in a good coat who buys other people's paper with other people's money, has never been in a room when it went badly, and genuinely does not know who he works for. |

### `07-jobs/01-investigation/characters/`

| File | Type | P | One line |
|---|---|---|---|
| [[anselm-boateng]] | npc | — | "the Factor" — The consolidator who has been buying provenance out of the Book on commission for a principal he cannot name; the confrontation of Job 1 and its deliberate dead end. |
| [[ivo-meszaros]] | npc | — | The surgeon at Threadneedle on Suture Row; reads what was taken out of Wax, will not price the second body, and becomes a contact the crew can keep. |
| [[wax]] | npc | — | "Wax" — The Weighhouse runner whose disappearance opens Job 1; found dead in a Suture Row cold room with her chrome stripped and her warranty tag left live. |

### `07-jobs/01-investigation/`

| File | Type | P | One line |
|---|---|---|---|
| [[investigation-aftermath]] | index | — | The denouement and fallout of investigation (Core p. 292–293). |
| [[investigation-vectors]] | index | — | Every major force in investigation, with a want (what it is trying to achieve in this Job), a push (what it is able and willing to spend), and a face — because vectors always have a face (Core p. 290). |
| [[investigation]] | job | — | investigation; 3 session(s); pole paycheck; pivot twist False — Find out who took the runner and what the pages were for, and put a name to the buyer who has been purchasing provenance in bulk out of the Book for eighteen months. |

### `07-jobs/01-investigation/scenes/`

| File | Type | P | One line |
|---|---|---|---|
| [[investigation-01-the-counter-door]] | scene | — | 1 · gullet-market · The Weighhouse at the second hour of the morning: the brass balance under the roof, the Slate by the counter door with the crew's figure on it, a coaster unloading on the water side, and a bundle of paper that never crossed the balance. |
| [[investigation-02-the-labyrinth-route]] | scene | — | 2 · gullet-market · A kilometre of stalls under corrugated plastic and pirate cabling, the roof-space above it, and three stops on a dead runner's round — the third of which she never reached. |
| [[investigation-03-the-cold-room]] | scene | — | 3 · suture-row · Three surgical bays behind a hand-painted sign, floodwater in the corridor, and a chest freezer that is also a morgue — with a warranty tag inside it, still answering, on a body it is no longer attached to. |
| [[investigation-04-the-mirror-rig]] | scene | — | 4 · relay-fields · core moment · Ten storeys of two-metre capsules under a dead relay mast, every door locked from the inside — and in one of them a rig holding a bad, partial mirror of twenty years of the Foot's property, with somebody else's search still cached on it. |
| [[investigation-05-the-back-room-at-lumen]] | scene | — | 5 · corbel-gallery · An implant bar on the fourth deck of the Corbel arcade — white leather, blue light, a drink and a subdermal — and behind it a room that does uncatalogued work for people who do not want a record, where an AP&I contracts clerk is being paid in exactly that. |
| [[investigation-06-the-lower-gate]] | scene | — | 6 · chancery-hill · core moment · The lower gate where the Hill's road meets the Crest ring road: a police checkpoint, a row of permit-assistance kiosks that are forgers, and a café where the clerks take their envelopes over coffee — with a page on the table, and then a second one. |
| [[investigation-07-the-counting-room]] | scene | — | 7 · kilbride-stretch · A converted automat unit in the Stretch behind a bonded door: a weigh-in desk, a lamp, four hundred bundles on numbered shelves, and a man in a good coat who has never once been in a room when it went badly. |
| [[investigation-08-the-cordon]] | scene | — | 8 · kilbride-stretch · core moment · A grey van with the side door already open stops where nothing was parked a minute ago; tape goes across a prefab street; and a second set of headlights arrives that should not be there, holding a different piece of paper. |
| [[investigation-09-what-the-book-cannot-say]] | scene | — | 9 · gullet-market · Back at the counter door before dawn with a stolen ledger on the brass balance, and the one question the Book has no page for: where do the copies live that nobody ever put back on the Chancery's shelves? |

### `07-jobs/02-acquisition/`

| File | Type | P | One line |
|---|---|---|---|
| [[acquisition-aftermath]] | index | — | The denouement of acquisition (Core p. 292): the reflection, the fallout, and the one decision this job exists to put in front of the table. |
| [[acquisition-vectors]] | index | — | Every major force in acquisition, with a want (what it is trying to achieve here), a push (what it is able and willing to spend), and a face (the person; Core p. 290 — "even if the main foe is Megacorp International, the |
| [[acquisition]] | job | — | acquisition; 3 session(s); pole pivot; pivot twist True — Take the Coldwater counterpart — the second-copy volume of everything filed under AP&I's Coldwater Outfall lease — out of the Chancery Records Repository at Kilbride before the collection run pulps it, and deliver it whole to the employer without the Chancery, AP&I, or Continuity learning it is gone. |

### `07-jobs/02-acquisition/challenges/`

| File | Type | P | One line |
|---|---|---|---|
| [[acquisition-roster]] | index | — | Everything acquisition puts in front of the crew, in one list: what is written new for this job, what is pulled unchanged from elsewhere in the vault, and what is reused from the book through generic-reuse-map. |
| [[collection-run]] | challenge | — | countdown, Scale 2 — The digitization contract: collect, scan, certify, pulp. Job-level countdown for the Acquisition. It is not protecting the volume — it is going to destroy it, on a schedule, with a completion bonus attached. |
| [[counterpart-stacks]] | challenge | — | barrier, Scale 2 — Four hundred metres of shelving holding the second half of Palisade's official memory: numbered runs, a scanning crew's arc-lamp, a duty clipboard, and a bonded cage. It cannot be hacked and it does not fight; it costs time, and time is the thing the crew do not have. |
| [[the-carters]] | challenge | — | pursuer, Scale 2 — Five freelancers who move things for people who cannot be seen moving them. Hired eleven weeks ago through three intermediaries to take the same volume, told it must arrive unread, and waiting on the road because they are thieves on roads, not thieves in buildings. |

### `07-jobs/02-acquisition/characters/`

| File | Type | P | One line |
|---|---|---|---|
| [[ileana-boakye]] | npc | — | The records assistant on the scanning contract who has been lifting counterpart pages ahead of the scan and selling them; the insider pulling the same job in Job 2, and the bottom of the supply line Job 1's second copies came up. |
| [[ilya-sarpong]] | npc | — | "Barrow" — Lead of the Carters, the rival freelance crew pulling the same job in Job 2; sets the ambush on the escape route and opens with a fair price. |
| [[margit-nakagawa]] | npc | — | The solicitor's clerk who hires the crew at the Weighhouse counter for a principal she will not name; the employer's face in Job 2. |

### `07-jobs/02-acquisition/scenes/`

| File | Type | P | One line |
|---|---|---|---|
| [[acquisition-01-a-job-at-the-counter]] | scene | — | 1 · gullet-market · The Weighhouse counter at the end of the market day: the brass balance still swinging, the Slate chalked up by the counter door, and a solicitor's clerk in expensive shoes standing where the dockers usually stand. |
| [[acquisition-02-the-lower-gate]] | scene | — | 2 · chancery-hill · The Chancery's lower gate at nine in the morning: police post, permit-assistance kiosks that are forgers, a café full of clerks taking envelopes over coffee, and above it the atrium queue of people holding paper and being seen to be grateful. |
| [[acquisition-03-the-scan-index]] | scene | — | 3 · the-lattice · Gallery Seven, half a kilometre of racks in blue light and a cold that gets into the teeth — and inside the Chancery's records Domain, a scanning index growing one volume at a time, with a shelf list, a collection schedule, and a pulping certificate at the end of every row. |
| [[acquisition-04-thirtieth-deck]] | scene | — | 4 · amalgam-stack · The Contracts Office on the thirtieth deck of the Stack: carpet, filtered air, a view of foundry heat venting off the cliff, and two hundred people whose whole working life is a column of figures that balances. |
| [[acquisition-05-the-prep-sequence]] | scene | — | 5 · gullet-market · The Weighhouse back room after the counter door shuts: a table, a hot plate, a shelf of bound ledgers nobody is allowed to touch, and a shelf list from a warehouse in the sprawl held flat under a mug. |
| [[acquisition-06-the-paper-barn]] | scene | — | 6 · kilbride-stretch · A leased bay in a distribution warehouse the size of a district: drone-lanes overhead, a loading apron under sodium light, a roller door with a Chancery seal stencilled on it, and behind it four hundred metres of steel shelving holding the second half of Palisade's official memory. |
| [[acquisition-07-the-coldwater-run]] | scene | — | 7 · kilbride-stretch · core moment · The bonded cage at the end of run C: welded mesh, a broken seal, an arc-lamp gantry three runs away throwing everything into hard shadow, and one buckram volume open flat on a steel shelf with a crew standing around it not moving. |
| [[acquisition-08-collection-night]] | scene | — | 8 · kilbride-stretch · core moment · The loading apron at four in the morning: sodium light, a records-contractor van with a real plate reversing up to the roller door on the wrong night, and four kilometres of identical prefab grid between the crew and anywhere. |
| [[acquisition-09-what-a-page-is-worth]] | scene | — | 9 · gullet-market · Delivery, in whichever of three rooms the crew choose: the Weighhouse back room with the volume on Tally's balance; a firm's meeting room behind the Hill with Nakagawa counting cash; or a bench in the Chancery's garden where a Superintendent has agreed, once, to be seen with people who do not work for the Hill. |

## Canon and flags

- Job types, structure, and the pivot: Brief §1.2, §7; Core p. 281, 284–293. Jobs 1 and 2 are written by WP7b and WP7c in parallel; their rows above restate the Plan's brief for them and nothing more.
