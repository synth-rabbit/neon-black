---
type: challenge
name: "EM Ambush"
slug: em-ambush
status: review
source: custom
page: ""
owner: WP5
canon_refs: ["Bible §2", "Core p. 294–300", "Core p. 255", "Core p. 319"]
flags: []
player_safe: false
role: barrier
scale: 1
alias: "Wired for One Kind of Target"
short_description: "A concealed electromagnetic kill-zone built specifically to catch a Bloodware target — a trap, not a combatant. Reads very differently depending on who walks into it."
limits:
  - {name: detect, tier: 3}
  - {name: disarm-or-bypass, tier: 4}
default_tags: ["concealed EM coils", "trigger-plate wired to the kill zone", "built by someone who's done this before"]
default_statuses: []
specials:
  - {name: "Built for One Kind of Target", text: "When the ambush triggers on a target with a nanite-based physiology (Bible §2, vampire), the Consequence includes a status that progresses toward exposing the master node (see the Threats below). Against anyone else, the same discharge is disruptive but survivable, per the setting's EM-weakness canon (Bible §2) rather than a universal weapon."}
threats:
  - threat: "A tripwire pulls taut in the dark, invisible unless you're looking for it."
    consequences:
      - {text: "The EM coils discharge. Against a Bloodware target: staggered-3 and nanite-lattice-disrupted-2, a step toward the master node being locatable (pairs with [[kernel-scanner-rig]]). Against anyone else: stunned-2 only.", statuses: ["staggered-3", "nanite-lattice-disrupted-2"], tags: []}
  - threat: "Sensors clock a nanite-dense signature passing through the kill zone."
    consequences:
      - {text: "The ambush arms fully and holds its charge, waiting for the target to reach the coils' center.", statuses: ["alert-1"], tags: []}
  - threat: "The trap does its work, and whoever set it reveals themselves."
    consequences:
      - {text: "Present a New Challenge: whoever laid the trap — a corp cleanup team (Security Guard or Mercenary Gunslinger, [[generic-reuse-map]]) or a Baseline hunting outfit, MC's choice for the scene.", statuses: [], tags: []}
  - threat: "disarm-or-bypass maxes out before the trap fires."
    consequences:
      - {text: "The kill zone is stripped for parts before it triggers — a source of [[em-pulse-cartridges]] and similar EM gear as loot, and a warning that someone is hunting Bloodware nearby.", statuses: [], tags: ["someone is hunting here"]}
power_sets: []
reuse_of: ""
---

# EM Ambush

**Role:** barrier (a hazard/trap, not a combatant — Core p. 297 groups "Barrier or Hazard" as one role) · **Scale:** 1 (a single prepared kill-zone) · **Alias:** Wired for One Kind of Target · *A concealed electromagnetic trap built specifically to catch a Bloodware target.*

The cross-cutting EM ambush Plan WP5 calls for — a set-piece trap any corp cleanup crew, Baseline hunting outfit, or well-prepared syndicate rival might lay for a vampire, using exactly the weakness Bible §2 specifies (electromagnetic effects, the master node) and nothing else. It is deliberately not tagged to any one Key Player; it is generic enough to appear wherever the MC needs a trap that punishes Bloodware specifically.

## Limits

| Limit | Tier |
|---|---|
| detect | 3 |
| disarm or bypass | 4 |

## Tags & statuses

concealed EM coils, trigger-plate wired to the kill zone, built by someone who's done this before

## Specials

**Built for One Kind of Target:** Against a Bloodware target, the discharge's Consequence includes a status progressing toward the master node being locatable. Against anyone else, the same discharge is disruptive but survivable (Bible §2).

## Threats / Consequences

› A tripwire pulls taut in the dark, invisible unless you're looking for it.
» EM coils discharge — Bloodware: *staggered-3*, *nanite-lattice-disrupted-2*; anyone else: *stunned-2* only

› Sensors clock a nanite-dense signature passing through the kill zone.
» The ambush arms fully and waits (*alert-1*)

› The trap does its work, and whoever set it reveals themselves.
» Present a New Challenge: whoever laid the trap ([[generic-reuse-map]])

› `disarm-or-bypass` maxes out before the trap fires.
» Stripped for parts as loot ([[em-pulse-cartridges]]) — *someone is hunting here*

## Power Sets

None.

## Canon and flags

- Bible §2 (vampire): weaknesses are EM and the master node, never sun/fire/stake; this Challenge is built entirely from that canon and nothing else.
