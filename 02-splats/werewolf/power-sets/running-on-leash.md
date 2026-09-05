---
type: power-set
name: "Running on Leash"
slug: running-on-leash
status: review
source: custom
page: ""
owner: WP2-werewolf
canon_refs: ["Bible §2 werewolf", "Bible §4 tone", "Brief §8", "Plan A.6", "Core p. 326–333", "Core p. 331", "Core p. 332–333"]
flags: [BUILD CHOICE]
player_safe: false
splat: werewolf
category: Noise
applies_to: "Any Challenge representing a Howler who has taken a dose, from a single pack member to an alpha."
default_tags: ["sculpted beast", "chromed claw sheaths", "scent through walls", "wrong shape in a doorway"]
default_statuses: ["running-3"]
specials:
  - {name: "Beast on the Dose", text: "While running-3 is on it, this Challenge helps everything it does with the sculpt and hinders anything requiring speech, patience, or fine hands. The dose holds until the end of the scene, or until the Challenge takes a status of tier 4 or higher representing exhaustion or blood loss, whichever comes first."}
  - {name: "Nothing to Reason With", text: "While the dose holds, any attempt to convince, frighten, bribe, or bargain with this Challenge resolves one success level lower. It can still be talked to — the dose makes a Howler hard to reach, not mindless; see Come Down."}
  - {name: "Come Down", text: "When running expires, the Challenge takes wrung-out-3 and cannot use this Power Set again until it takes another dose. A Challenge that has come down is a person again, and can be talked to."}
threats:
  - threat: "Draw one long breath and let the shape arrive"
    consequences:
      - {text: "Complete the shift (see Beast on the Dose).", statuses: ["running-3"], tags: []}
      - {text: "Open someone up with grown claws in chromed sheaths.", statuses: ["mauled-4"], tags: []}
      - {text: "Take a body to the ground and hold it there.", statuses: ["pinned-3"], tags: []}
      - {text: "Go up a wall or across a roofline into somewhere better.", statuses: ["superior-position-2"], tags: []}
      - {text: "Catch the scent it wanted and stop pretending to look (a hidden PC is found; Deny Them Something They Want).", statuses: [], tags: []}
  - threat: "Stop mid-stride, sway, and breathe wrong"
    consequences:
      - {text: "The dose runs out early.", statuses: ["wrung-out-3"], tags: []}
      - {text: "Take the next dose in front of everyone, out of a case, a port, or somebody else's count (reset the scene's clock on Come Down).", statuses: [], tags: ["another dose gone"]}
  - threat: "Put its weight against something that was holding"
    consequences:
      - {text: "Come through a shutter, a wall panel, or a vehicle door.", statuses: [], tags: ["no cover left", "way out is open"]}
      - {text: "Take a Consequence that was meant for a packmate standing beside it.", statuses: [], tags: []}
---

# Running on Leash

**Applies to:** Any Challenge representing a Howler who has taken a dose, from a single pack member to an alpha · **Category:** Noise · **Splat:** Howler

The overlay for the hour the dose is working. Layer it onto a Gang Member, a Syndicate Leg-Breaker, or a named pack Challenge; before the dose goes in, that profile runs as printed and this Power Set is not on it.

**Two Howler overlays (WP6, BC-133).** This is the general overlay for any Howler on a dose anywhere in Palisade, and the one [[leash-frenzy-pack]] layers. The Run's own overlay, [[running-shape]] (WP4-trio2), models the same dose through Meliora's settling mechanism and a *settled* clock the pack can read; the packs' named Challenges use that one. Never apply both to one Challenge. Under either, a Howler on the dose remains a person — hindered here, not mindless — who comes down and can be talked to (OQ-49 records the difference in wording for the GM). [[pack-tactics]] stacks with either.

## Tags & statuses

sculpted beast, chromed claw sheaths, scent through walls, wrong shape in a doorway, *running-3*

## Specials

**Beast on the Dose:** While *running-3* is on it, this Challenge helps everything it does with the sculpt and hinders anything requiring speech, patience, or fine hands. The dose holds until the end of the scene, or until the Challenge takes a status of tier 4 or higher representing exhaustion or blood loss, whichever comes first.

**Nothing to Reason With:** While the dose holds, any attempt to convince, frighten, bribe, or bargain with this Challenge resolves one success level lower. It can still be talked to — the dose makes a Howler hard to reach, not mindless (see Come Down).

**Come Down:** When *running* expires, the Challenge takes *wrung-out-3* and cannot use this Power Set again until it takes another dose. A Challenge that has come down is a person again, and can be talked to.

## Threats / Consequences

› Draw one long breath and let the shape arrive
» Complete the shift (see Beast on the Dose) (*running-3*)
» Open someone up with grown claws in chromed sheaths (*mauled-4*)
» Take a body to the ground and hold it there (*pinned-3*)
» Go up a wall or across a roofline into somewhere better (*superior-position-2*)
» Catch the scent it wanted and stop pretending to look (a hidden PC is found; Deny Them Something They Want)

› Stop mid-stride, sway, and breathe wrong
» The dose runs out early (*wrung-out-3*)
» Take the next dose in front of everyone, out of a case, a port, or somebody else's count (*another dose gone*)

› Put its weight against something that was holding
» Come through a shutter, a wall panel, or a vehicle door (*no cover left*, *way out is open*)
» Take a Consequence that was meant for a packmate standing beside it

## Canon and flags

- Splat canon obeyed (Plan A.6): the shape comes from **a dose, not from will, moon, rage, or a Source** (Bible §2), and every threat line runs through the dose. The Challenge is **sculpt plus chrome** — *chromed claw sheaths* is on the base tag list so the cybernetics half is never dropped. Nothing here spreads: no bite, no infection, no conversion.
- No Tao content and no Mythos category, so this is a **Noise** Power Set. It is not a re-flavour of **Shapechanger** (Core p. 331), which is a Mythos set built on a Source; a table wanting the printed set for a Howler would have to strip the Source out of it, and this exists so they do not have to.
- Related printed sets a Howler Challenge can also take as written: **Chromed Up** (Core p. 332) for a pack member who is more chrome than sculpt, and **Inhumanly Fast** (Core p. 333) for the drug-and-reflex end of the same idea.
- Body horror is the register the Bible asks for (§4); the come-down is written to be as visible as the shift.
- **[BUILD CHOICE]** (BC-46) display name; (BC-52) statuses, tiers, and the scene-length dose duration.
