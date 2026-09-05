---
type: challenge
name: Vice President Marchetti
slug: vice-president-marchetti
status: review
source: custom
page: "294–300, 304"
owner: WP4-trio2
canon_refs: ["Bible §2 werewolf", "Bible §3 power structure", "Bible §4 theme 1", "Brief §8", "Core p. 294–300", "Core p. 304", "Core p. 328"]
flags: [BUILD CHOICE]
player_safe: false
role: temptation
scale: 0
alias: "the woman from Meliora"
short_description: "The executive who owns the Long Settle, offering exactly what the crew needs in exchange for exactly what she needs, and never once raising her voice."
limits:
  - {name: refuse-her, tier: 5}
  - {name: implicate, tier: 6}
  - {name: hurt-or-subdue, tier: 2}
default_tags: ["reasonable in every register", "signs the contracts herself", "a warm-handled sample case", "forty years of clinical authority"]
default_statuses: ["asset-protection-3"]
specials:
  - {name: "The Offer Is Real", text: "Whatever Marchetti offers, she delivers — a body repaired, a name struck from a list, a debt cleared, a clinic opened. She never lies about the terms and never mentions the terms twice. Refuse-her is a polar Limit against her negotiate attempts: a PC who maxes refuse-her has ended the conversation for the Series, and Marchetti's people stop offering and start filing."}
  - {name: "Fund It, Don't Fix It", text: "Once per scene, as a Consequence, Marchetti can resolve the crew's immediate problem with money and access instead of force — a Sterile Field Unit stood down, a lift pass, a surgeon, a shipment released. The problem goes away. Give the crew obligated-3, which is a compelling status and clears only when the favor is repaid."}
  - {name: "Nothing Personal In Writing", text: "Marchetti cannot be implicated by anything short of the invoice itself. Statuses on implicate from testimony, recordings, or reputation are halved (round down); only physical documentation of the aftercare supply contract, the variance file, or a dosing record puts full tiers on implicate."}
  - {name: "Escorted", text: "When Marchetti would take a physical status her escort takes it instead. Use Bodyguard (Core p. 304) or a Sterile Field Unit pair (see [[sterile-field-unit]]) with Scale 1; on the Crest, add the Connected & Protected Power Set (Core p. 328)."}
threats:
  - threat: "She sets the sample case down beside her chair and asks, with real interest, what happened to the crew's worst injury."
    consequences:
      - {text: "She names the procedure, the surgeon who botched it, and what it would cost her to fix — nothing.", statuses: ["tempted-3"], tags: []}
      - {text: "She has the file already; she read it before the meeting and lets that show.", statuses: ["exposed-2"], tags: ["she knows what was done to you"]}
  - threat: "She explains the program, patiently, in the register of a surgeon describing a good outcome — including the part where stopping now kills more people than continuing."
    consequences:
      - {text: "The argument lands, because it is a real argument. A PC who cannot answer it takes doubt-3, a compelling status cleared by acting against Meliora in the same scene.", statuses: ["doubt-3"], tags: []}
      - {text: "She offers the crew the honest version of the work — collection, escort, retrieval — at a rate nobody under the Wall has ever been offered.", statuses: [], tags: ["Meliora contract on the table"]}
  - threat: "She looks at her case, then at the door, and says she has kept the crew long enough."
    consequences:
      - {text: "The window closes. Deny Them Something They Want; the meeting cannot be reopened this job.", statuses: [], tags: []}
      - {text: "Her regulatory affairs office spends a favor on the Hill. Present a New Challenge from [[corp-a-reuse]] — an Investigator (Core p. 305) working the crew's paperwork rather than their bodies.", statuses: ["legal-issues-3"], tags: []}
  - threat: "Somebody in the room raises their voice, and she stops talking and waits."
    consequences:
      - {text: "The escort closes. Present a New Challenge: Bodyguard (Core p. 304) or [[sterile-field-unit]], Scale 1.", statuses: [], tags: []}
      - {text: "She writes the crew off. Every Meliora door in the Series is shut to them until they bring her the one thing she cannot buy.", statuses: ["blacklisted-3"], tags: []}
power_sets: []
reuse_of: "Built beside Corporate Executive, Core p. 304; escort from Bodyguard, Core p. 304; Connected & Protected Power Set, Core p. 328."
---

# Vice President Marchetti

**Role:** temptation · **Scale:** 0 · **Alias:** *the woman from Meliora* · *The executive who owns the Long Settle, offering exactly what the crew needs in exchange for exactly what she needs.*

The person is [[solenne-marchetti]]. This profile is for the scene where the crew is in a room with her and the room is the obstacle. She is a **temptation** first (Core p. 297) and a corporate executive second; the fight, if it comes, is short and she is not in it.

## Limits

| Limit | Tier |
|---|---|
| refuse her | 5 |
| implicate | 6 |
| hurt or subdue | 2 |

*Refuse her* is polar against her offers: max it out and a PC has ended the negotiation for the Series. *Implicate* is tier 6 because the only evidence that touches her is paper.

## Tags & statuses

reasonable in every register, signs the contracts herself, a warm-handled sample case, forty years of clinical authority · *asset-protection-3*

## Specials

**The Offer Is Real:** Whatever Marchetti offers, she delivers. She never lies about the terms and never repeats them. A PC who maxes *refuse her* is done being offered things and starts being filed.

**Fund It, Don't Fix It:** Once per scene, as a Consequence, she resolves the crew's immediate problem with money and access — a unit stood down, a lift pass, a surgeon, a shipment released. Give the crew *obligated-3*, compelling, cleared only by repaying the favor.

**Nothing Personal In Writing:** Testimony, recordings, and reputation put half tiers (round down) on *implicate*. Only the aftercare supply contract, the variance file, or a dosing record puts full tiers on it.

**Escorted:** When she would take a physical status her escort takes it instead — Bodyguard (Core p. 304) or a [[sterile-field-unit]] pair at Scale 1; on the Crest, add Connected & Protected (Core p. 328).

## Threats / Consequences

› She sets the sample case down beside her chair and asks, with real interest, what happened to the crew's worst injury.
» She names the procedure, the surgeon who botched it, and what it would cost her to fix — nothing (*tempted-3*)
» She read the file before the meeting and lets that show (*exposed-2*, *she knows what was done to you*)

› She explains the program, patiently, including the part where stopping now kills more people than continuing.
» The argument lands, because it is a real argument (*doubt-3*, compelling; cleared by acting against Meliora in the same scene)
» She offers the honest version of the work at a rate nobody under the Wall has been offered (*Meliora contract on the table*)

› She looks at her case, then at the door, and says she has kept the crew long enough.
» The window closes (Deny Them Something They Want; the meeting cannot be reopened this job)
» Regulatory affairs spends a favor on the Hill (*legal-issues-3*; Present a New Challenge: Investigator, Core p. 305)

› Somebody in the room raises their voice, and she stops talking and waits.
» The escort closes (Present a New Challenge: Bodyguard, Core p. 304, or [[sterile-field-unit]], Scale 1)
» She writes the crew off (*blacklisted-3*; every Meliora door is shut until they bring her the one thing she cannot buy)

## Power Sets

None by default. On the Crest, Connected & Protected (Core p. 328).

## Canon and flags

- Bible §2, §3, §4 theme 1; Brief §8 (custom profiles for named key characters). Built beside Corporate Executive (Core p. 304).
- **[BUILD CHOICE]** (BC-108) the twist she owns; (BC-114) *refuse her* as a polar Limit and *implicate* at tier 6 with the paper-only rule.
- Splat canon (Plan A.6): Marchetti is not one of the five. No sculpting content here contradicts the Bible; she is Sculpted, which is a caste band, not a splat.
