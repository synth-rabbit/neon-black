---
type: challenge
name: "Hanne Oyelaran, \"Amber\""
slug: hanne-oyelaran-challenge
status: review
source: custom
page: "294–300, 321–325, 118–120"
owner: WP4-trio1
canon_refs: ["Bible §2 hunter", "Bible §3 corporate security legality", "Bible §5 the inciting incident", "Brief §8", "Core p. 294–300", "Core p. 321–325"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: pursuer
scale: 0
alias: "the one who takes her helmet off"
short_description: "Continuity's crisis-response lead: reads a room like a floor plan, talks to frightened people like a paramedic, and completes the contract as written."
limits:
  - {name: hurt-or-subdue, tier: 4}
  - {name: convince, tier: 5}
  - {name: discredit, tier: 3}
  - {name: contract-complete, tier: 4}
default_tags: ["first through the door", "reads a room like a floor plan", "the warm voice", "no name anywhere on her"]
default_statuses: ["calm-3"]
specials:
  - {name: "Cell Eleven", text: "When Amber takes a status her cell can take for her, the cell takes it instead. Use Continuity Crisis-Response Cell. If the cell is not present, this Special does not apply and her hurt-or-subdue is 3."}
  - {name: "The Warm Voice", text: "When Amber speaks to civilians, bystanders, or anyone frightened and unarmed, she may give reassured-3 to all of them at once. reassured is a compelling status: it goes away when the person acts against her instructions, and while it stands they will point the crew out to her if asked."}
  - {name: "The Contract Is The Ceiling", text: "Amber will not deliver a Consequence to anyone who is not named in her contract and is not between her and the person who is. Crews that stay out of the doorway are stepped around. This is not mercy; incidents are billable."}
  - {name: "She Was Not Told Why", text: "Amber cannot be made to reveal the reason for a contract, by any Limit, because she does not have it. Maxing convince yields the name, the window, and the client's contact protocol, and nothing else — every route past that runs through [[rosalind-ekwueme]], not her."}
threats:
  - threat: "She takes her helmet off in the middle of a scene that is not finished, and looks directly at someone."
    consequences:
      - {text: "She tells them what is about to happen and what to do about it, and being told is worse (rattled-2 and she gains superior-position-2).", statuses: ["rattled-2", "superior-position-2"], tags: []}
      - {text: "She names something about them she should not know — a face, a block, a debt. Escalate the Situation.", statuses: [], tags: []}
  - threat: "She lifts two fingers without looking away from the person she is talking to."
    consequences:
      - {text: "Cell Eleven moves on the signal (deliver a Consequence from Continuity Crisis-Response Cell).", statuses: [], tags: []}
      - {text: "The exits the crew were counting on are held before they reach them (Deny Them Something They Want).", statuses: [], tags: []}
  - threat: "She puts a hand under someone's elbow and starts walking them toward the door."
    consequences:
      - {text: "The extraction advances; nothing is hurried and nobody is hurt (contract-complete-2).", statuses: ["contract-complete-2"], tags: []}
      - {text: "Anyone who steps in front of her is put down efficiently and without heat (broken-arm-3).", statuses: ["broken-arm-3"], tags: []}
  - threat: "She raises her carbine to a low ready and says a number out loud."
    consequences:
      - {text: "Aimed fire, one target, center of mass (gunshot-wound-3).", statuses: ["gunshot-wound-3"], tags: []}
      - {text: "She calls the scene lost and pulls the cell out through a wall (the cell and whatever it has leave; add contract-complete-1).", statuses: ["contract-complete-1"], tags: []}
power_sets: []
reuse_of: ""
---

# Hanne Oyelaran, "Amber"

**Role:** pursuer · **Scale:** 0 (Cell Eleven is Scale 2 beside her) · **Alias:** *the one who takes her helmet off* · *She completes the contract as written.*

Crisis-response lead for [[upstart|Continuity Risk & Response]]; the person who ran the strike on [[coldwater-outfall|the Ledger]] (Bible §5). See [[hanne-oyelaran]] for who she is, what she wants, and what she does not know.

A **Baseline** (Bible §2): a replacement eye, a replacement knee, and nothing else — no sculpt, no bio-work. Her edge is a cell that has trained together for four years, a breaching frame, and the fact that at a cordon she has the standing of a police officer (Bible §3).

## Limits

| Limit | Tier |
|---|---|
| hurt or subdue | 4 (3 without her cell) |
| convince | 5 |
| discredit | 3 |
| contract-complete (progress) | 4 |

**contract-complete** is hers, not the crew's: when it maxes, she has the person or the thing she came for and is gone. In the breakout it is the extraction clock (WP7a).

**discredit** at 3: prove to a crowd that she is a contractor and not an emergency service, and *the warm voice* stops working — remove that base tag and *reassured* cannot be given again in the scene.

## Tags & statuses

first through the door, reads a room like a floor plan, the warm voice, no name anywhere on her · *calm-3*

## Specials

**Cell Eleven:** her cell takes statuses for her ([[continuity-crisis-response-cell]]). Without it, *hurt or subdue* is 3.

**The Warm Voice:** *reassured-3* to every frightened, unarmed person at once — compelling, ends when they act against her instructions, and while it stands they will point the crew out if asked.

**The Contract Is The Ceiling:** she delivers no Consequence to anyone unnamed in the contract who is not in her way. Incidents are billable.

**She Was Not Told Why:** *convince*, maxed, yields the name, the window and the client's contact protocol. There is nothing else in her to get.

## Threats / Consequences

› She takes her helmet off mid-scene and looks directly at someone.
» Being told what is about to happen (*rattled-2*; she gains *superior-position-2*)
» She names something she should not know (Escalate the Situation)

› She lifts two fingers without looking away.
» Cell Eleven moves (deliver a Consequence from [[continuity-crisis-response-cell]])
» The exits are held first (Deny Them Something They Want)

› She puts a hand under an elbow and starts walking.
» The extraction advances, unhurried (*contract-complete-2*)
» Anyone in front of her is put down without heat (*broken-arm-3*)

› She raises the carbine to a low ready and says a number out loud.
» Aimed fire, center of mass (*gunshot-wound-3*)
» She calls the scene lost and pulls out through a wall (*contract-complete-1*)

## Power Sets

None. A cell escalation adds **Heavily Armed** (Core p. 328) to [[continuity-crisis-response-cell]], not to her.

## Canon and flags

- Baseline canon — replacement-only cybernetics, no sculpting or bio-manipulation: Bible §2. Corporate security's legality: Bible §3. The strike and its shape: Bible §5.
- **[BUILD CHOICE]** (BC-103, BC-107) her name, her cell, and her being a Baseline who was told a name and a window.
- **[OPEN]** (OQ-10) *She Was Not Told Why* is the structural guarantee that this profile cannot leak the reason [[tomas-adair]] matters.
