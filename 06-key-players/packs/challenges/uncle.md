---
type: challenge
name: Uncle
slug: uncle
status: review
source: custom
page: "294–300, 306"
owner: WP4-trio2
canon_refs: ["Bible §2 werewolf", "Bible §3 haves and have-nots", "Bible §4 themes 1 and 3", "Brief §2.5 werewolf", "Brief §8", "Core p. 294–300", "Core p. 297", "Core p. 306", "Core p. 329"]
flags: [BUILD CHOICE]
player_safe: false
role: temptation
scale: 0
alias: "everybody's uncle"
short_description: "The Nineteens' recruiter, working a courtyard on the worst day of somebody's week: a body on credit, the chrome arranged, and the first dose free."
limits:
  - {name: hurt-or-subdue, tier: 3}
  - {name: refuse-him-in-front-of-people, tier: 4}
  - {name: make-him-hear-himself, tier: 5}
default_tags: ["knows your mother's name", "carries the shopping up eleven floors", "the money is already arranged", "a cousin who will vouch"]
default_statuses: ["settled-1", "sincere-3"]
specials:
  - {name: "He Means It", text: "Uncle is not lying and cannot be caught in a lie, because he believes every word. Actions that would expose a con, a scam, or a hidden motive find nothing. Make-him-hear-himself is tier 5 and takes tiers only from the consequences of his own recruiting made concrete in front of him — a kid he brought in, gone wrong; a mother; a name in a ledger; a body that did not settle."}
  - {name: "The Offer", text: "Once per scene, as a Consequence, Uncle makes the offer to a PC or to somebody the PC cares about: the sculpt on credit through [[syndicate|the Almoners]], the anchors from a Row chop-shop with no records, four months of healing among people who will feed you, and the first dose free. Give the target tempted-3. If the PC's own theme motivation pulls toward it — climbing, belonging, a body that works — the status is compelling."}
  - {name: "Refusing Him Is Public", text: "Uncle only ever makes the offer where people can see. Refuse-him-in-front-of-people is polar: maxing it costs the PC standing in [[marlow-blocks]] (unwelcome-3) unless they can give the courtyard a better answer than his, which nobody in the Blocks has ever had."}
  - {name: "One Tier Of Dose", text: "He carries his own, and it is a tier, not three: settled-1. He can spend it and become the shape for one exchange (see [[running-shape]]), and he will, because the Nineteens' standing is the only thing he has. Afterward he takes coming-apart-3 and has to be walked home."}
threats:
  - threat: "He crosses the courtyard with two bags of somebody else's shopping and greets a PC by name, warmly, with a detail nobody outside the Blocks could know."
    consequences:
      - {text: "The crew's business in Marlow is now a thing the Nineteens are aware of.", statuses: ["marked-2"], tags: []}
      - {text: "He asks after somebody the crew cares about, by name, without any threat in it at all.", statuses: ["unsettled-2"], tags: ["he knows your people too"]}
  - threat: "He sits down on the step next to somebody who has had a bad week and does not say anything for a while."
    consequences:
      - {text: "The offer, made kindly, at the worst possible moment.", statuses: ["tempted-3"], tags: []}
      - {text: "A kid from the courtyard says yes. Nothing in the scene stops it; it goes in the ledger tonight and on a table in eleven days.", statuses: [], tags: ["another name in the Kitchen's ledger"]}
  - threat: "He explains what the pack did for him, and it is the truest thing anyone says in the scene."
    consequences:
      - {text: "The argument lands on anyone who came up under the Wall.", statuses: ["doubt-3"], tags: []}
      - {text: "He offers the crew a floor in Block Nineteen, a name at the Kitchen, and an introduction to the alpha — three favors, and then a ledger line.", statuses: ["obligated-2"], tags: []}
  - threat: "He stops smiling, rolls his sleeve, and shows the crew the back of his hand."
    consequences:
      - {text: "He spends his tier (gain [[running-shape]], settled-1) and closes.", statuses: [], tags: []}
      - {text: "The stairwell fills behind him. Present a New Challenge: [[pack-on-the-run]], Scale 1, the Nineteens.", statuses: [], tags: []}
power_sets: [running-shape]
reuse_of: "Built beside Gang Member (Core p. 306) with the role changed to temptation (Core p. 297); In The Know (Core p. 329) for the courtyard gossip."
---

# Uncle

**Role:** temptation · **Scale:** 0 · **Alias:** *everybody's uncle* · *A body on credit, the chrome arranged, and the first dose free.*

The person is [[jarek-kovac]]. This is the profile for the courtyards, stairwells, and school gates of [[marlow-blocks]], where [[packs|the Run]] recruits.

He is a **temptation** (Core p. 297), which is the whole design: the danger Uncle poses is not that he will hurt the crew but that he is offering, sincerely and for free, the only route up that anybody in the Blocks has ever been offered — and that the price is a body you can never give back and a counter you pay for the rest of your life ([[syndicate]], [[corp-a]]). He is also a Howler, and if the scene goes badly enough he will spend his one tier of dose on it.

## Limits

| Limit | Tier |
|---|---|
| hurt or subdue | 3 |
| refuse him in front of people | 4 |
| make him hear himself | 5 |

## Tags & statuses

knows your mother's name, carries the shopping up eleven floors, the money is already arranged, a cousin who will vouch · *settled-1*, *sincere-3*

## Specials

**He Means It:** He cannot be caught in a lie because there is not one. *Make him hear himself* takes tiers only from his own recruiting made concrete in front of him — a kid gone wrong, a mother, a name in a ledger, a body that did not settle.

**The Offer:** Once per scene, as a Consequence, to a PC or to somebody they care about: the sculpt on credit, anchors with no records, four months of healing among people who will feed you, the first dose free. *Tempted-3* — compelling if the PC's own motivation pulls toward climbing, belonging, or a body that works.

**Refusing Him Is Public:** He only offers where people can see. *Refuse him in front of people* is polar; maxing it costs *unwelcome-3* in [[marlow-blocks]] unless the crew can give the courtyard a better answer than his.

**One Tier Of Dose:** He carries *settled-1*, not three. He can spend it for one exchange ([[running-shape]]) and will. Afterward: *coming-apart-3*, and somebody has to walk him home.

## Threats / Consequences

› He crosses the courtyard with two bags of somebody else's shopping and greets a PC by name, with a detail nobody outside the Blocks could know.
» The crew's business in Marlow is now the Nineteens' business (*marked-2*)
» He asks after somebody the crew cares about, with no threat in it at all (*unsettled-2*, *he knows your people too*)

› He sits down on the step next to somebody who has had a bad week and does not say anything for a while.
» The offer, made kindly, at the worst possible moment (*tempted-3*)
» A kid from the courtyard says yes (*another name in the Kitchen's ledger*)

› He explains what the pack did for him, and it is the truest thing anyone says in the scene.
» The argument lands on anyone who came up under the Wall (*doubt-3*)
» Three favors — a floor, a name, an introduction — and then a ledger line (*obligated-2*)

› He stops smiling, rolls his sleeve, and shows the crew the back of his hand.
» He spends his tier and closes (gain [[running-shape]], *settled-1*)
» The stairwell fills behind him (Present a New Challenge: [[pack-on-the-run]], Scale 1, the Nineteens)

## Power Sets

[[running-shape]] at *settled-1* only, and only when the offer has failed badly.

## Canon and flags

- Bible §2 (how a Howler is made; the syndicate's credit and supply; rarity — the Nineteens are eleven people), §3 (unequal access; the Masquerade), §4 themes 1 and 3; Brief §2.5, §8; roles per Core p. 297.
- **[BUILD CHOICE]** (BC-110, BC-112) the recruiter as a temptation, *The Offer*, and the public-refusal Limit.
- Splat canon (Plan A.6): a Howler, dependent on the [[syndicate|Almoners']] dose, irreversibly sculpted; no Tao.
