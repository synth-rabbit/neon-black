---
type: challenge
name: First Alms
slug: first-alms
status: review
source: custom
page: "294–300, 306"
owner: WP4-trio2
canon_refs: ["Bible §2 werewolf", "Bible §3 power structure", "Bible §4 theme 3", "Bible §5", "Brief §8", "Core p. 294–300", "Core p. 306", "Core p. 329"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: temptation
scale: 0
alias: "the office"
short_description: "Two rooms above a shipping agent, a kettle, and a filing cabinet: the First Almoner will buy anything the crew has, including their future, and will spend the Run to keep one contract unread."
limits:
  - {name: refuse-the-terms, tier: 4}
  - {name: find-the-contract, tier: 6}
  - {name: hurt-or-subdue, tier: 2}
default_tags: ["reads paper for a living", "owns the district's debts", "no security in the building", "a kettle and two chairs"]
default_statuses: ["unhurried-3"]
specials:
  - {name: "Everything Is Priced", text: "First Alms never refuses a request and never grants one. She counters. Any ask the crew makes comes back as terms — a favor, a tab, a name, a job at the Round's edge — and the terms are always achievable and always cost more than they look. Refuse-the-terms is polar: maxing it ends the negotiation for the Series and converts the crew into a line item."}
  - {name: "The Collateral Walks", text: "First Alms has no muscle of her own and never needs any. As a Consequence, in any district where the Almoners lend, she can call the tab on somebody who owes — and what arrives is not hers. Present a New Challenge: [[pack-on-the-run]], [[almoners-volunteer]], or a Syndicate Leg-Breaker (Core p. 307), and note that the person who came did not want to."}
  - {name: "The Contract Is Not Here", text: "Find-the-contract is tier 6 and cannot take tiers in this scene, in this building, or from her. The supply application and its renewals are lodged with the Chancery's clinic registry and with the vendor ([[corp-a]]); the crew has to go and get one of those copies. She will say so, calmly, if asked, because it is true and because saying it is the cheapest way to make the errand look impossible."}
  - {name: "She Would Rather Be Sold", text: "If the crew brings her leverage that would end the Almoners — the contract, the ledger's structure, a Chancery officer who cannot be bought — she does not fight it. She offers to sell the book to whoever the crew is working for, on terms, and asks them to carry the message. Escalate the Situation; the Series now has a lender changing hands ([[upstart]])."}
threats:
  - threat: "She fills the kettle before she sits down, and asks the crew what they are owed."
    consequences:
      - {text: "She is genuinely willing to pay it, and says a number that is more than the crew expected.", statuses: ["tempted-3"], tags: []}
      - {text: "She already knows what they are owed, by whom, and what they did to be owed it.", statuses: ["exposed-2"], tags: []}
  - threat: "She takes a pencil and begins writing terms on the back of a shipping docket."
    consequences:
      - {text: "The terms are fair, achievable, and structured so the first payment costs nothing.", statuses: ["obligated-3"], tags: ["on the Almoners' paper"]}
      - {text: "One clause names a person the crew cares about as security. She will remove it if asked, and remember that they asked.", statuses: [], tags: ["they named your people"]}
  - threat: "She mentions, without emphasis, a district where the price of the dose has not gone up this month."
    consequences:
      - {text: "A kennel in [[cinder-yards]] is told the crew are the reason it is going up. Present a New Challenge: [[pack-on-the-run]].", statuses: [], tags: ["the packs blame you"]}
      - {text: "A pack that has been useful is rewarded at the crew's expense — a door opened, a name sold, a route given away.", statuses: [], tags: ["somebody was told where you sleep"]}
  - threat: "She looks at the filing cabinet, once, and then does not look at it again."
    consequences:
      - {text: "The cabinet holds twenty years of renewals and nothing incriminating. Deny Them Something They Want.", statuses: [], tags: []}
      - {text: "Within a day, the clinic's paperwork is copied, split, and lodged in three places. Add one tier to find-the-contract's difficulty for the rest of the Series (the MC may instead reset any statuses on it).", statuses: [], tags: ["the paperwork has moved"]}
power_sets: []
reuse_of: "Built beside Criminal Overlord (Core p. 306), with the Overlord's bodyguards and home-field jamming deliberately removed; In The Know Power Set, Core p. 329."
---

# First Alms

**Role:** temptation · **Scale:** 0 · **Alias:** *the office* · *The First Almoner will buy anything the crew has, and will spend the Run to keep one contract unread.*

The person is [[halina-ansah]]. This profile is the scene in the two rooms above the shipping agent's office at the shore end of [[gullet-market]] — a window onto the locks, a filing cabinet, a kettle, two chairs, and no security anywhere in the building.

She is built beside the book's **Criminal Overlord** (Core p. 306) with the Overlord's two signature features taken away: she has no bodyguards and no jammed home ground. She does not need them, and the absence is the point. The dangerous thing in the room is the pencil.

## Limits

| Limit | Tier |
|---|---|
| refuse the terms | 4 |
| find the contract | 6 |
| hurt or subdue | 2 |

## Tags & statuses

reads paper for a living, owns the district's debts, no security in the building, a kettle and two chairs · *unhurried-3*

## Specials

**Everything Is Priced:** She never refuses and never grants; she counters. Terms are always achievable and always cost more than they look. *Refuse the terms* is polar — maxing it ends the negotiation for the Series and turns the crew into a line item.

**The Collateral Walks:** She has no muscle. As a Consequence, in any district where the Almoners lend, she calls a tab, and what arrives is not hers — Present a New Challenge: [[pack-on-the-run]], [[almoners-volunteer]], or Syndicate Leg-Breaker (Core p. 307). Whoever came did not want to.

**The Contract Is Not Here:** *Find the contract* takes no tiers in this scene, in this building, or from her. The supply application and its renewals sit with the Chancery's clinic registry and with the vendor ([[corp-a]]). She will say so if asked, because it is true and because it makes the errand look impossible.

**She Would Rather Be Sold:** Bring her leverage that would end the Almoners and she does not fight it — she offers to sell the book to whoever the crew works for, on terms, and asks them to carry the message (Escalate the Situation; see [[upstart]]).

## Threats / Consequences

› She fills the kettle before she sits down, and asks the crew what they are owed.
» She is willing to pay it, and says a number that is more than expected (*tempted-3*)
» She already knows what they are owed, by whom, and what they did to be owed it (*exposed-2*)

› She takes a pencil and begins writing terms on the back of a shipping docket.
» The terms are fair, achievable, and the first payment costs nothing (*obligated-3*, *on the Almoners' paper*)
» One clause names somebody the crew cares about as security; she will remove it if asked, and remember that they asked (*they named your people*)

› She mentions, without emphasis, a district where the price of the dose has not gone up this month.
» A kennel is told the crew are the reason it is going up (Present a New Challenge: [[pack-on-the-run]]; *the packs blame you*)
» A pack that has been useful is rewarded at the crew's expense (*somebody was told where you sleep*)

› She looks at the filing cabinet, once, and then does not look at it again.
» The cabinet holds twenty years of renewals and nothing incriminating (Deny Them Something They Want)
» Within a day the paperwork is copied, split, and lodged in three places (*the paperwork has moved*)

## Power Sets

**In The Know** (Core p. 329) — she is the best-informed person under the Wall about who owes what. Explicitly **not** Connected & Protected: the Almoners' whole design is that they have no protection worth the name.

## Canon and flags

- Bible §2, §3, §4 theme 3, §5; Brief §8. Built beside Criminal Overlord (Core p. 306) with bodyguards and jamming removed.
- **[BUILD CHOICE]** (BC-109) the profile, *find the contract* at tier 6 as the mechanical form of the twist, and *She Would Rather Be Sold* as the Continuity hook.
- **[OPEN]** (OQ-18) her business beyond lending and the Leash trade; **[OPEN]** (OQ-17) untouched.
