---
type: challenge
name: "The Strike Hour"
slug: the-strike-hour
status: review
source: custom
page: "294–300, 297, 305, 118–120"
owner: WP7a
canon_refs: ["Bible §3 corporate security legality", "Bible §5 the inciting incident", "Bible §6 (all)", "Brief §7.1", "Brief §8", "Core p. 294–300", "Core p. 305", "Core p. 118–120"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: countdown
scale: 2
alias: "the lights going out"
short_description: "The hour between Continuity cutting the Ledger's mains and AP&I's generators coming up: everything the camp relies on fails at once except the causeway gate, a hundred people run, and the crew are part of what the strike is spending."
limits:
  - {name: generators-up, tier: 4}
  - {name: the-yard-empties, tier: 3}
default_tags: ["the mains are cut", "Nearspace flat grey", "a hundred people running", "torches, not floodlights"]
default_statuses: ["dark-3"]
specials:
  - {name: "Everything Fails Except The Gate", text: "While generators-up is not maxed, the camp's electronic layer ([[ledger-security-system]]) is dead: its readers, cameras, floodlight automation and speakers are off, none of its Threats can be voiced, its lockdown clock does not advance, and RFID Fatigues does not detect. The causeway gate and its floodlight run on the gate house's own generator: the gate is down, with a truck held on the far side and its engine running, and it is the one working thing in the camp."}
  - {name: "The Count Is Not Read", text: "[[ledger-line-security]]'s The Count does not fire for the duration — there are no speakers. Its guards count sheds by torch, a row at a time, and its other Threats stand; Debt Is The Lock still applies, because a sergeant with a torch and the crew's numbers can add months to an account by morning."}
  - {name: "The Running Is The Cover", text: "The crowd is a hazard and a cover. Anyone moving against the flow, or stopping in it, takes trampled-2 or separated-2 as a Consequence. Anyone moving with it holds the story tag one face in a hundred for as long as they keep moving, and torch lines, guards, and drones cannot pick them out of it."}
  - {name: "Stepped Around", text: "Continuity's cell ([[continuity-crisis-response-cell]]) delivers no Consequence to the crew unless they are between it and its contract, or inside a room it is blowing. It is a hazard, not an ally: its breaching frames, its cordon at the gap, and the power it cut are weather the crew move through. Nothing it does helps them on purpose, and nothing it does hinders them on purpose (Bible §5: the general breakout is cover)."}
  - {name: "When The Generators Come Up", text: "When generators-up maxes, the mains return all at once. Every floodlight comes on (exposed-2 to anyone in the open inside the wire or on the lit stretch of the causeway); the speakers click on and the count is read into the yard; the readers wake. Present a New Challenge: [[ledger-security-system]] at alert-2 with lockdown at 2, and [[ledger-line-security]] resumes The Count. This Challenge ends."}
  - {name: "The Yard Empties", text: "When the-yard-empties maxes, the crowd is gone — over the gate, into the flats, or back in the blocks — and the cover is gone with it. Whoever is still inside the wire is alone with the shift: remove one face in a hundred from everyone, and the torch line's Security Guard (Core p. 305) gains alert-3."}
threats:
  - threat: "Somewhere beyond the sheds a diesel the size of a truck turns over, catches, and dies."
    consequences:
      - {text: "The mechanic gets it a little further each time (generators-up-1).", statuses: ["generators-up-1"], tags: []}
      - {text: "A single tower light flickers and holds for a breath, and whoever is under it is lit (exposed-2).", statuses: ["exposed-2"], tags: []}
  - threat: "The shift sergeant gets a torch line together at the shed row and starts working it toward the wire."
    consequences:
      - {text: "Present a New Challenge: Security Guard (Core p. 305), Scale 1, gun for hire — torches, one shotgun, one rifle, and the count in their heads.", statuses: [], tags: []}
      - {text: "The yard between the blocks and the sheds is crossed with torch beams for the rest of the scene.", statuses: [], tags: ["torch line on the yard"]}
  - threat: "The block doors, which failed open, bang shut behind the last people out as the crowd clears them."
    consequences:
      - {text: "The blocks are empty and the yard is thinning (the-yard-empties-1).", statuses: ["the-yard-empties-1"], tags: []}
      - {text: "Anyone still inside a block is locked in with the shift (separated-3).", statuses: ["separated-3"], tags: []}
  - threat: "The crowd reaches the causeway gate, finds it down, and stops."
    consequences:
      - {text: "The crush at the barrier (trampled-2 to anyone in the front third of it).", statuses: ["trampled-2"], tags: []}
      - {text: "The yard behind is empty and the gate is the only thing anyone is looking at (the-yard-empties-2).", statuses: ["the-yard-empties-2"], tags: ["everyone at the gate"]}
  - threat: "A breaching frame's countdown is heard through a wall, out loud, so the people inside can hear it."
    consequences:
      - {text: "The frame blows the wall and the room with it (concussed-3 to anyone inside; the doorway, or the gate house, is gone).", statuses: ["concussed-3"], tags: []}
      - {text: "The cell comes through the gap it made. Present a New Challenge: [[continuity-crisis-response-cell]] — and anyone in its way is in its way.", statuses: [], tags: []}
  - threat: "generators-up maxes."
    consequences:
      - {text: "When The Generators Come Up: floodlights, speakers, readers; Present a New Challenge: [[ledger-security-system]] at alert-2, lockdown 2; the count is read into the yard. This Challenge ends.", statuses: [], tags: ["the mains are back"]}
power_sets: []
reuse_of: ""
---

# The Strike Hour

**Role:** countdown · **Scale:** 2 (the yard, the sheds, the wire, and everyone in them) · **Alias:** *the lights going out* · *The hour between the mains being cut and the generators coming up.*

The strike itself, as a Challenge — not the cell, which has its own profile ([[continuity-crisis-response-cell]]), and not the camp's security, which has two ([[ledger-line-security]], [[ledger-security-system]]), but the *hour*: the interval in which [[upstart|Continuity]] has switched the Ledger off and [[corp-c|AP&I]] has not yet switched it back on. Everything in [[breakout]]'s first four scenes happens inside it. It is the reason the security system's lockdown clock is frozen and the reason it starts; it is the crowd; it is the diesel behind the sheds.

The book allows a vector that is time running out (Core p. 290) and a Challenge whose role is a countdown "advancing toward a crescendo" (Core p. 297). This is both. Its two progress Limits are the two things that end the crew's cover: the generators, which give the camp its eyes back, and the yard emptying, which leaves whoever is still inside alone with the shift.

## Limits

| Limit | Tier |
|---|---|
| generators-up (progress) | 4 |
| the-yard-empties (progress) | 3 |

Neither is a Limit the crew overcome; both are clocks. `generators-up` climbs on the diesel Threat and on any Consequence elsewhere that says the mechanic got it started; the crew can push it *down* — a Set Back on the generator shed, a cut fuel line, a mechanic with a shotgun to his head — and doing so is a scene of its own inside the wire. `the-yard-empties` climbs as the crowd clears the blocks and hits the gate.

**[BUILD CHOICE]** (BC-142) The tiers are the pacing: four notches of diesel across three scenes inside the wire and the causeway walk, so that a crew moving with the crowd is past the gate when the floods come back and a crew that stopped for anything is on the lit road.

## Tags & statuses

the mains are cut, Nearspace flat grey, a hundred people running, torches, not floodlights · *dark-3*

## Specials

**Everything Fails Except The Gate:** the electronic system is dead until `generators-up` maxes; the causeway gate, on its own generator, is alive and *down*.

**The Count Is Not Read:** no speakers; the routine's guards count by torch; *Debt Is The Lock* still applies.

**The Running Is The Cover:** against the flow, *trampled-2* or *separated-2*; with it, *one face in a hundred*.

**Stepped Around:** the cell is a hazard, not an ally, and not an enemy. In its way is different.

**When The Generators Come Up:** at `generators-up` 4 — floodlights, speakers, readers; Present [[ledger-security-system]] at *alert-2*, `lockdown` 2; this Challenge ends.

**The Yard Empties:** at `the-yard-empties` 3 — the cover is gone; the torch line gains *alert-3*.

## Threats / Consequences

› A diesel turns over behind the sheds, catches, and dies.
» A little further each time (*generators-up-1*)
» One tower light flickers and holds (*exposed-2* to whoever is under it)

› The sergeant gets a torch line together at the shed row.
» Present a New Challenge: Security Guard (Core p. 305), Scale 1, gun for hire
» The yard is crossed with torch beams (*torch line on the yard*)

› The block doors bang shut behind the last people out.
» The blocks are empty (*the-yard-empties-1*)
» Anyone still inside is locked in with the shift (*separated-3*)

› The crowd reaches the gate, finds it down, and stops.
» The crush (*trampled-2*)
» Nobody is looking anywhere else (*the-yard-empties-2*; *everyone at the gate*)

› A breaching frame's countdown, through a wall, out loud.
» The wall and the room (*concussed-3*)
» The cell comes through — Present a New Challenge: [[continuity-crisis-response-cell]]

› `generators-up` maxes.
» *When The Generators Come Up* (*the mains are back*)

## Power Sets

None. The hour has no body.

## Canon and flags

- The strike's shape — mains cut, Nearspace cut, doors opened, one man walked out, a hundred people let run — and the general breakout as cover: Bible §5; [[continuity-crisis-response-cell]], [[hanne-oyelaran]]. Corporate security as the only law on the fill-rise: Bible §3. The camp's layout: [[coldwater-outfall]] (BC-24).
- **[BUILD CHOICE]** (BC-142) the strike hour as a countdown with two progress Limits, and what wakes when each maxes; the causeway gate alone on its own generator, and down. Registered in [[build-choices]] "Added by WP7a".
- **[OPEN]** (OQ-40) nothing here says whether anyone inside the wire knew the hour was coming.
