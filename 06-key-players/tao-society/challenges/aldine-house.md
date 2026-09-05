---
type: challenge
name: "Aldine House"
slug: aldine-house
status: review
source: custom
page: "294–300, 43"
owner: WP4-trio3
canon_refs: ["Bible §2 mage", "Bible §3 power structure", "Bible §3 Masquerade", "Brief §3.1–3.2", "Brief §4.1", "Brief §8", "Core p. 43", "Core p. 294–300", "Tokyo p. 151–158"]
flags: [BUILD CHOICE, TAO-REINTERPRETED, OPEN]
player_safe: false
role: temptation
scale: 1
alias: "a members' club and cultural foundation"
short_description: "The Wuji's respectable front: a library, a garden, a morning practice, and an offer that is real — where being seen inside is the price and the reward."
limits:
  - {name: accept-the-offer, tier: 3}
  - {name: refuse-and-stay-findable, tier: 5}
  - {name: search-the-house, tier: 6}
  - {name: hurt-or-subdue, tier: 999}
default_tags: ["impeccable respectability", "the Long Room, where nothing is loud", "a minister on the board", "a garden of raked gravel and one old tree", "no terminals anywhere", "the Quiet Hand joke"]
default_statuses: ["welcoming-3", "watched-without-cameras-2"]
specials:
  - {name: "Nobody Is Thrown Out", text: "The House has no guards, no checkpoint, and no alarm, and it never refuses entry to anyone who was invited or brought. It is immune to hurt-or-subdue and to every intrusion Limit that assumes a hostile door. Violence inside the House is possible and is answered with apology, a doctor, a settlement, and the permanent closure of every door in Palisade that the House can reach."}
  - {name: "The Offer Is Real", text: "Whatever the House offers a PC — a scholarship, a place, a debt cleared, a room for a friend who is in trouble — is genuine, arrives without conditions, and is not withdrawn. Nothing is asked for months. This is the temptation: not a trick, a gift."}
  - {name: "Being Seen Here Counts", text: "Anyone who spends a scene inside the House gains the story tag seen at Aldine House. It opens doors on Chancery Hill that are shut to Patched crews and closes doors under the Wall that were open, and every Key Player with a floor on the Hill hears about it within a week."}
  - {name: "The Morning Practice", text: "A PC who attends the practice in the garden three times may, at the MC's cue, be shown one thing about their own discipline, item, or body that nobody has ever explained to them. Nothing is asked in return at the time. The House does not teach anyone who has not been offered a place."}
  - {name: "A Refusal Is Not a No", text: "When a PC declines an offer, remove welcoming and add a tier to refuse-and-stay-findable. Each further refusal adds another. When it maxes, the House has finished: the PC's records are tidy, their contacts have moved on, their clinic has a new owner, and a very good opportunity exists in another district. Take a permanent story tag such as quietly closed out of the Crest."}
threats:
  - threat: "A letter arrives on paper, addressed correctly, offering a place. There is no interview and no conditions."
    consequences:
      - {text: "The offer is better than anything the crew has been paid all year and it does not expire (tempted-3).", statuses: ["tempted-3"], tags: []}
      - {text: "The letter names something the PC did that nobody was supposed to have seen (Escalate the Situation).", statuses: [], tags: ["the House saw it"]}
  - threat: "The Steward invites the crew to sit in the Long Room, and the door closes on a silence that is deeper than the room should be able to hold."
    consequences:
      - {text: "The conversation goes exactly as the House wants and nobody can say afterwards why they agreed (convinced-3).", statuses: ["convinced-3"], tags: []}
      - {text: "Whatever the crew brought in — a device, a recording, a wire — does not work in this room and is not working when they leave either (burn a tag representing a recording or a transmitter).", statuses: [], tags: []}
  - threat: "A member the crew recognizes from somewhere else entirely — a Chancery office, an Orison floor, a Suture Row surgery — nods at them across the garden."
    consequences:
      - {text: "The crew learns that the House's membership reaches into a place they were about to work (Escalate the Situation).", statuses: [], tags: []}
      - {text: "The House learns the same thing about the crew, faster (noticed by the House).", statuses: [], tags: ["noticed by the House"]}
  - threat: "Somebody asks, pleasantly, what the crew is looking for in the library, and offers to help them find it."
    consequences:
      - {text: "The librarian is genuinely helpful about everything except one subject, and the crew cannot tell which subject that was (Deny Them Something They Want).", statuses: [], tags: []}
      - {text: "Present a New Challenge: Wuji Operative, who was already in the building and offers to buy whatever the crew came for.", statuses: [], tags: []}
  - threat: "After a refusal, nothing happens for a week. Then a landlord is polite, and a fixer does not answer, and a very good job in another district is mentioned by three different people."
    consequences:
      - {text: "Add a tier to refuse-and-stay-findable; the crew loses a contact, a room, or a line of credit (a door closed with no hand on it).", statuses: [], tags: ["a door closed with no hand on it"]}
      - {text: "When the Limit maxes: quietly closed out of the Crest, permanently, and the House sends flowers.", statuses: [], tags: ["quietly closed out of the Crest"]}
power_sets: []
reuse_of: "Structurally the Thin Place Shrine's role as a place that changes people (Core p. 311), stripped of every mystical property [TAO-REINTERPRETED]; the House is a building, and what happens in it is people."
---

# Aldine House

**Role:** temptation · **Scale:** 1 (a house and its membership) · **Alias:** *a members' club and cultural foundation* · *The Wuji's respectable front: a library, a garden, a morning practice, and an offer that is real.*

Three storeys of pale brick behind a wall and a gate on the north side of [[chancery-hill]] (BC-19). A garden of raked gravel and one old tree. A recital hall. A library whose reading room — the **Long Room** — is the quietest place on the Wall, with no terminals in it, because members do not bring devices. A minister of [[government|the Chancery]] on the board. And, every morning before dawn, forty people in grey moving slowly in the garden, taught by an instructor who is never quite the same person twice.

It is the safest building in Palisade to be inside and the most expensive one to have entered. The House has no guards and does not need them: it is protected by being unremarkable, by a century of favours, and by the Quiet Hand joke, which does more for it than a denial ever could ([[chancery-hill]]; Brief §4.1). Its danger to a crew is not injury. It is that the House will give them something they need, at a moment when nobody else will, and then simply wait.

**[TAO-REINTERPRETED]** (CR-1) The Long Room is not a Thin Place and this file does not say Tao runs dense anywhere — **[OPEN]** (OQ-14). Members find the practice easier to hold in that room; members also believe a great many things about the House. The book's Thin Place Shrine (Core p. 311) is the structural ancestor of this profile and every mystical property of it has been removed: no aura, no Source, no worshippers, no allegiance sworn to anything.

## Limits

| Limit | Tier |
|---|---|
| accept the offer | 3 (progress — the crew's, not the House's) |
| refuse and stay findable | 5 (progress — maxes into *quietly closed out of the Crest*) |
| search the House | 6 |
| hurt or subdue | – (immune; see *Nobody Is Thrown Out*) |

## Tags & statuses

impeccable respectability · the Long Room, where nothing is loud · a minister on the board · a garden of raked gravel and one old tree · no terminals anywhere · the Quiet Hand joke · *welcoming-3* · *watched-without-cameras-2*

## Specials

**Nobody Is Thrown Out:** No guards, no checkpoint, no alarm, and no refusal of entry to anyone invited or brought. Immune to *hurt or subdue* and to every intrusion Limit that assumes a hostile door. Violence inside is answered with apology, a doctor, a settlement, and the permanent closing of every door on the Crest the House can reach.

**The Offer Is Real:** Whatever the House offers is genuine, unconditional, and not withdrawn, and nothing is asked for months. The temptation is a gift, not a trick.

**Being Seen Here Counts:** A scene inside the House gives the story tag *seen at Aldine House* — it opens Crest doors that are shut to Patched crews, closes doors under the Wall that were open, and is known to every Key Player with a floor on the Hill within a week.

**The Morning Practice:** Attend three times and the House may show a PC one thing about their own discipline, item, or body that nobody has ever explained to them. Nothing is asked at the time. The House does not teach anyone who has not been offered a place.

**A Refusal Is Not a No:** Each refusal removes *welcoming* and adds a tier to *refuse and stay findable*. Maxed, the House has finished: records tidy, contacts moved on, a very good opportunity in another district — *quietly closed out of the Crest*.

## Threats / Consequences

› A letter arrives on paper, correctly addressed, offering a place. No interview, no conditions.
» Better than anything the crew has been paid all year, and it does not expire (*tempted-3*)
» It names something the PC did that nobody was supposed to have seen (*the House saw it*; Escalate the Situation)

› The Steward invites them into the Long Room and the door closes on a silence deeper than the room should hold.
» The conversation goes as the House wants and nobody can say why they agreed (*convinced-3*)
» What they brought in does not work in this room, or afterwards (burn a recording or transmitter tag)

› A member they recognize from a Chancery office, an Orison floor, or a Suture Row surgery nods across the garden.
» The crew learns the House reaches into a place they were about to work (Escalate the Situation)
» The House learns the same about them, faster (*noticed by the House*)

› Somebody asks pleasantly what they are looking for in the library and offers to help.
» Helpful about everything except one subject, and they cannot tell which (Deny Them Something They Want)
» Present a New Challenge: [[wuji-operative-challenge]], already in the building, offering to buy

› After a refusal, nothing happens for a week — then a landlord is polite and a fixer does not answer.
» A tier to *refuse and stay findable*; a contact, a room, or a line of credit is gone (*a door closed with no hand on it*)
» Maxed: *quietly closed out of the Crest*, and the House sends flowers

## Power Sets

None. The House has no powers; its members do — see [[wuji-operative-challenge]].

## Canon and flags

- The society recruits the talented and hides itself; the corporations prefer that (Bible §2, §3). Aldine House as the respectable Crest front is BC-19 (WP1); this file gives it rules.
- **[BUILD CHOICE]** (BC-120) the House as a temptation whose gifts are genuine and whose refusals close doors instead of breaking bones; (BC-118) the name *the Long Room*.
- **[TAO-REINTERPRETED]** (CR-1) the Thin Place Shrine's structure with all mystical properties removed; no worship, no allegiance, nothing with a will.
- **[OPEN]** (OQ-14) the Long Room is written as belief, never as a Tao-dense place. **[OPEN]** (OQ-6) nobody inside says *Tao* aloud.
