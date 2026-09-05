---
type: challenge
name: Sterile Field Unit
slug: sterile-field-unit
status: review
source: custom
page: "294–300, 304, 305"
owner: WP4-trio2
canon_refs: ["Bible §2 werewolf", "Bible §2 rarity", "Bible §3 the Masquerade", "Brief §4.1", "Brief §8", "Core p. 294–300", "Core p. 304", "Core p. 305", "Core p. 332"]
flags: [BUILD CHOICE]
player_safe: false
role: attacker
scale: 1
alias: "soap"
short_description: "Meliora's bio-containment response: a sealed four-person team in white overpressure suits who arrive to sterilize a site, and who count people as material."
limits:
  - {name: hurt-or-subdue, tier: 4}
  - {name: breach-a-suit, tier: 3}
  - {name: talk-them-down, tier: 5}
default_tags: ["overpressure suits", "sealed comms", "foam lances and sample tongs", "site authority under enclave law"]
default_statuses: ["methodical-2"]
specials:
  - {name: "Material, Not Witnesses", text: "A Sterile Field Unit does not negotiate with anyone inside a declared field; under enclave law and the Chancery's remediation statutes, everything inside is Meliora's material. Talk-them-down is tier 5 and can only be attacked from outside the cordon — by a Chancery officer, a rival corporation's counsel, or a live feed. Inside, it is immune and the Limit reads \"-\"."}
  - {name: "Sealed", text: "The unit is immune to airborne, contact, and biological effects while their suits hold. Statuses that would work through skin, blood, breath, or scent do nothing until breach-a-suit is maxed. When breach-a-suit maxes, one suited officer takes exposed-3 and stops fighting; the rest of the unit stops fighting too, because retrieving them takes priority over the crew."}
  - {name: "Take It Alive If You Can", text: "Against anything the unit believes is a sculpt event — a Howler, a body mid-settle, a subject with visible Patched sculpt-work — the unit leads with foam and tongs rather than rounds. Their first Consequence against such a target each scene must be a restraining or containing one, not a lethal one. This is not mercy; a live sample is worth more."}
threats:
  - threat: "White suits come down the street in a line, and the street empties ahead of them without being told to."
    consequences:
      - {text: "The unit declares a field and seals the block. Present a New Challenge: [[the-sterile-field]].", statuses: [], tags: ["the block is sealed"]}
      - {text: "Anyone still in the open is logged, photographed, and told to stand still.", statuses: ["marked-2"], tags: []}
  - threat: "A lance comes up and the nozzle hisses as it charges."
    consequences:
      - {text: "Containment foam across an area: everything caught sets in eleven seconds.", statuses: ["set-in-foam-4"], tags: []}
      - {text: "A short controlled burst to the legs, because the top half is the sample.", statuses: ["shattered-knee-3"], tags: []}
  - threat: "Two of them peel off toward someone on the ground and unroll a bag."
    consequences:
      - {text: "The subject is bagged and carried out; Deny Them Something They Want, or Escalate the Situation if the subject is a PC's friend.", statuses: [], tags: ["taken as material"]}
      - {text: "Sample tongs into open tissue, and the unit does not stop for the screaming.", statuses: ["flensed-3"], tags: []}
  - threat: "A suited officer holds a scanner steady on a member of the crew for four full seconds."
    consequences:
      - {text: "The scan reads implants, grafts, and healing sculpt-work, and the unit's posture changes.", statuses: ["exposed-3"], tags: ["logged as a sculpt event"]}
      - {text: "The find is uploaded. A collection request follows the PC for the rest of the Series — the van comes to their district (see [[ondine-ferreira]]).", statuses: [], tags: ["on Meliora's collection list"]}
power_sets: []
reuse_of: "Built beside Security Guard (Core p. 305) and Heavy Urban Response Tactics Officer (Core p. 304); Chromed Up (Core p. 332) for a corporate-funded variant."
---

# Sterile Field Unit

**Role:** attacker · **Scale:** 1 · **Alias:** *soap* · *Meliora's bio-containment response: four people in white overpressure suits who arrive to sterilize a site.*

A Sterile Field Unit is what [[corp-a|Meliora Bioworks]] sends when a site declares an event: a spill on a pharmaceutical line, a floor of the Verdant Spire that has gone wrong overnight, a sculpt failure in a warranty clinic, or a body found in the wrong shape in a district Meliora has no business in. Four suited officers, one lance, one case, sealed comms, and the legal authority of an enclave inside the cordon and a remediation contract outside it ([[meliora-terraces]]; [[suture-row]]). They are not soldiers and do not act like soldiers: they move slowly, in a line, and they finish what they came to do.

Under the Wall they are called **soap**, and the sentence is *here comes the soap*, and it is not a joke about hygiene. A unit that arrives at a Foot address arrives because something happened there that Meliora already knows the shape of.

Their standing brief includes Howler incidents — the corporations do the cleanup for what the Masquerade hides (Bible §3) — and they perform it as biology. Nothing in a Sterile Field report ever says *Howler*. The word in the file is **event**.

## Limits

| Limit | Tier |
|---|---|
| hurt or subdue | 4 |
| breach a suit | 3 |
| talk them down | 5 (inside a declared field: –) |

## Tags & statuses

overpressure suits, sealed comms, foam lances and sample tongs, site authority under enclave law · *methodical-2*

## Specials

**Material, Not Witnesses:** Inside a declared field, everything is Meliora's material and *talk them down* is immune. The Limit only exists from outside the cordon — a Chancery officer, a rival's counsel, a live feed.

**Sealed:** Airborne, contact, and biological effects do nothing while the suits hold. When *breach a suit* maxes, one officer takes *exposed-3* and stops fighting, and so does the rest of the unit: retrieval comes before the crew.

**Take It Alive If You Can:** Against a sculpt event — a Howler, a body mid-settle, visible Patched sculpt-work — the unit's first Consequence each scene must restrain or contain rather than kill. A live sample is worth more.

## Threats / Consequences

› White suits come down the street in a line, and the street empties ahead of them without being told to.
» The unit declares a field and seals the block (Present a New Challenge: [[the-sterile-field]]; *the block is sealed*)
» Anyone still in the open is logged and photographed (*marked-2*)

› A lance comes up and the nozzle hisses as it charges.
» Containment foam across an area (*set-in-foam-4*)
» A short controlled burst to the legs, because the top half is the sample (*shattered-knee-3*)

› Two of them peel off toward someone on the ground and unroll a bag.
» The subject is bagged and carried out (Deny Them Something They Want, or Escalate the Situation; *taken as material*)
» Sample tongs into open tissue (*flensed-3*)

› A suited officer holds a scanner steady on a member of the crew for four full seconds.
» The scan reads implants, grafts, and healing sculpt-work (*exposed-3*, *logged as a sculpt event*)
» The find is uploaded and a collection request follows the PC (*on Meliora's collection list*; see [[ondine-ferreira]])

## Power Sets

None by default. For a Spire-based unit, Chromed Up (Core p. 332). For a unit escorting an executive, add nothing — they are the escort ([[vice-president-marchetti]]).

## Canon and flags

- Bible §2 (rarity; the shift and its supply chain), §3 (corporate cleanup keeps Bloodware and Howlers hidden); Brief §4.1 (Noise plus cleanup); Brief §8.
- **[BUILD CHOICE]** (BC-108, BC-114) the unit, the street name *soap*, the sealed/immunity rules, and the take-alive brief.
- Splat canon (Plan A.6): the unit's file language never names Howlers; nothing here makes the shift public.
