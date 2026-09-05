---
type: scene
name: "The Mirror Rig"
slug: investigation-04-the-mirror-rig
status: review
source: custom
page: "291, 290, 308, 309, 22, 27–28"
owner: WP7b
canon_refs: ["Bible §6", "Brief §6.5", "Brief §7.2", "Core p. 290", "Core p. 291", "Core p. 308", "Core p. 309"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
job: investigation
order: 4
set_piece: "Ten storeys of two-metre capsules under a dead relay mast, every door locked from the inside — and in one of them a rig holding a bad, partial mirror of twenty years of the Foot's property, with somebody else's search still cached on it."
district: relay-fields
story_tags: ["every kid is a hacker", "a capsule two metres by one", "somebody else's search, still cached"]
challenges: [the-consignment-window, escapee-list, escapee-recovery-desk]
vectors_active: [rasheeda-novak, the-factor, the-consignment-window]
core_moment: true
flashback_hooks:
  - "One of you has been in a coffin-block for longer than a night. What were you hiding from, and did it work?"
  - "Before the Ledger, somebody taught one of you how to Harness on borrowed hardware. What did you owe them?"
outcomes_to_next:
  - "The query: the Book's provenance cross-matched against AP&I warranty telemetry to produce a roster of bodies that are unaccounted for."
  - "The crew's own dead tags, inside somebody else's search string."
  - "The telemetry came from AP&I as year-blocks of aged write-offs, sold on by the Contracts Office."
---

# The Mirror Rig

![[assets/jobs/investigation/investigation-04-the-mirror-rig.png]]

**Job:** [[investigation]] · **Order:** 4 · **District:** [[relay-fields]] · **Story tag:** *every kid is a hacker* · **Core moment:** **yes — the Job goes deeper (1)**

The Job's cyberspace scene. Cyberspace runs **as written** (Brief §6.5): Nearspace, Domains, the Tangle, Harnessing, exactly as the book has them, with nothing of Tao asserted anywhere in it (**[OPEN]** OQ-15).

## Set piece

The coffin-blocks between the towers: ten storeys of capsules two metres by one, each with a jack, a screen, and a door that locks from the inside, stacked under three hundred metres of rusted lattice with the whole Foot laid out below ([[relay-fields]]). A crew can vanish into one and nobody will look, because everyone in a coffin-block is somewhere else.

Capsule 6-114 has been rented continuously for two years by a rig-builder [[dessa-rahimi|Chit]] found, on the Weighhouse's money, to hold the **mirror**: a bad, incomplete, roughly one-third-indexed copy of the last two years of the Book, made because paper burns ([[fence-network]], BC-102). Tally knows it exists and has decided to let it. Dessa has never read it and thinks about it constantly.

She is here when the crew arrive, sitting in the corridor with her back against the capsule door, because the query log from Wax's tag points at this rig and she worked that out on the way over.

## What the rig holds

The mirror is a **Domain** in the book's sense: a small, cheap, badly-lit one, built by a Relay Fields kid out of Gullet parts, its metaphor a warehouse aisle of shelves with the wrong labels. Harnessing in is easy. Finding anything is not — the index is a third done, which is what makes the *cached search* so loud.

Somebody has been in here. Four times in eleven days, from outside, through the block's own Nearspace, using a credential that was bought and not cracked. They did not take the mirror. They ran a **search** on it and took the answer.

### The core moment — the query

Prepared as a situation (Core p. 290). The set is the aisle; the atmosphere is a warehouse with the lights failing one bank at a time; the story tags are *somebody else's search, still cached* and *a third of the shelves have no labels*. Then the players are let in and the search string is readable.

It is a **join**. On one side, the Book's provenance: what crossed the brass balance under the Wall, who brought it, and what it turned out to be. On the other side, a second dataset that is not Tally's at all — **AP&I warranty telemetry**, sold on in year-blocks of aged write-offs, the servicing records of chrome whose accounts have been closed at zero value.

Matched together, the two produce one output, and it is not a list of goods. It is a list of **bodies that stopped being accounted for**: people whose chrome surfaced under the Wall without them, or whose tags stopped answering on a date, or whose parts were weighed by somebody who did not know whose they were. Everyone in Palisade whom the record has lost, with a date and a district against each.

Four hundred and some names, and rising, and the crew are in it.

Their own tags — the ones they walked out of [[coldwater-outfall]] wearing — are dead tags on a written-off account, which is the second of Tally's three buying categories exactly. They have been line items in somebody's order since before they met her.

**This is where the Job goes deeper** (Core p. 286): the crew came looking for a runner, and found that the thing they are investigating already contains them.

## The hard choices here

- **Casters.** A discipline runs only while its condition holds ([[casters]]). A coffin-block is two metres of other people's audio, screens, and jack-hum in every direction; nothing that needs silence, stillness, both hands free or a month-fresh working survives it. A Caster who keeps the condition — by finding a place in the stack where it can be kept, at the price the discipline takes in hours the crew do not have — reads the query outright, join and output and credential. A Caster who breaks the condition to act now gets the same answer and lapses, and must re-establish the practice in Downtime before [[investigation-08-the-cordon]].
- **Doppels.** The output's definition — *bodies that stopped being accounted for* — covers every Cutloose who ever had a tracker cut out at the Sump. The names off the Wall of Faces are in the same query as the crew's ([[changeling-cells]], [[odile-ferraz]], [[fresh-cut]]). Telling Gallery Nine buys allies and starts thirty escapees racing a consignment they cannot reach. Not telling keeps the crew's edge (**[OPEN]** OQ-48).

## Challenges

- [[escapee-recovery-desk]] — watcher. The join *is* the Desk's job description being done by somebody who does not work there, and every AP&I record the crew touch in this scene is `priced`.
- [[escapee-list]] — watcher, background; a credential query against a Fields rig is one `noticed` tier.
- [[the-consignment-window]] — countdown, running; add a tier if the crew take Downtime in the block.
- Reuse: **Hacker** (Core p. 309) at Scale 0 for the rig-builder and for Dessa's own kit — a Fields build, not a professional's; **Cyberspace Intrusion Countermeasure AI** (Core p. 308) only if the crew go the other way and follow the bought credential back through the block's Nearspace toward whoever used it, which is a barrier and not a lead. See [[investigation-roster]].

## Vectors active

- [[the-factor]] — offstage, and now measurable: he bought a credential rather than cracking one, which is what a man with somebody else's money does.
- [[rasheeda-novak]] — offstage. The telemetry half of the join came out of her corporation, and not out of her desk.
- [[the-consignment-window]] — running.

## Flashback slots

- Prompt only: "One of you has been in a coffin-block for longer than a night. What were you hiding from, and did it work?"
- Prompt only: "Before the Ledger, somebody taught one of you how to Harness on borrowed hardware. What did you owe them?"

## What carries forward

- **The join**, and what it outputs.
- **The crew's names in it**, which is the Job's first real cost.
- **The telemetry's origin** — year-blocks of aged write-offs, sold on — which is an AP&I sale and therefore has a seller. → [[investigation-05-the-back-room-at-lumen]].
- **Dessa**, who now knows the mirror she built is the reason a runner is dead, and who will do something reckless about it if nobody stops her.

## Canon and flags

- Cyberspace as written — Nearspace, Domains, the Tangle, Harnessing: Brief §6.5; [[pillars]]. The mirror of the Book and Dessa's part in it: BC-102, BC-103, [[dessa-rahimi]]. Warranty telemetry on every Fitted body; write-offs kept on the book at zero value: BC-101, [[corp-c]]. The crew on the escapee list with no bounty: Bible §6.
- **[BUILD CHOICE]** the query, the join, and the roster of unaccounted bodies; see [[build-choices]] "Added by WP7b".
- **[OPEN]** (OQ-15) nothing here asserts Tao in cyberspace. (OQ-37) the credential was bought through an intermediary and leads to the Factor, not to a buyer. (OQ-48) the Doppel hook raises the legal status of an escaped Doppel and does not settle it.
