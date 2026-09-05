---
type: power-set
name: "Leash-Dosed"
slug: leash-dosed
status: review
source: custom
page: ""
owner: WP5
canon_refs: ["Bible §2", "Core p. 263", "Core p. 326–333"]
flags: [BUILD CHOICE]
player_safe: false
splat: none
category: Noise
applies_to: "Any Challenge representing a body that was never sculpted or chemically prepared for Leash but takes it anyway — a Baseline, a corp guard, a desperate civilian. Not a Howler; a body reacting badly to a drug it was never built for."
default_tags: ["muscles bulge wrong", "veins standing out black under the skin", "no fine control"]
default_statuses: ["berserk-3"]
specials:
  - {name: "Not Built for This", text: "This Challenge takes burnout-1 every time it inflicts or takes a Consequence while dosed. burnout is a progress Limit at tier 3; see the final Threat for what happens when it maxes."}
  - {name: "Berserk, Not Shifted", text: "Gains a strong bonus to any hurt-or-subdue action (already reflected in berserk-3), but any action requiring precision, subtlety, or self-control takes the no fine control weakness tag as a negative — this is Bane's venom, not a controlled shift (Bible §2's own reference point for the trigger)."}
threats:
  - threat: "Muscles bulge wrong, veins standing out black under the skin."
    consequences:
      - {text: "A wild swing lands harder than it should (bludgeoned-3), but leaves the attacker open (exposed-2 to the next action against them).", statuses: ["bludgeoned-3", "exposed-2"], tags: []}
  - threat: "It doesn't stop when it should, and the body keeps drawing on reserves it doesn't have."
    consequences:
      - {text: "burnout advances a tier.", statuses: [], tags: []}
  - threat: "burnout maxes out at 3."
    consequences:
      - {text: "The body gives out. This Challenge takes collapsed-5 and stops posing a threat, unconscious and in urgent need of a medic — or, if the MC wants a grimmer table, the Consequence is written as a lasting injury (organ damage, a status that follows the character past this scene) rather than mechanical death, matching the book's own guidance to state Consequences as something concrete rather than automatic lethality.", statuses: ["collapsed-5"], tags: []}
---

# Leash-Dosed

**Applies to:** Any Challenge representing a body that was never sculpted or chemically prepared for Leash but takes it anyway. · **Category:** Noise · **Splat:** none

`[BUILD CHOICE]` A body that has not had the bio-sculpt-and-chrome preparation a true Howler's transformation requires (Bible §2: werewolves are "a mix of bio-sculpt and cybernetics," triggered chemically) does not shift cleanly when it takes Leash — it reacts badly, in the Bane-from-the-Batman-comics register the Bible names as the trigger's own reference point (Bible §2). This is an authorized invention within this package's brief (not a new splat mechanic and not lycanthropy under a different name): it exists so an MC can put an unprepared Baseline, a desperate civilian, or a corp guard who got dosed by accident into a scene without borrowing the werewolf splat's own theme kits. Registered as `BC-28` in [[build-choices|BC-27 to BC-30]].

## Tags & statuses

muscles bulge wrong, veins standing out black under the skin, no fine control · *berserk-3*

## Specials

**Not Built for This:** Takes `burnout-1` per Consequence inflicted or taken while dosed; `burnout` is a progress Limit at tier 3.

**Berserk, Not Shifted:** Strong hurt-or-subdue bonus, but precision/subtlety/self-control actions carry the *no fine control* weakness — Bane's venom, not a controlled shift.

## Threats / Consequences

› Muscles bulge wrong, veins standing out black under the skin.
» A wild swing lands hard (*bludgeoned-3*) but leaves an opening (*exposed-2*)

› It doesn't stop when it should, and the body keeps drawing on reserves it doesn't have.
» `burnout` advances

› `burnout` maxes out at 3.
» The body gives out (*collapsed-5*) — written as a concrete Consequence (unconscious, or a lasting injury), never automatic death by default.

## Canon and flags

- Bible §2 (werewolf): the trigger is chemical, "in the style of Bane," and the shift itself requires the bio-sculpt-and-chrome preparation only a true Howler has. This overlay is explicitly what happens to a body that lacks that preparation, so it never contradicts or duplicates the splat's own mechanics.
- **[BUILD CHOICE]** (BC-28) this entire Power Set — the Bible does not describe what an unprepared body does on Leash; this is this package's answer, flagged for the GM as the task brief itself requires.
