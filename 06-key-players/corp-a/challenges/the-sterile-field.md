---
type: challenge
name: The Sterile Field
slug: the-sterile-field
status: review
source: custom
page: "294–300, 310, 319"
owner: WP4-trio2
canon_refs: ["Bible §2 werewolf", "Bible §3 the Masquerade", "Brief §4.1", "Brief §8", "Core p. 294–300", "Core p. 310", "Core p. 319"]
flags: [BUILD CHOICE]
player_safe: false
role: countdown
scale: 2
alias: "a service interruption"
short_description: "Meliora's containment protocol: the building seals, the air changes, and the crew has until the field goes hot to be somewhere else or to be material."
limits:
  - {name: sterilize, tier: 5}
  - {name: get-out, tier: 4}
  - {name: abort-the-field, tier: 6}
default_tags: ["shutters and airlocks", "positive pressure gone negative", "every door logs a face", "the announcement is very calm"]
default_statuses: ["sealed-3"]
specials:
  - {name: "Progress: Sterilize", text: "Sterilize is a progress Limit. It gains a tier whenever the crew spends a scene inside the field without advancing get-out, whenever a Consequence from [[sterile-field-unit]] lands on a PC, and whenever anything inside the field is opened, spilled, cut, or set on fire. When sterilize maxes, the field goes hot: foam floods the lower levels, the air is scrubbed, and everything still inside takes set-in-foam-5 and scoured-5. Statuses on sterilize are not shown to the crew as numbers; the tells are the announcement, the pressure, the lights, and the smell."}
  - {name: "Get Out Is Not Overcome", text: "Get-out is the crew's Limit, not Meliora's: maxing it means the crew is outside the cordon, not that the field has ended. A field that is not aborted still goes hot behind them, with whoever is left inside."}
  - {name: "The Announcement", text: "A recorded voice repeats the same four sentences on a loop, in three languages, in the register of a delayed transit service. Anyone who has been inside a field before takes remembering-3, a compelling status cleared by leaving the building or by breaking something."}
  - {name: "Abort Requires A Name", text: "Abort-the-field cannot be maxed by force, hacking, or destruction — only by an authorization from someone whose name is on the site's protocol list. There are four such names on a Foot site and eleven on the Terraces; [[solenne-marchetti]] is on every list Meliora keeps."}
threats:
  - threat: "Shutters run down in sequence from the far end of the corridor, and the pressure in the room changes enough to hurt."
    consequences:
      - {text: "The route the crew came in by is gone.", statuses: ["sealed-3"], tags: ["that way is shut"]}
      - {text: "Ears, sinuses, and any open graft react to the pressure drop.", statuses: ["bleeding-from-somewhere-2"], tags: []}
  - threat: "The calm voice begins the announcement, and the corridor lights step down one shade."
    consequences:
      - {text: "The field advances toward hot.", statuses: ["sterilize-1"], tags: []}
      - {text: "A Sterile Field Unit enters the level. Present a New Challenge: [[sterile-field-unit]].", statuses: [], tags: []}
  - threat: "Scrubbers start somewhere below and the air begins to taste of nothing at all."
    consequences:
      - {text: "Breathing hurts and keeps hurting.", statuses: ["scoured-lungs-3"], tags: []}
      - {text: "Anything the crew is carrying that is biological — a sample, a culture, a wound dressing, a body — is degrading. Burn a tag representing it, or take it as a story tag with 'spoiling' attached.", statuses: [], tags: ["the sample is spoiling"]}
  - threat: "A door the crew needs opens on its own, onto a route that is clean, lit, and away from the level they came for."
    consequences:
      - {text: "The field herds rather than kills. Advancing get-out this way costs the objective — Deny Them Something They Want.", statuses: [], tags: []}
      - {text: "The clean route logs every face that takes it.", statuses: ["marked-2"], tags: ["on the site's entry log"]}
power_sets: []
reuse_of: "Built beside Security System (Core p. 319) and Crumbling Building's navigate structure (Core p. 310)."
---

# The Sterile Field

**Role:** countdown · **Scale:** 2 · **Alias:** *a service interruption* · *The building seals, the air changes, and the crew has until the field goes hot.*

The Sterile Field is [[corp-a|Meliora Bioworks]]' site-wide containment protocol and the reason its buildings are shaped the way they are. Any Meliora site — a pharmaceutical bay under the Verdant Spire, a sculpting theater, a warranty clinic on [[suture-row]], a greenhouse floor in [[meliora-terraces]] — can declare a field, and the declaration is automatic in some cases and a supervisor's thumb in others. Shutters run, airlocks reverse, pressure inverts, the scrubbers start, and a recorded voice apologizes for the interruption. Then a [[sterile-field-unit]] comes in through the clean side.

It is not a trap built for intruders; it is a protocol built for spills, which is exactly why it is worse. It has no interest in who the crew are and no setting for *people are in here*. On the Terraces, the field's most-used feature is that the countermeasure program can declare one against *contamination* — the things that move in the condensation and nest in the root-mats ([[meliora-terraces]]) — and that a field declared for those reasons is not logged with the Chancery at all.

## Limits

| Limit | Tier |
|---|---|
| sterilize (progress) | 5 |
| get out | 4 |
| abort the field | 6 |

## Tags & statuses

shutters and airlocks, positive pressure gone negative, every door logs a face, the announcement is very calm · *sealed-3*

## Specials

**Progress: Sterilize.** Gains a tier when the crew spends a scene inside without advancing *get out*, when a [[sterile-field-unit]] Consequence lands on a PC, and when anything inside is opened, spilled, cut, or burned. At max, the field goes hot: *set-in-foam-5* and *scoured-5* to everything still inside. The crew never sees a number — only the announcement, the pressure, the lights, and the smell.

**Get Out Is Not Overcome.** Maxing *get out* puts the crew outside the cordon. The field still goes hot behind them, with whoever is left inside.

**The Announcement.** Four sentences, three languages, on a loop, in the register of a delayed transit service. Anyone who has been inside a field before takes *remembering-3*, compelling, cleared by leaving the building or by breaking something.

**Abort Requires A Name.** *Abort the field* cannot be maxed by force, hacking, or destruction — only by an authorization from a name on the site's protocol list. Four names on a Foot site, eleven on the Terraces. [[solenne-marchetti]] is on every list Meliora keeps.

## Threats / Consequences

› Shutters run down in sequence from the far end of the corridor, and the pressure in the room changes enough to hurt.
» The route the crew came in by is gone (*sealed-3*, *that way is shut*)
» Ears, sinuses, and any open graft react (*bleeding-from-somewhere-2*)

› The calm voice begins the announcement, and the corridor lights step down one shade.
» The field advances toward hot (*sterilize-1*)
» A unit enters the level (Present a New Challenge: [[sterile-field-unit]])

› Scrubbers start somewhere below and the air begins to taste of nothing at all.
» Breathing hurts and keeps hurting (*scoured-lungs-3*)
» Anything biological the crew is carrying is degrading (burn its tag, or *the sample is spoiling*)

› A door the crew needs opens on its own, onto a route that is clean, lit, and away from the level they came for.
» The field herds rather than kills (Deny Them Something They Want)
» The clean route logs every face that takes it (*marked-2*, *on the site's entry log*)

## Power Sets

None. This is a location and a system, not a person.

## Canon and flags

- Bible §2, §3 (the corporations do the cleanup); Brief §4.1, §8. Built beside Security System (Core p. 319) and the navigate structure of Crumbling Building (Core p. 310).
- **[BUILD CHOICE]** (BC-114) the protocol, its three Limits, the hidden progress tiers, and the abort-by-name rule.
