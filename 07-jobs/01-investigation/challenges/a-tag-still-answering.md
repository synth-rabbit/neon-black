---
type: challenge
name: "A Tag Still Answering"
slug: a-tag-still-answering
status: review
source: custom
page: "294–300, 297"
owner: WP7b
canon_refs: ["Bible §2 vampire", "Bible §6", "Brief §8", "Core p. 294–300", "Core p. 297"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: mystery
scale: 0
alias: "a bump under the skin of a forearm"
short_description: "An AP&I warranty tag left deliberately live in a body whose chrome has been cut out of it, so that a ledger somewhere would go on reading 'in good standing'."
limits:
  - {name: read-the-tag, tier: 3}
  - {name: read-the-query-log, tier: 4}
  - {name: silence-it, tier: 2}
default_tags: ["still in good standing", "eleven days of queries", "warranty telemetry"]
default_statuses: []
specials:
  - {name: "It Reports While It Is Read", text: "Every attempt against read-the-tag or read-the-query-log gives [[escapee-recovery-desk]] priced-1, whether or not the attempt succeeds (Every Fitted Body Reports). Using a licensed reader — a clinic terminal, a warranty booth, a fitted interface port bought on AP&I's channel — makes it priced-2 instead. There is no way to read it that does not tell somebody."}
  - {name: "Whoever Left It Wanted The Ledger Tidy", text: "The tag is the only part of the body anybody paid to keep. Reading it establishes, without a roll, that the killing was incidental and the bookkeeping was not: a stripped body with a live tag still services its account, and an account in good standing is not reviewed."}
  - {name: "The Query Log", text: "Maxing read-the-query-log yields four searches run against this tag from outside in eleven days, all four from one rig, and the rig's location: a coffin-block in the Relay Fields. This is the only route from [[investigation-03-the-cold-room]] to [[investigation-04-the-mirror-rig]] that does not cost a scene."}
  - {name: "Silence Is Also An Answer", text: "Maxing silence-it kills the tag. The crew stop reporting to the Desk through this object, they lose the query log permanently, and within a week somebody at a contracts desk notices an account that stopped servicing on a date — which is a page, and pages get bought."}
threats:
  - threat: "The reader gets a handshake and the tag answers with a name, an account number, and the words in good standing."
    consequences:
      - {text: "It answers the crew and it answers everyone else on the same channel (priced-1 on the Escapee Recovery Desk).", statuses: ["priced-1"], tags: []}
      - {text: "One of the PCs' own tags, sitting in their own forearm, answers a broadcast query it should not have been able to hear (that PC takes flagged-2).", statuses: ["flagged-2"], tags: []}
  - threat: "The log is longer than it should be. Somebody has been asking this tag questions for eleven days."
    consequences:
      - {text: "The queries came from outside, through a block's Nearspace, on a credential that was bought rather than cracked (a bought credential).", statuses: [], tags: ["a bought credential"]}
      - {text: "Reading the log tells the log's owner it was read. Escalate the Situation.", statuses: [], tags: []}
  - threat: "The clinic's system prompts, unasked, for a routine warranty check on whoever is holding the reader."
    consequences:
      - {text: "Present a New Challenge: Security Guard (Core p. 305) as clinic security, apologetic, about a flag on an account.", statuses: [], tags: []}
      - {text: "priced-2 on the Escapee Recovery Desk and a clerk asks the crew to wait a moment.", statuses: ["priced-2"], tags: []}
power_sets: []
reuse_of: ""
---

# A Tag Still Answering

**Role:** mystery · **Scale:** 0 · **Alias:** *a bump under the skin of a forearm* · *Something the PCs want to find out, which is not evident and may even be hidden from them* (Core p. 297).

A subdermal AP&I warranty tag, left in a body on purpose after everything else worth money was cut out of it. It is the Job's central clue and its central hazard, and it is a **mystery** rather than a barrier because the difficulty is not getting at it — it is nine centimetres under the skin of a dead runner in a chest freezer — but working out what it means and surviving having asked.

Every Fitted body in Palisade carries one. Every one of them reports. The fitting paperwork disclosed it and nobody has ever read the fitting paperwork (BC-101; [[corp-c]]).

## Limits

| Limit | Tier |
|---|---|
| read the tag | 3 |
| read the query log | 4 |
| silence it | 2 |

## Tags & statuses

still in good standing, eleven days of queries, warranty telemetry

## Specials

**It Reports While It Is Read:** every attempt gives [[escapee-recovery-desk]] `priced-1`; a licensed reader makes it `priced-2`. There is no safe way to read it — the book's third Investigation complication, made mechanical (Core p. 286).

**Whoever Left It Wanted The Ledger Tidy:** reading it establishes without a roll that the killing was incidental and the bookkeeping was not.

**The Query Log:** four searches, eleven days, one rig, in a [[relay-fields]] coffin-block. The clean route to [[investigation-04-the-mirror-rig]].

**Silence Is Also An Answer:** killing the tag costs the log and produces a different page somewhere else.

## Threats / Consequences

› The reader gets a handshake and the tag answers with a name, an account number, and the words *in good standing*.
» It answers everyone else on the channel too (*priced-1* on [[escapee-recovery-desk]])
» A PC's own tag answers a broadcast query it should not have heard (*flagged-2*)

› The log is longer than it should be. Somebody has been asking this tag questions for eleven days.
» Queries from outside, on a credential that was bought and not cracked (*a bought credential*)
» Reading the log tells its owner it was read. Escalate the Situation

› The clinic's system prompts, unasked, for a routine warranty check on whoever is holding the reader.
» Present a New Challenge: **Security Guard** (Core p. 305), apologetic, about a flag on an account
» *priced-2* and a clerk asks the crew to wait a moment

## Power Sets

None.

## Canon and flags

- Warranty telemetry on every Fitted body, the Standing Account, and write-offs that stay on the book at zero value: BC-101, [[corp-c]], [[escapee-recovery-desk]]. The crew on the escapee list without a bounty: Bible §6.
- Splat canon: this profile touches no splat. The second body in the same cold room is an EM kill ([[em-ambush]]) and has no profile here, because nothing in this Job explains it (**[OPEN]** OQ-17) — Bloodware weaknesses are EM and the master node, never sun, fire or a stake (Bible §2).
- **[BUILD CHOICE]** the live-tag method and the query log as the chain's hinge; see [[build-choices]] "Added by WP7b".
