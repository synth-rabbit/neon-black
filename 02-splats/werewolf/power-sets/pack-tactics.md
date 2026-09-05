---
type: power-set
name: "Pack Tactics"
slug: pack-tactics
status: review
source: custom
page: ""
owner: WP2-werewolf
canon_refs: ["Bible §2 werewolf", "Bible §3 the syndicate", "Bible §4 theme 3", "Brief §8", "Plan A.6", "Core p. 326–333", "Core p. 329", "Core p. 146"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
splat: werewolf
category: Self
applies_to: "Any Challenge representing two or more of the Run acting together on their own ground, or an alpha with a kennel behind them."
default_tags: ["we run this ground", "lines walked a thousand times", "nobody goes alone"]
default_statuses: ["alert-2"]
specials:
  - {name: "Nobody Runs Alone", text: "When a member of the pack in the scene would take a status, another member who can reach them may take it instead."}
  - {name: "The Alpha Counts", text: "While the alpha is present, every other pack Challenge entering the scene gains unshakable-2. If the alpha is removed from the scene, the rest lose it and take rattled-2."}
  - {name: "Whose Ground This Is", text: "On the pack's own turf, the MC may spend a Consequence to state one thing about the ground the crew did not know and cannot now unlearn: a way out that is welded, a roof that carries, a room with people asleep in it."}
threats:
  - threat: "Spread along a line without a word being spoken"
    consequences:
      - {text: "Close the way out.", statuses: ["cornered-3"], tags: []}
      - {text: "Two take the front while a third goes wide.", statuses: ["flanked-3"], tags: []}
      - {text: "Push the crew toward ground the pack picked.", statuses: [], tags: ["out on the flats", "nowhere to climb"]}
      - {text: "Call the rest of the kennel (increase the collective's Scale by 1, or Present a New Challenge).", statuses: [], tags: []}
  - threat: "Hold up a hand and stop the pack dead"
    consequences:
      - {text: "Name terms — the ground, the count, or a dose — and wait (Deny Them Something They Want).", statuses: [], tags: ["the alpha's terms"]}
      - {text: "Let one of the crew through and keep the rest (split the crew).", statuses: [], tags: []}
  - threat: "Take the count out loud, in front of everyone"
    consequences:
      - {text: "Say what a PC or an NPC in the scene owes the pack, and to whom (Escalate the Situation).", statuses: ["owing-2"], tags: []}
      - {text: "Put a packmate's debt onto whoever is standing closest.", statuses: [], tags: ["somebody else's count"]}
---

# Pack Tactics

**Applies to:** Any Challenge representing two or more of the Run acting together on their own ground, or an alpha with a kennel behind them · **Category:** Self · **Splat:** Howler

The overlay for what a pack is when it is *not* on a dose: a gang with turf, lines it has walked a thousand times, and a ledger. Layer it onto Gang Member collectives, a named alpha, or a kennel's sentries. It stacks with [[running-on-leash]] on a night the pack has dosed, and works entirely without it on every other night — which is most of them, because doses cost money.

## Tags & statuses

we run this ground, lines walked a thousand times, nobody goes alone, *alert-2*

## Specials

**Nobody Runs Alone:** When a member of the pack in the scene would take a status, another member who can reach them may take it instead.

**The Alpha Counts:** While the alpha is present, every other pack Challenge entering the scene gains *unshakable-2*. If the alpha is removed from the scene, the rest lose it and take *rattled-2*.

**Whose Ground This Is:** On the pack's own turf, the MC may spend a Consequence to state one thing about the ground the crew did not know and cannot now unlearn: a way out that is welded, a roof that carries, a room with people asleep in it.

## Threats / Consequences

› Spread along a line without a word being spoken
» Close the way out (*cornered-3*)
» Two take the front while a third goes wide (*flanked-3*)
» Push the crew toward ground the pack picked (*out on the flats*, *nowhere to climb*)
» Call the rest of the kennel (increase the collective's Scale by 1, or Present a New Challenge)

› Hold up a hand and stop the pack dead
» Name terms — the ground, the count, or a dose — and wait (*the alpha's terms*; Deny Them Something They Want)
» Let one of the crew through and keep the rest (split the crew)

› Take the count out loud, in front of everyone
» Say what a PC or an NPC in the scene owes the pack, and to whom (*owing-2*; Escalate the Situation)
» Put a packmate's debt onto whoever is standing closest (*somebody else's count*)

## Canon and flags

- Splat canon obeyed (Plan A.6): a pack is a **gang** — "small fish in the big scheme, but kings and queens of their turfs" (Core p. 146; Bible §2) — with no political pull and no reach off its own ground. Every Consequence above is people, ground, or a ledger; none is money, corporate leverage, or a supply the pack manufactures, because the pack manufactures nothing (Bible §2–3).
- **Category: Self**, not Noise. Nothing in this set uses the sculpt or a dose; it is turf, numbers, and a count. That is deliberate — it means a pack is dangerous to a crew on a night when no one can afford to shift.
- The debt line is Bible §4 theme 3 made mechanical: the pack's hold over its own is the Almoners' hold one link further up.
- Built against the printed **Troop-Leading** set (Core p. 329), which a pack Challenge may also take as written for straightforward battlefield handling.
- **[BUILD CHOICE]** (BC-46) display name; (BC-52) statuses, tiers, and the alpha-presence rule.
- **[OPEN]** (OQ-18) the Almoners' terms with the alpha; the *dose* named in the alpha's terms is a thing the pack has in hand, never a supply the pack controls. Pack internals belong to WP4's `packs`.
