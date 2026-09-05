---
type: challenge
name: "Product Integrity Recovery Team"
slug: product-integrity-team
status: review
source: custom
page: "294–300, 304–307, 328"
owner: WP4-trio3
canon_refs: ["Bible §2 mage", "Bible §3 power structure", "Brief §8", "Plan A.6", "Core p. 294–300", "Core p. 304", "Core p. 328"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: pursuer
scale: 1
alias: "Orison contracts, returning company property"
short_description: "Orison's trade-secret enforcers: a four-person crew in matte grey who buy first, take second, and never open the case."
limits:
  - {name: hurt-or-subdue, tier: 4}
  - {name: outrun-or-lose, tier: 4}
  - {name: buy-off, tier: 5}
  - {name: discredit, tier: 3}
default_tags: ["Orison hardware, correctly maintained", "settlement authority in the field", "an itemized recovery manifest", "gloves and a sealed case"]
default_statuses: ["patient-2", "jurisdiction-arranged-2"]
specials:
  - {name: "Never Opens the Case", text: "This crew will not open, scan, or photograph the item it is recovering, and will not permit anyone else to. If an action would reveal the contents of a sealed Orison case, the team first delivers a Consequence to prevent it, even at cost to itself — it will take a status rather than let a case be read."}
  - {name: "Buy First", text: "The first time the team engages the crew in a scene, it opens with an offer instead of an attack: a settlement, a contract, a debt bought out, a name struck off a list. While the offer stands, its hurt-or-subdue Limit is unavailable to the PCs, because nobody has drawn yet. If any PC accepts, the team leaves and the buy-off Limit is maxed for the rest of the job."}
  - {name: "Jurisdiction Arranged", text: "The team's paperwork was filed before it arrived (Bible §3: corporate security is exactly as legal as the city police). Chancery police who arrive at the scene treat the team as the lawful party and the PCs as the incident. Removing jurisdiction-arranged-2 requires action at the Chancery, not at the scene."}
  - {name: "No Report Was Filed", text: "Product Integrity does not use the courts and does not want the record. If the team is beaten, nothing is reported, no bounty is posted, and no name reaches the Chancery — the crew instead gains the story tag an unresolved matter with Orison, and the team comes back with one more member and a better arrangement."}
threats:
  - threat: "A grey-suited woman puts a case on the table, slides a folded page across, and says the company would like to close this out today."
    consequences:
      - {text: "The offer is good and it is the last one: money, a debt cleared, a name off a list — and an obligation that outlives the job.", statuses: ["solvent-2"], tags: ["owned by an Orison settlement"]}
      - {text: "The offer is withdrawn and the team stops speaking. Everyone in the room understands what happens next.", statuses: ["threatened-2"], tags: []}
  - threat: "Two of them move to the doorways without hurrying while the third keeps talking."
    consequences:
      - {text: "The exits are held by people who are better at this than the crew (cornered-3).", statuses: ["cornered-3"], tags: []}
      - {text: "Suppressed fire from correctly maintained Orison weapons, aimed to stop rather than to kill (pinned-down-3 or gunshot-wound-3).", statuses: ["pinned-down-3"], tags: []}
  - threat: "A hand in a glove reaches for the case and does not look away from it."
    consequences:
      - {text: "The item is recovered, sealed, and gone; the crew has nothing to sell and nothing to prove (Deny Them Something They Want).", statuses: [], tags: []}
      - {text: "If a PC is holding the item, they are taken with it as far as the door (grappled-3), and the team still does not open the case.", statuses: ["grappled-3"], tags: []}
  - threat: "The auditor reads the crew's names off a wrist holo, in order, with middle names."
    consequences:
      - {text: "Product Integrity's contract arm has already bought the crew's landlord, their fixer's debt, or their clinic's account (in-the-company-books-3).", statuses: ["in-the-company-books-3"], tags: []}
      - {text: "Escalate the Situation: the team hands the crew's file to whoever else was already looking for them.", statuses: [], tags: []}
  - threat: "A Chancery patrol pulls up outside and the team's auditor walks out to meet it, unhurried."
    consequences:
      - {text: "The police take the team's account as the record. Present a New Challenge: Security Guard as police, Scale 1 (Core p. 305), or [[envelope-detail]] if the crew is under the Wall.", statuses: [], tags: ["the report already says what happened"]}
power_sets: []
reuse_of: "Built on Security Guard (Core p. 305) and Corporate Executive's Bodyguards logic (Core p. 304); pairs with Connected & Protected and Heavily Armed (Core p. 328)."
---

# Product Integrity Recovery Team

**Role:** pursuer · **Scale:** 1 (a four-person crew) · **Alias:** *Orison contracts, returning company property* · *Orison's trade-secret enforcers: they buy first, take second, and never open the case.*

The department is real, its budget has doubled in two years, and its staff believe they are protecting a finishing process. Four people: an auditor who talks, two who move to the doors, and a driver who stays with the vehicle and the second case. Matte grey, gloved, unhurried, apologetic. They carry Orison hardware that is correctly maintained, which on the street is rarer than good hardware, and they have settlement authority in the field, which is rarer still.

What makes them frightening is not the guns. It is that they arrive already knowing the crew's landlord, and that they have decided in advance which force will be the lawful one in this room ([[government|the Chancery]], the Office of Concurrent Jurisdiction). What makes them *interesting* is the one thing they will not do: look inside the case they came for. They do not know why the rule exists. They enforce it as though their lives depended on it, and — since the alternative is [[adaeze-ferreira]] finding out they broke it — they are not wrong.

## Limits

| Limit | Tier |
|---|---|
| hurt or subdue | 4 |
| outrun or lose | 4 |
| buy off | 5 |
| discredit | 3 |

*Buy off* is high because they have the budget and the patience; *discredit* is low because Product Integrity cannot survive a public argument and knows it.

## Tags & statuses

Orison hardware, correctly maintained · settlement authority in the field · an itemized recovery manifest · gloves and a sealed case · *patient-2* · *jurisdiction-arranged-2*

## Specials

**Never Opens the Case:** The team will not open, scan, or photograph what it is recovering, and will not let anyone else. If an action would reveal a sealed Orison case's contents, the team delivers a Consequence first to prevent it, accepting a status rather than allowing a reading.

**Buy First:** The first engagement in a scene opens with an offer, not an attack — a settlement, a contract, a debt bought, a name struck. While the offer stands, *hurt or subdue* is unavailable to the PCs. Acceptance ends the encounter and maxes *buy off* for the job.

**Jurisdiction Arranged:** The paperwork was filed before they arrived. Chancery police treat the team as the lawful party and the crew as the incident (Bible §3). *jurisdiction-arranged-2* is removed at the Chancery, not at the scene.

**No Report Was Filed:** Beat them and nothing is reported and no bounty posted; the crew gains the story tag *an unresolved matter with Orison*, and the team returns larger and better arranged.

## Threats / Consequences

› A grey-suited woman puts a case on the table and slides a folded page across.
» The offer is good and it is the last one (*solvent-2*; *owned by an Orison settlement*)
» The offer is withdrawn and the talking stops (*threatened-2*)

› Two of them take the doorways without hurrying while the third keeps talking.
» The exits are held by people better at this than the crew (*cornered-3*)
» Suppressed fire, aimed to stop (*pinned-down-3* or *gunshot-wound-3*)

› A gloved hand reaches for the case and does not look away from it.
» The item is recovered, sealed, gone (Deny Them Something They Want)
» A PC holding it goes as far as the door with it (*grappled-3*) — and the case stays shut

› The auditor reads the crew's names off a wrist holo, with middle names.
» Their landlord, their fixer's debt, or their clinic account is already bought (*in-the-company-books-3*)
» Escalate the Situation: the file goes to whoever else was looking

› A Chancery patrol pulls up and the auditor walks out to meet it.
» The police take the team's account as the record (*the report already says what happened*; Present a New Challenge: Security Guard as police, Scale 1, Core p. 305, or [[envelope-detail]] under the Wall)

## Power Sets

None applied by default. **Connected & Protected** (Core p. 328) fits the auditor; **Heavily Armed** (Core p. 328) fits the crew that comes back after *No Report Was Filed*.

## Canon and flags

- Corporate security is exactly as legal as the city police (Bible §3) — the *Jurisdiction Arranged* Special is that sentence in rules. The team is Baseline in the vault's terms: gear and weapon systems, replacement cybernetics only, no sculpt (Bible §2 hunter; Plan A.6).
- **[BUILD CHOICE]** (BC-116) Product Integrity as an unwitting Masquerade department; (BC-118) the department's name.
- **[OPEN]** (OQ-6) nobody on this team has the word for what is in the case, and neither does the file.
