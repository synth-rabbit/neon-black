---
type: job
name: "A Full Set of Names"
slug: investigation
status: review
source: custom
page: "284–293, 286, 76–113, 118–120, 124–125"
owner: WP7b
canon_refs: ["Bible §3 power structure", "Bible §5", "Bible §6", "Brief §1.2", "Brief §5", "Brief §7.2", "Brief §7.3", "Core p. 285–287", "Core p. 287–293", "Core p. 291", "Core p. 124–125"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
job_type: [investigation]
sessions: 3
series_pole: paycheck
hooks:
  - "The Weighhouse offer: a runner went out with a bundle of the Book's pages and did not come back, and Tally will not ask the Gullet to help her look."
  - "Personal: whatever the crew are wearing, using or owing still reports somewhere, and the first page of the bundle is a list of bodies that stopped being weighed — which is what they are now."
goal: "Find out who took the runner and what the pages were for, and put a name to the buyer who has been purchasing provenance in bulk out of the Book for eighteen months."
employer_vector: marisol-okonkwo
vectors: [marisol-okonkwo, the-factor, emeric-vann, rasheeda-novak, halima-boyce, the-consignment-window]
core_moments: [investigation-04-the-mirror-rig, investigation-06-the-lower-gate, investigation-08-the-cordon]
scenes:
  - investigation-01-the-counter-door
  - investigation-02-the-labyrinth-route
  - investigation-03-the-cold-room
  - investigation-04-the-mirror-rig
  - investigation-05-the-back-room-at-lumen
  - investigation-06-the-lower-gate
  - investigation-07-the-counting-room
  - investigation-08-the-cordon
  - investigation-09-what-the-book-cannot-say
climax: investigation-08-the-cordon
aftermath: investigation-aftermath
twist_for_pivot: false
key_players_touched: [fence-network, government, corp-c, upstart, changeling-cells]
districts_touched: [gullet-market, suture-row, relay-fields, corbel-gallery, chancery-hill, kilbride-stretch]
complications:
  - "A clue the crew expects to find is missing, due to a cover up (Core p. 286): the runner's route chit was eaten, the pawnbroker's day-book has a torn stub, and the Chancery page they need has been struck — on one copy."
  - "The Job goes a lot deeper than first thought, putting the crew in the sights of someone powerful in the Megacity (Core p. 286): twice, at [[investigation-04-the-mirror-rig]] and [[investigation-06-the-lower-gate]]."
  - "A clue is itself dangerous to handle, or leads somewhere the PCs would rather not go (Core p. 286): a warranty tag that answers is a tag that reports, and the Hill's registry reads the requester before it reads the request."
---

# A Full Set of Names

**Type:** investigation (Core p. 286) · **Sessions:** 2–3 · **Pole:** paycheck · **Pivot twist:** no · **Employer:** [[marisol-okonkwo|Marisol Okonkwo, "Tally"]] through [[fence-network|the Weighhouse]]

The crew's first paid work. It begins as a missing runner and a bundle of paper, and ends with the crew holding proof that Palisade keeps two records of who it has lost — and a place where the second one can be taken. It hands directly to [[acquisition]].

## Hooks

- **The Weighhouse offer.** A runner called Wax went out of the counter door with a bundle nobody weighed and has not come back. Tally will not put it on the Slate and will not send the network after it, because a fence who is seen looking for her own paper is a fence whose paper is worth stealing. She will pay a crew nobody knows yet. The offer is made across the brass balance, with food on the table, and it is chalked ([[the-weighhouse]], *The Percentage*).
- **The personal hook.** Tally names the three buying categories out loud — corporate shipping losses, chrome with dead tags, and things nobody can explain — and a crew of Ledger escapees hears the second one as a description of themselves. Whatever chrome they walked out of [[coldwater-outfall]] wearing still has a tag on it, and a tag that is not answering is a tag somebody has started paying money for. Every PC is already an entry in the thing they are being hired to find. Ties to [[escapee-list]] (`noticed`) and [[escapee-recovery-desk]] (`priced`).

## Goal

Find out who took Wax and what the pages were for, and put a name to the buyer who has been purchasing provenance in bulk out of the Book for eighteen months (**[OPEN]** OQ-37).

The crew will get a name. It will be the wrong one, and knowing that it is the wrong one is the job's real payment.

## Structure

Four movements across two or three sessions, in the book's investigation shape (Core p. 291: a starting scene, "snooping around" follow-ups, the core moments, a finale that raises tension to the max).

1. **The offer and the street.** [[investigation-01-the-counter-door]] → [[investigation-02-the-labyrinth-route]] → [[investigation-03-the-cold-room]]. The Gullet and the Row. Wax is found; the bundle is not.
2. **What the pages were for.** [[investigation-04-the-mirror-rig]] (core moment — the Job goes deeper) → [[investigation-05-the-back-room-at-lumen]]. The Fields and the Gallery. The purchase is not about goods.
3. **Two copies.** [[investigation-06-the-lower-gate]] (core moment — the Job goes deeper again). The Hill. The escapee list exists twice.
4. **The consignment.** [[investigation-07-the-counting-room]] → **climax** [[investigation-08-the-cordon]] → [[investigation-09-what-the-book-cannot-say]] → [[investigation-aftermath]].

## The clue chain

Each row is a clue, where it sits, what it establishes, and the lead it opens. The chain is not a corridor: scenes 2–6 can be taken in any order the crew choose, and the two rows marked **goes deeper** are the only ones that must both land before [[investigation-07-the-counting-room]] is playable.

| # | Clue | Where | What it reveals | Next |
|---|---|---|---|---|
| 1 | A wax-sealed chit with a route on it, eaten and recovered, and a bundle that never crossed the balance | [[investigation-01-the-counter-door]] · [[gullet-market]] | Wax was carrying an *order* out of the network, not a delivery: pages pulled from the Book against a standing list of three categories | Retrace the route |
| 2 | A pawnbroker's day-book with a torn stub, and a receipt written in a hand that is not the Weighhouse's — paid in Chancery instruments, not cash | [[investigation-02-the-labyrinth-route]] · [[gullet-market]] | The order was placed by a consolidator the Foot calls **the Factor**, who buys on commission for people who do not want to be seen buying, and who settles in paper from the Hill | Follow the paper, or follow Wax |
| 3 | A warranty tag still answering from a chop-shop cold room, on a body it is no longer attached to | [[investigation-03-the-cold-room]] · [[suture-row]] | Wax is dead; her chrome was stripped and her tag deliberately left live, so the ledger she appears in would stay tidy. Two tables over, a body burned from the inside out that nobody on the Row will price | The tag's query log |
| 4 | **Goes deeper (1).** The query log on the Book's mirror rig | [[investigation-04-the-mirror-rig]] · [[relay-fields]] | The buyer is not buying goods. Somebody is cross-matching the Book's provenance against AP&I warranty telemetry to produce a roster of bodies that are unaccounted for — and the crew's own dead tags are inside the query | Who supplied the telemetry |
| 5 | An aged write-off ledger, re-priced and sold on, in a back room that does uncatalogued work | [[investigation-05-the-back-room-at-lumen]] · [[corbel-gallery]] | AP&I's Contracts Office has been selling written-off accounts to the Factor by the year-block. [[rasheeda-novak]] has been buying pages of her own, in a different pattern, and says the bulk order is not hers | The instruments the Factor pays in |
| 6 | **Goes deeper (2).** The crew's own page on AP&I's escapee list, produced twice, with two seals in different inks | [[investigation-06-the-lower-gate]] · [[chancery-hill]] | The list exists in **two copies**, because the Office of Concurrent Jurisdiction double-sold the paper registry. The crew are struck from one copy and standing on the other — and the Factor has been buying the second copies | The consignment, and where it goes |
| 7 | A consignment ledger, a weigh-in desk, and a delivery window | [[investigation-07-the-counting-room]] · [[kilbride-stretch]] | The order is a *full set*: goods provenance, telemetry, and now name-bearing paper. The Factor cannot name his principal — payment arrives as pre-bought concurrences through three intermediaries | The finale |
| 8 | Who arrives to close the room, and under whose authority | [[investigation-08-the-cordon]] · [[kilbride-stretch]] | Somebody bought lawfulness over this address before anything happened here | Get out with it |
| 9 | Where the second copies actually live | [[investigation-09-what-the-book-cannot-say]] · [[gullet-market]] | The double-sold pages left the Chancery's shelves years ago under a records-retention lease and sit in a leased bay in a distribution warehouse in the Stretch — the Chancery Records Repository, **the paper barn** — which is a room, in a building, with a door | → [[acquisition]] |

### The two places the Job goes deeper

Both are the book's own Investigation complication — *the job goes a lot deeper than first thought, putting the crew in the sights of someone powerful in the Megacity* (Core p. 286) — used twice, at different scales.

- **First (scene 4):** the crew came looking for a runner and a bundle. What they find is that they are line items. The job stops being a Weighhouse errand and becomes personal in the only way this Series does personal: on paper, priced, and not yet worth collecting ([[escapee-recovery-desk]], *A Write-Off Is Not A Forgiveness*).
- **Second (scene 6):** the crew came looking for a buyer. What they find is that the record of Palisade does not agree with itself, that this is not an accident, and that the people who broke it are the ones who sell the only lawful account of any event in the city ([[government]], BC-122). From that moment the crew are carrying knowledge that four corporations and the Hill would all rather nobody had, and none of them knows they have it. That is the sights they are in.

## Core moments

Prepared as situations, in the book's sense (Core p. 290) — set, atmosphere, story tags, and who is present, then the players are let in.

- [[investigation-04-the-mirror-rig]] — **the query.** A rig in a coffin-block, a badly indexed mirror of twenty years of the Foot's property, and a search string somebody else ran on it four times.
- [[investigation-06-the-lower-gate]] — **two seals in different inks.** A clerk turns a page around on a café table where the Hill's clerks take their envelopes, and there are two of it.
- [[investigation-08-the-cordon]] — **whose room this is.** Two lawful forces, one address, one hour, and a piece of paper that says which of them is real.

## Set pieces

- **The counter door and the brass balance** ([[investigation-01-the-counter-door]]) — the Weighhouse at the second hour, coasters unloading on the water side.
- **The cold room behind Threadneedle** ([[investigation-03-the-cold-room]]) — three surgical bays, a chest freezer that is also a morgue, floodwater in the corridor.
- **The coffin-block stack at night** ([[investigation-04-the-mirror-rig]]) — ten storeys of two-metre capsules under a dead relay mast, every door locked from the inside.
- **The counting room** ([[investigation-07-the-counting-room]]) — a converted automat unit in the Stretch with a bonded door, a weigh-in desk, and four hundred bundles on numbered shelves.
- **The cordon** ([[investigation-08-the-cordon]]) — a grey van with the side door already open, a taped line across a prefab street, and a second set of headlights that should not be there.

## Vectors

See [[investigation-vectors]]. In brief: the employer is always a vector (Core p. 290) and here that is **[[marisol-okonkwo|Tally]]**; the opposition is **the Factor** ([[the-factor]]); the Hill is **[[emeric-vann]]** below and **[[halima-boyce]]** above; AP&I is **[[rasheeda-novak]]**, who is a rival buyer and not the buyer; and time is **[[the-consignment-window]]**, a Countdown Challenge that is the job's time-pressure vector and does not think.

## Ties to PC themes — the hard choice, one per splat

Each hook below is written so it only fires if that splat is at the table. None of them is required for the Job to resolve; each of them costs the crew something real if it is taken, and something else if it is not. Written against the Itch, Ritual or Identity each splat's kits carry (Brief §2.5; [[pillars]]).

- **Bloodware** — *the Itch against the evidence.* In [[investigation-03-the-cold-room]] the crew need Wax's body intact enough for the Row's surgeon to read what was taken out of her, and there is a second body two tables over, burned from the inside out and unpriced, with no owner and no page. The Itch is *feed the strain — blood or iron* ([[bloodware]]), and the cold room is full of both. Feeding here costs the crew the clue: what the surgeon could have read is gone, the chain skips row 3, and scene 4 opens without the query log. Stifling it marks Decay. The second body is never explained — the Row will not price it, [[em-ambush]] is what did it, and nobody in this Job knows or says by whom (**[OPEN]** OQ-17).
- **Howlers** — *the dose against the debt.* [[investigation-02-the-labyrinth-route]] can be run down on foot in the Labyrinth's roof-space at a speed no unmodified body holds, and the Almoners' collector working the Gullet that night has clinical-grade on him ([[leash-almoners-cut]]). He will not sell it. He will trade it, for the name of who is paying the crew — which puts the Weighhouse into the Kitchen's ledger, permanently, and Tally will find out ([[syndicate]]; [[howlers]]). Taking the dose gets the crew ahead of the Factor's own people at scene 7. Refusing it means the roof-space is closed and row 2 costs a Tracked outcome instead of a Quick one.
- **Casters** — *the condition against the moment.* A discipline runs only while its condition holds ([[casters]]). Two scenes in this Job actively break conditions: the coffin-block stack in [[investigation-04-the-mirror-rig]] is two metres of noise, screens and other people's audio in every direction, and the counting room in [[investigation-07-the-counting-room]] is under an AP&I-supplied site rig that floods a room until nothing can be held. A Caster who keeps the condition can read the query log or the consignment ledger outright, at the price the discipline takes; a Caster who breaks it to act in the moment does the thing and lapses, and the practice must be re-established in Downtime before the climax. There is no third option and the MC does not offer one.
- **Doppels** — *the face against the roster.* The fastest way past [[chancery-process]] in [[investigation-06-the-lower-gate]] is to be a clerk who already has a queue number, and the Hill's atrium is the most photographed room in Palisade. Worse: the roster on the mirror rig is a list of people whose bodies stopped being accounted for, and that description covers every Cutloose who ever cut a tracker out at the Sump. The names off the Wall of Faces are in the same query as the crew's ([[changeling-cells]], [[odile-ferraz]]). A Doppel who tells Gallery Nine buys allies and puts thirty escapees into a race against a consignment; a Doppel who does not keeps the crew's edge and will have to look at [[fresh-cut]] again knowing (**[OPEN]** OQ-48).
- **Baselines** — *the line against the log.* Reading a live warranty tag ([[investigation-03-the-cold-room]]) or pulling the telemetry side of the query ([[investigation-04-the-mirror-rig]]) properly wants an interface port, and AP&I's licensed channel on the Row will fit one that afternoon at a price a broke crew can nearly afford ([[api-enhancement-splice]] — enhancement, not replacement, and therefore across the line the Baseline holds; [[baselines]]). The alternative is to do it the Baseline way: a bench reader, a borrowed clinic terminal, four hours, and a scene of exposure at [[investigation-05-the-back-room-at-lumen]] where a port would have taken four minutes. The Job never rewards taking the splice — it only makes it available, twice, at the worst moment. ([[api-replacement-limb]] remains open to a Baseline who lost a part in scene 8; that is a different question.)

## Complications

From the Investigation list (Core p. 286), all three, placed rather than rolled:

- **A clue the crew expects to find is missing, due to a cover up.** Wax ate her route chit; the pawnbroker's day-book has a stub torn out; the crew's name is struck from one Chancery copy and not the other. Three instances, escalating from "somebody was careful" to "the record itself is the cover-up."
- **The Job goes a lot deeper than first thought.** Twice, as above.
- **A clue is itself dangerous to handle, or leads somewhere the PCs would rather not go.** A warranty tag that answers reports while it is read ([[escapee-recovery-desk]], *Every Fitted Body Reports*); the registry reads the requester before it reads the request ([[chancery-process]]); and the last lead in the chain is a Chancery leasehold in the sprawl on a destruction schedule — a building a Foot crew has no business robbing.

## Key Players and districts

**Key Players touched** (≥2 required, five present): [[fence-network]] (employer and the Book), [[government]] (the registry, the Office, the Envelope Detail), [[corp-c]] (telemetry, write-offs, the Recovery Desk), [[upstart]] (a crisis-response cell at the cordon, and nothing else said), [[changeling-cells]] (through the Doppel hook only).

**Districts** (≥3 required, six present): [[gullet-market]] · [[suture-row]] · [[relay-fields]] · [[corbel-gallery]] · [[chancery-hill]] · [[kilbride-stretch]].

## Challenges

Full roster with reuse-by-slug first: [[investigation-roster]]. Custom to this Job: [[the-factor]], [[a-tag-still-answering]], [[the-counting-room]], [[the-consignment-window]].

## Canon and flags

- Paycheck framing and hiring through the fence or her network: Bible §5, §6; Brief §1.2, §7.2. The crew on AP&I's escapee list with no bounty: Bible §6; [[escapee-list]]. The Chancery's double-sold paper registry: BC-122, [[government]]. The Book and provenance as the product: BC-102, [[fence-network]]. Investigation job type and its complications: Core p. 286. Job structure, vectors, core moments, set pieces, hooks, denouement: Core p. 287–293.
- **[BUILD CHOICE]** The clue chain, the Factor, the *full set* order, and the handoff to [[acquisition]] are this package's construction (BC-151 to BC-160); the names *Wax*, *the Factor*, *Anselm Boateng*, *Ivo Meszaros* are proposals in [[names]]. The place the lead points at was reconciled with Job 2 by WP8 (BC-171): WP7b's *Second Shelf* behind the Hill is superseded by WP7c's paper barn in the Stretch, and the handoff reads accordingly.
- **[OPEN]** (OQ-37) who is buying provenance in bulk is **not answered here and may not be answered here**. The Factor is an intermediary who does not know. Both Continuity and AP&I remain live readings at the end of this Job, and [[investigation-aftermath]] says so in terms. **[OPEN]** (OQ-11) nothing in this Job decides whether Tally is connected to Continuity. **[OPEN]** (OQ-10) Rook's motives are not touched. **[OPEN]** (OQ-17) the second body in the cold room is never explained. **[OPEN]** (OQ-48) whether a Doppel is property in law is raised by the Doppel hook and not resolved.
