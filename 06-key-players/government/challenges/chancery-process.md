---
type: challenge
name: "The Chancery Process"
slug: chancery-process
status: review
source: custom
page: "294–300, 310"
owner: WP4-trio3
canon_refs: ["Bible §3 power structure", "Bible §6", "Brief §6.3", "Brief §8", "Plan A.6", "Core p. 43", "Core p. 294–300", "Core p. 310"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: barrier
scale: 2
alias: "just paperwork"
short_description: "The registry, the rate card, and the queue: a barrier made of desks, which cannot be fought, cannot be hacked, and gets more expensive the more you want it."
limits:
  - {name: get-the-page, tier: 4}
  - {name: change-the-page, tier: 6}
  - {name: hurt-or-subdue, tier: 999}
  - {name: take-over-or-shut-down, tier: 999}
default_tags: ["a rate card updated quarterly", "the registry is paper", "a queue in the atrium", "two copies of most pages", "a forger in every law firm behind the Hill"]
default_statuses: ["indifferent-3", "referred-onward-2"]
specials:
  - {name: "Not On The Net", text: "The registry is paper, in a basement, because paper cannot be Harnessed ([[chancery-hill]]). Cyberspace actions, Harnessing, hacking, and every take-over-or-shut-down effect are immune. The Nearspace of the Hill swarms with four corporations' data security and none of it touches the shelves. The only ways in are a clerk, a queue, or a door."}
  - {name: "The Price Goes Up", text: "Every time the crew returns to the same clerk about the same page, the price rises by one tier of whatever they are paying in — money, favours, or something they would rather keep. Rolling to intimidate a clerk resets nothing and adds a tier to referred-onward."}
  - {name: "Referred Onward", text: "When referred-onward reaches 4, the matter has been moved to a different bureau in a different building with a different fee, and get-the-page resets. Removing a tier of referred-onward requires a name — a clerk, a minister, a sponsor — not an argument."}
  - {name: "Two Copies", text: "Most pages in the registry exist twice; the copies were separated years ago and reconciled never. Maxing change-the-page alters one copy. Which one, and where the other is, is not knowable from inside the Chancery: a struck name may still be a name somewhere else, and a crew that believes otherwise will find out in someone else's scene."}
  - {name: "A Concurrence Is Sold Separately", text: "Nothing bought here makes anyone lawful. That is a different office, a different fee, and [[halima-boyce]]'s signature — and it can be bought retroactively at a surcharge, which is the fastest-growing line on the rate card."}
threats:
  - threat: "The clerk turns the page around, taps a line on the fee schedule, and waits without impatience."
    consequences:
      - {text: "The fee is more than the crew brought and is not negotiable at this window (blocked-by-a-desk-3).", statuses: ["blocked-by-a-desk-3"], tags: []}
      - {text: "Payment is accepted and the price of the next thing is now known to be higher (add a tier to the pay-in of the crew's choice).", statuses: [], tags: ["the Hill knows what you will pay"]}
  - threat: "\"That is not this bureau.\" A form is stamped and handed back with an address on it."
    consequences:
      - {text: "Add a tier to referred-onward; at 4 the matter starts again in another building (frustrated-2).", statuses: ["frustrated-2"], tags: []}
      - {text: "The referral is itself a record: somebody is now on file as having asked (asked-about-at-the-Hill).", statuses: [], tags: ["asked about at the Hill"]}
  - threat: "The clerk looks up the requester before looking up the request."
    consequences:
      - {text: "The crew's own page is read back to them — the escapee list, the outstanding matter, the name they used last month (exposed-on-paper-3).", statuses: ["exposed-on-paper-3"], tags: []}
      - {text: "Escalate the Situation: within the day, whoever else has an account with this clerk is told who was asking.", statuses: [], tags: []}
  - threat: "A page is produced from the shelf with two seals on it, in different inks."
    consequences:
      - {text: "The document the crew came for is real and so is the other one; the crew now holds evidence that Palisade's record disagrees with itself (a page that should not exist).", statuses: [], tags: ["a page that should not exist"]}
      - {text: "The clerk sees them see it, and the price of everything from this window doubles for the rest of the Series (Make the Future Bleaker).", statuses: [], tags: []}
  - threat: "A permit-assistance kiosk at the lower gate offers to solve the whole problem this afternoon."
    consequences:
      - {text: "A forgery indistinguishable from real paper, because the real paper was bought too — and it will pass everywhere except in front of the person who filed the original (a forged Chancery seal).", statuses: [], tags: ["a forged Chancery seal"]}
      - {text: "Present a New Challenge: Envelope Detail, who were told about the kiosk's customers before the ink dried.", statuses: [], tags: []}
power_sets: []
reuse_of: "Structurally a Location/Barrier in the Crumbling Building and Hazard Zone pattern (Core p. 310) with navigate replaced by get-the-page; clerks and officials use Shady Tech Merchant (Core p. 303) and Corporate Executive (Core p. 304)."
---

# The Chancery Process

**Role:** barrier · **Scale:** 2 (an institution and its basement) · **Alias:** *just paperwork* · *The registry, the rate card, and the queue.*

Five floors of stone around a glass atrium, the registry in the basement, the council chamber under the dome, the police command in an annex bolted on the back ([[chancery-hill]]). A Seat of Power in the book's sense (Core p. 43) and a Marketplace in every other: the atrium is where the Foot queues with envelopes, and the rate card is updated quarterly.

This Challenge is the government as an obstacle. It is not hostile — nobody here has any feeling about the crew at all — and that is what makes it a barrier rather than a foe. It cannot be shot, threatened usefully, or hacked, because the thing the crew needs is a piece of paper on a shelf in a room, held by a person who has already been paid by somebody else this month, and the only currencies are money, names, and patience.

It is also, quietly, the most dangerous room in Palisade to be *noticed* in, because everything the Chancery does leaves a record, and everyone who matters has an account with somebody in the building.

## Limits

| Limit | Tier |
|---|---|
| get the page | 4 |
| change the page | 6 |
| hurt or subdue | – (immune) |
| take over or shut down | – (immune; see *Not On The Net*) |

## Tags & statuses

a rate card updated quarterly · the registry is paper · a queue in the atrium · two copies of most pages · a forger in every law firm behind the Hill · *indifferent-3* · *referred-onward-2*

## Specials

**Not On The Net:** The registry is paper in a basement because paper cannot be Harnessed. Cyberspace, Harnessing, and hacking do nothing; the Hill's four overlapping corporate security nimbuses do not touch the shelves. The ways in are a clerk, a queue, or a door.

**The Price Goes Up:** Each return to the same clerk about the same page raises the price by one tier of whatever the crew pays in. Intimidation resets nothing and adds a tier to *referred onward*.

**Referred Onward:** At *referred-onward-4* the matter is now in a different bureau in a different building with a different fee, and *get the page* resets. Removing a tier takes a name, not an argument.

**Two Copies:** Most pages exist twice and were never reconciled. Maxing *change the page* alters one copy. Which one — and where the other is — cannot be learned inside the Chancery.

**A Concurrence Is Sold Separately:** Nothing bought here makes anyone lawful. That is [[halima-boyce]]'s office, a separate fee, and available retroactively at a surcharge.

## Threats / Consequences

› The clerk turns the page around, taps the fee schedule, and waits without impatience.
» More than the crew brought, and not negotiable at this window (*blocked-by-a-desk-3*)
» Paid — and the Hill now knows what they will pay (*the Hill knows what you will pay*)

› "That is not this bureau." A form is stamped and handed back with an address on it.
» A tier to *referred onward* (*frustrated-2*)
» The referral is a record; somebody asked (*asked about at the Hill*)

› The clerk looks up the requester before looking up the request.
» Their own page read back to them (*exposed-on-paper-3*)
» Escalate the Situation: whoever else has an account with this clerk is told

› A page comes off the shelf with two seals on it, in different inks.
» Evidence that Palisade's record disagrees with itself (*a page that should not exist*)
» The clerk sees them see it; every price from this window doubles (Make the Future Bleaker)

› A permit-assistance kiosk at the lower gate offers to solve the whole thing this afternoon.
» A forgery indistinguishable from real paper (*a forged Chancery seal*)
» Present a New Challenge: [[envelope-detail]], told about the kiosk's customers before the ink dried

## Power Sets

None. Individual officials take **Connected & Protected** (Core p. 328) or **In The Know** (Core p. 329).

## Canon and flags

- Deeply corrupt government, kleptocratic bureaucracy, forged paper, the paper registry, and the escapee lists: Bible §3, §6; Brief §6.3; [[chancery-hill]] (BC-17).
- **[BUILD CHOICE]** (BC-122) *Two Copies* and the separately-sold concurrence.
- **[OPEN]** (OQ-8, OQ-21) the papers here are permits, leases, licences, and lists; nothing in this Challenge makes caste legal. **[OPEN]** (OQ-10) nothing in the registry answers where the crew leader was caught, and no roll against this Challenge can produce it.
