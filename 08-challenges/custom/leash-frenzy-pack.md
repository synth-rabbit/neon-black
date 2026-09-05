---
type: challenge
name: "A Pack, Mid-Leash"
slug: leash-frenzy-pack
status: review
source: custom
page: ""
owner: WP5
canon_refs: ["Bible §2", "Bible §3", "Core p. 294–300", "Core p. 306"]
flags: [BUILD CHOICE]
player_safe: false
role: attacker
scale: 2
alias: "Dogs Off the Chain"
short_description: "The Run mid-shift, chemically triggered and coordinated — attacker by default, pursuer when the fight turns into a chase."
limits:
  - {name: hurt-or-subdue, tier: 4}
  - {name: catch-or-outrun, tier: 3}
  - {name: trigger-burns-out, tier: 4}
default_tags: ["sculpt-and-chrome physiology", "pack coordination", "trigger-fueled-3"]
default_statuses: []
specials:
  - {name: "Pack Tactics", text: "When one member of the pack takes an action against a target, every other pack member present who acts against the same target that scene adds 1 Power, to a maximum of +2, reflecting coordinated flanking rather than a lone attacker."}
  - {name: "The Trigger Burns Out", text: "Every time this Challenge inflicts or takes a Consequence in a scene, it takes trigger-burns-out-1. When trigger-burns-out maxes at tier 4, see the final Threat below — this is the setting's built-in resolution that does not require defeating the pack outright, matching Bible §2 (the trigger is a chemical, chained state, not a permanent one)."}
  - {name: "Howler Overlay", text: "This profile stands alone; the tags and Specials above already carry the heightened strength, senses, and regeneration a Howler mid-Leash has (Bible §2). Layer [[running-on-leash]] on top for full crunch (the dose as running-3, Come Down as the crash). A pack of the Run in the Cinder Yards uses [[running-shape]] instead — never both. Under any overlay the pack are people, not beasts: coordinated, counting their doses, able to break off and to be talked to (BC-133, OQ-49); Dogs Off the Chain is the street's account, not the fact."}
threats:
  - threat: "A muzzle full of too many teeth turns toward the nearest sound."
    consequences:
      - {text: "Claws or bite (mauled-3)", statuses: ["mauled-3"], tags: []}
      - {text: "Grapple and pin (restrained-3)", statuses: ["restrained-3"], tags: []}
  - threat: "The pack fans out without a word, herding a target away from cover."
    consequences:
      - {text: "Cut off the retreat (surrounded-2 and create no clean line of retreat)", statuses: ["surrounded-2"], tags: ["no clean line of retreat"]}
  - threat: "One drops to all fours and the chase is on."
    consequences:
      - {text: "Close the distance (catch-2, using the catch/outrun Limit)", statuses: [], tags: []}
  - threat: "hurt-or-subdue maxes out on one pack member."
    consequences:
      - {text: "That member goes down; the rest do not stop for it — Present a New Challenge (this profile again, Scale reduced by 1) rather than treating the pack as defeated.", statuses: [], tags: []}
  - threat: "trigger-burns-out maxes out at tier 4."
    consequences:
      - {text: "The Leash runs out mid-fight. Remove trigger-fueled-3 and add withdrawal-crash-3 to the whole pack; hurt-or-subdue drops to 2 for the rest of the scene. This is the theme made mechanical: the drug that lets them off the chain is the chain (Bible §2–3), and it always ends.", statuses: ["withdrawal-crash-3"], tags: ["the trigger ran out"]}
power_sets: [running-on-leash]
reuse_of: ""
---

# A Pack, Mid-Leash

**Role:** attacker (pursuer via the catch/outrun Limit) · **Scale:** 2 (several, up to a dozen) · **Alias:** Dogs Off the Chain · *The Run mid-shift, chemically triggered and coordinated.*

The cross-cutting Howler-pack Challenge no single Key Player owns — usable by [[packs|the Run]] in [[cinder-yards]], by an Almoners enforcement action gone wrong, or by any job that needs a pack at the height of the trigger's effect. One role per Challenge (Plan A.6): this profile is written as an **attacker** by default, with a `catch-or-outrun` Limit that lets the same profile serve as a **pursuer** in a chase without a second file.

## Limits

| Limit | Tier |
|---|---|
| hurt or subdue | 4 |
| catch or outrun | 3 |
| trigger burns out (progress) | 4 |

## Tags & statuses

sculpt-and-chrome physiology, pack coordination · *trigger-fueled-3*

## Specials

**Pack Tactics:** Every other pack member acting against the same target that scene adds +1 Power (max +2) to the attacker's roll — coordinated flanking, not a lone predator.

**The Trigger Burns Out:** Every Consequence inflicted or taken adds `trigger-burns-out-1`. At tier 4, see the final Threat.

**Howler Overlay:** Stands alone; layer [[running-on-leash]] for full crunch, or [[running-shape]] for a Run pack — never both. The pack are people, not beasts (BC-133, OQ-49).

## Threats / Consequences

› A muzzle full of too many teeth turns toward the nearest sound.
» Claws or bite (*mauled-3*)
» Grapple and pin (*restrained-3*)

› The pack fans out without a word, herding a target away from cover.
» Cut off the retreat (*surrounded-2*, *no clean line of retreat*)

› One drops to all fours and the chase is on.
» Close the distance (*catch-2*)

› `hurt-or-subdue` maxes out on one pack member.
» That member goes down; the rest don't stop — Present a New Challenge (this profile, Scale −1)

› `trigger-burns-out` maxes out at 4.
» The Leash runs out mid-fight (*withdrawal-crash-3* to the whole pack, `hurt-or-subdue` drops to 2, *the trigger ran out*)

## Power Sets

[[running-on-leash]] (general) or [[running-shape]] (the Run) — optional, never both; see the *Howler Overlay* Special. [[pack-tactics]] stacks with either.

## Canon and flags

- Bible §2 (werewolf): the shift is chemically triggered, packs function as gangs, the trigger is the chain. Bible §3: the syndicate's product runs out.
- **[BUILD CHOICE]** the specific tag/Limit split and the "trigger burns out" resolution are this package's invention of a mechanic the Bible does not specify; the GM may re-tier.
