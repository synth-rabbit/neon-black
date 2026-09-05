---
type: power-set
name: Owned Asset
slug: owned-asset
status: review
source: custom
page: ""
owner: WP2-changeling
canon_refs: ["Bible §2 changeling", "Bible §3 power structure", "Bible §4 theme 3", "Brief §8", "Plan A.6", "Core p. 326–333", "Core p. 328", "Core p. 330"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
splat: changeling
category: Self
applies_to: "Any Challenge representing a Doppel who is still owned — a corporation's special unit, a syndicate's assassin, or anybody else's property with a face."
default_tags: ["unit credentials", "a handler on the line"]
default_statuses: ["tracked-2"]
limits:
  - {name: turn-them, tier: 5}
specials:
  - {name: "Standing Orders", text: "This Challenge does not improvise. When the crew does something its orders did not anticipate, it withdraws and reports rather than pressing: the MC may Escalate the Situation instead of inflicting a Consequence."}
  - {name: "Somebody Is Always Watching", text: "The tracker reports whether or not the Challenge wants it to. If the Challenge is captured, killed, or loses contact with its handler, at the end of that scene its unit knows where the crew is: the crew takes tagged-2 until the end of the next downtime."}
  - {name: "The Switch", text: "If the Challenge is about to be turned, taken, or otherwise lost to its owners, its handler can end it. The Challenge takes dead-6 and whatever it knew goes with it (Deny Them Something They Want). The crew cannot mitigate this. Once the turn-them Limit is maxed, this Special no longer functions."}
threats:
  - threat: "Take a call and stop listening to the room"
    consequences:
      - {text: "Receive an order and act on it before anyone can talk them out of it (Escalate the Situation).", statuses: [], tags: []}
      - {text: "Call in the unit (Present a New Challenge: corporate security or syndicate leg-breakers, Scale 2).", statuses: [], tags: []}
  - threat: "Look at a PC the way a fitter looks at a face"
    consequences:
      - {text: "Copy a PC's face, voice, and papers.", statuses: ["impersonated-2"], tags: ["wearing their face"]}
      - {text: "Offer the crew the one thing its owners can give and nobody else can (Escalate the Situation).", statuses: [], tags: []}
  - threat: "Touch their sternum without meaning to"
    consequences:
      - {text: "Break off mid-job and go where they are told, whatever it costs the scene (Deny Them Something They Want).", statuses: [], tags: []}
      - {text: "Drop where they stand, mid-sentence, with nobody in the room having done anything.", statuses: ["dead-6"], tags: []}
---

# Owned Asset

**Applies to:** Any Challenge representing a Doppel who is still owned — a corporation's special unit, a syndicate's assassin, or anybody else's property with a face · **Category:** Self · **For:** Doppels

## Limits

**turn-them 5** — TURN THEM: the handler is no longer worth more to this Challenge than whatever the crew is offering. It acts on its own from here; remove this Power Set, and the switch stops being a thing anyone else can use.

## Tags & statuses

unit credentials, a handler on the line, *tracked-2*

## Specials

**Standing Orders:** This Challenge does not improvise. When the crew does something its orders did not anticipate, it withdraws and reports rather than pressing: the MC may Escalate the Situation instead of inflicting a Consequence.

**Somebody Is Always Watching:** The tracker reports whether or not the Challenge wants it to. If the Challenge is captured, killed, or loses contact with its handler, at the end of that scene its unit knows where the crew is: the crew takes **tagged-2** until the end of the next downtime.

**The Switch:** If the Challenge is about to be turned, taken, or otherwise lost to its owners, its handler can end it. The Challenge takes **dead-6** and whatever it knew goes with it (Deny Them Something They Want). The crew cannot mitigate this. Once the *turn-them* Limit is maxed, this Special no longer functions.

## Threats / Consequences

› Take a call and stop listening to the room
» Receive an order and act on it before anyone can talk them out of it (Escalate the Situation)
» Call in the unit (Present a New Challenge: corporate security or syndicate leg-breakers, Scale 2)

› Look at a PC the way a fitter looks at a face
» Copy a PC's face, voice, and papers (create *wearing their face*; the PC takes *impersonated-2*)
» Offer the crew the one thing its owners can give and nobody else can (Escalate the Situation)

› Touch their sternum without meaning to
» Break off mid-job and go where they are told, whatever it costs the scene (Deny Them Something They Want)
» Drop where they stand, mid-sentence, with nobody in the room having done anything (*dead-6*)

## Against the book's neighbours

***Corporate Sponsored*** (Self, Core p. 328) and ***Connected & Protected*** (Self, Core p. 328) both model somebody with a company behind them, and both remain the right choice for a Challenge that is merely employed. This Power Set is the version where the company is not behind them, it is inside them. Layer it over the printed sets rather than instead of them where a Doppel is both.

## Canon and flags

- Splat canon (Plan A.6): a Doppel NPC obeys the same canon as a PC. This overlay carries the kill switch and the tracker; a Doppel Challenge that has escaped does **not** take it. Ownership is the Bible's fact (§2) and theme 3's whole subject (§4).
- The *turn-them* Limit at tier 5 exists so that a crew can, at cost, buy a Doppel out of their leash in play — and so that the moment they do, the handler's last option is gone. It is the Challenge-side mirror of [[switch-and-handler]]'s removal clause.
- **[BUILD CHOICE]** (BC-78) the Power Set name; (BC-83) that a handler can trigger the switch remotely; (BC-88) carrying a Limit in a Power Set's frontmatter, using the `challenge` schema's `limits` shape (Plan A.4) — the book's *Lucky +* and *Spirit-Possessed +* (Core p. 330–331) do the same in print, but Plan A.4's `power-set` schema did not list the field; WP6 added it to the template as optional (BC-129).
- **[OPEN]** (OQ-30) who the handler works for; the overlay is written so that it does not matter; [[changeling-cells]] leaves it open too (no single maker is proposed there).
