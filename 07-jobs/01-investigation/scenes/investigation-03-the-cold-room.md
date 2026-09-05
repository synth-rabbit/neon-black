---
type: scene
name: "The Cold Room at Threadneedle"
slug: investigation-03-the-cold-room
status: review
source: custom
page: "291, 305, 320"
owner: WP7b
canon_refs: ["Bible §2 vampire", "Bible §3 haves and have-nots", "Bible §6", "Brief §7.2", "Core p. 291", "Core p. 305", "Core p. 320"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
job: investigation
order: 3
set_piece: "Three surgical bays behind a hand-painted sign, floodwater in the corridor, and a chest freezer that is also a morgue — with a warranty tag inside it, still answering, on a body it is no longer attached to."
district: suture-row
story_tags: ["stitched up, sent back out", "floodwater in the basement", "a tag that is still answering"]
challenges: [a-tag-still-answering, escapee-recovery-desk, escapee-list, the-consignment-window]
vectors_active: [rasheeda-novak, the-factor, the-consignment-window]
core_moment: false
flashback_hooks:
  - "Somebody on this Row has already done work on one of you, off the record. What did it cost, and what is still owed?"
  - "The last time you were near a body that had been taken apart for parts, whose was it?"
outcomes_to_next:
  - "Wax is dead; her chrome was stripped and the tag deliberately left live so a ledger somewhere would stay tidy."
  - "The tag's query log: four searches, run from outside, on a rig in the Relay Fields."
  - "A second body in the cold room that nobody on the Row will price, burned from the inside out."
---

# The Cold Room at Threadneedle

![[assets/jobs/investigation/investigation-03-the-cold-room.png]]

**Job:** [[investigation]] · **Order:** 3 · **District:** [[suture-row]] · **Story tag:** *stitched up, sent back out* · **Core moment:** no

The second **"snooping around" scene** (Core p. 291). It can be a montage of three questions on the Row, or one long Tracked outcome in a room with a freezer in it. It is the scene where the Job stops being about paper.

## Set piece

Threadneedle: a street-level chop-shop under a hand-painted sign, three surgical bays, a fitter's bench, and a waiting room that is also the surgeon's kitchen ([[suture-row]]). The surgeon is [[ivo-meszaros|Ivo Meszaros]] — fifties, chain-drinking tea, a Patched left hand he built himself, does anything, asks nothing, takes chrome in part-payment. Storm season has the corridor under four centimetres of water and everybody has stopped mentioning it.

The cold room is at the back: a walk-in chest freezer that the Row uses as a morgue between collections, because the Chancery's collections come when they come. There are three bodies in it.

**The first is Wax.** Nine days. Her chrome is gone — the leg, the shoulder assembly, the eye — cut out clean by somebody competent, and *not* by Meszaros, who says so and is telling the truth. She was killed first, badly, by people who were being quick rather than careful.

**Her warranty tag is still in her.** A subdermal AP&I tag under the skin of the forearm, left in on purpose, still answering. That is the whole clue. A stripped body with a live tag is a body whose ledger line still reads *in good standing* — somebody wanted the warranty record to stay tidy while the parts moved. The tag is the only piece of Wax that anybody paid to keep.

**The second body is not part of the Job.** Male, no papers, no chrome worth taking, and burned from the inside out: the skin unmarked, everything under it cooked. Meszaros will not price it, will not cut it, and would like it gone. He has seen two others this year and has stopped asking. Nobody in this Job explains it, and nobody in this Job may. **[OPEN]** (OQ-17) — see [[em-ambush]], which is what did it, and which says nothing about who.

## The tag

Profiled as [[a-tag-still-answering]] — role **mystery**, Scale 0. Reading it is the point of the scene, and reading it is dangerous, which is the book's third Investigation complication (Core p. 286).

- Reading it properly gives its **query log**: four searches run against this tag from outside in the last eleven days, all four from the same rig, and the rig is in the [[relay-fields]] — which is where the Book's mirror lives ([[dessa-rahimi]]).
- Reading it at all makes it report. Every read is `priced-1` on [[escapee-recovery-desk]] (*Every Fitted Body Reports*), and a licensed reader on the Row makes it worse.

**Baseline hard choice.** Reading the tag properly wants an interface port. AP&I's licensed channel on the Row will fit one this afternoon, on credit, and it is an **enhancement** and not a replacement ([[api-enhancement-splice]]) — over the line a Baseline holds ([[baselines]]; Bible §2 hunter). The alternative is Meszaros's bench reader, four hours, and a scene of exposure later at [[investigation-05-the-back-room-at-lumen]] where a port would have been four minutes. The Job offers the splice and never rewards it.

**Bloodware hard choice.** The cold room is full of blood and iron and two of the three bodies are nobody's ([[bloodware]] — the Itch is *feed the strain*). Feeding here costs the chain its third row: what Meszaros could have read out of Wax is gone, the query log with it, and [[investigation-04-the-mirror-rig]] opens blind. Stifling the Itch marks Decay. There is no version where a Bloodware PC gets both, and the second body is sitting right there being exactly the wrong kind of temptation.

## Challenges

- [[a-tag-still-answering]] — mystery, Scale 0. The scene's spine.
- [[escapee-recovery-desk]] — watcher. `priced` runs whenever AP&I hardware is touched, read, serviced or bought in this scene.
- [[escapee-list]] — watcher, background.
- [[the-consignment-window]] — countdown, running.
- Reuse: **Security Guard** (Core p. 305) if the crew go up to Marrowgate's licensed floors instead; **Surveillance Drone** (Core p. 320) retained by the Desk on a standing contract, which is not looking at them. See [[investigation-roster]].

## Vectors active

- [[rasheeda-novak]] — offstage, and closer than she was. Every read of a tag is a line in her dataset.
- [[the-factor]] — offstage. The people who stripped Wax were hired by the evening and are already elsewhere.
- [[the-consignment-window]] — running.

## Flashback slots

- Prompt only: "Somebody on this Row has already done work on one of you, off the record. What did it cost, and what is still owed?"
- Prompt only: "The last time you were near a body that had been taken apart for parts — whose was it?"

## What carries forward

- **Wax is dead**, and the Job has a body in it. Tally is told, or is not, and both are choices with prices.
- **The query log** → [[investigation-04-the-mirror-rig]].
- **The second body**, unexplained, and Meszaros's face when he says he has seen two others.

## Canon and flags

- Threadneedle and the Sump, the Row's chop-shops and floodwater: [[suture-row]]. Warranty telemetry on every Fitted body and the Standing Account: BC-101, [[corp-c]]. Baselines take cybernetics only as replacements: Bible §2 hunter, [[baselines]]. Bloodware weaknesses are EM and the master node — the second body is an EM kill, never sun, fire or a stake: Bible §2 vampire, [[em-ambush]].
- **[BUILD CHOICE]** Ivo Meszaros (the Row file leaves Threadneedle's surgeon to be named by WP4 or WP7), the live-tag method, and the placement of the second body; see [[build-choices]] "Added by WP7b".
- **[OPEN]** (OQ-17) the second body is never explained in this Job or its aftermath.
