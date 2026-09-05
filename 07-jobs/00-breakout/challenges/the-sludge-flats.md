---
type: challenge
name: "The Sludge Flats"
slug: the-sludge-flats
status: review
source: custom
page: "294–300, 310, 320, 118–120"
owner: WP7a
canon_refs: ["Bible §5 the camp", "Bible §6 standing after the breakout", "Brief §7.1", "Brief §8", "Core p. 294–300", "Core p. 310", "Core p. 320", "Core p. 118–120"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: barrier
scale: 2
alias: "the dark past the floodlights"
short_description: "The Outfall's settling lagoons and sludge-flats, crossed at night: a crust that holds until it does not, a haze that hides the crew from the drone and the drone from the crew, culvert mouths the size of tunnels, and a tide coming in. Nobody walks out of the Ledger unaided."
limits:
  - {name: cross-the-flats, tier: 4}
  - {name: find-the-culvert-line, tier: 3}
  - {name: by-water, tier: 3}
default_tags: ["a crust over sludge", "chemical haze to the knee", "culvert mouths the size of tunnels", "the tide coming in", "no light but the gate's"]
default_statuses: ["lethal-in-the-wrong-places-3"]
specials:
  - {name: "Nobody Walks Out Unaided", text: "The flats are the reason the Ledger has no wall ([[coldwater-outfall]]). cross-the-flats at 4 is the honest tier for kilometers of poisoned ground in the dark with no map. The two cheaper Limits are the aids: find-the-culvert-line (3) — the raised concrete spine of the outfall's culverts, which runs to the coast and can be walked if it can be found; and by-water (3) — the landing stage's skiff ([[landing-stage-post]]), which follows the lagoon channels to the coast road's foot if its outboard starts."}
  - {name: "The Haze Is Also Cover", text: "While the crew are in the flats, the AP&I perimeter drone (Surveillance Drone, Core p. 320) cannot get a face: the haze over the lagoons defeats it. [[escapee-list]]'s noticed does not advance from anything the drone sees here. The same haze is against the crew — lights past twenty meters are smears, and the gate's floodlight is the only bearing."}
  - {name: "Poison Underneath", text: "This Challenge is Hazard Zone (Core p. 310) with a shape. Its Poison Consequences are the lagoons' — corrosive, choking, cumulative — and every physical status it deals is one the Weighhouse's surgeon on Suture Row will price."}
  - {name: "Past The Wire", text: "Nothing from the camp follows into the flats. [[ledger-line-security]] does not pursue past the causeway (No Bounty Beyond The Wire) and [[ledger-security-system]]'s reach ends at the last floodlight; a body in the Outfall at night is cheaper written off than followed (Bible §6). The only thing out here that answers to AP&I is the drone, and it cannot see."}
threats:
  - threat: "The crust, which held for the last ten steps, sags under the eleventh."
    consequences:
      - {text: "Through it, to the thigh, into what the city flushes (mired-3 and burned-2).", statuses: ["mired-3", "burned-2"], tags: []}
      - {text: "Somebody else's weight is what pulls them out, and now two are in it (separated from the rest: split-up-2).", statuses: ["split-up-2"], tags: []}
  - threat: "The haze thickens, and the gate's light — the only bearing — goes."
    consequences:
      - {text: "Turned around in the dark (lost-3; cross-the-flats cannot be advanced until it is reduced).", statuses: ["lost-3"], tags: []}
      - {text: "The haze in the lungs (choking-2, cumulative each scene in the flats).", statuses: ["choking-2"], tags: []}
  - threat: "A culvert mouth ahead, big enough to drive a truck into, breathes out — the Wall's run-off, discharging on a timer nobody out here knows."
    consequences:
      - {text: "The discharge takes whoever is on the culvert line off it (swept-3; burn a gear tag that was carried, not worn).", statuses: ["swept-3"], tags: []}
      - {text: "The culvert line is found — the raised spine, the way to the coast (find-the-culvert-line advances; create the story tag the culvert line).", statuses: [], tags: ["the culvert line"]}
  - threat: "The tide comes in behind the crew, over the flats they crossed."
    consequences:
      - {text: "No way back (Deny Them Something They Want: the flats behind are water).", statuses: [], tags: ["the tide is behind you"]}
      - {text: "The skiff, if they have it, floats free of its channel; the outboard coughs (by-water advances or Set Back, on the roll).", statuses: [], tags: []}
  - threat: "A searchlight comes out over the lagoons from the direction of the camp, sweeping, and the haze turns it into a wall of yellow."
    consequences:
      - {text: "Present a New Challenge: Surveillance Drone (Core p. 320) — AP&I perimeter drone on the generators' power; it cannot get a face through the haze and its surveillance report says only that people are in the flats.", statuses: [], tags: []}
      - {text: "The crew stop moving until it passes, and the tide does not (the tide is behind you; cross-the-flats loses a tier).", statuses: [], tags: []}
power_sets: []
reuse_of: "Hazard Zone, Core p. 310 (Poison), as a specific place; Surveillance Drone, Core p. 320"
---

# The Sludge Flats

**Role:** barrier · **Scale:** 2 (kilometers of ground; the part of it between the wire and the coast road) · **Alias:** *the dark past the floodlights* · *Nobody walks out of the Ledger unaided.*

[[coldwater-outfall|The Outfall]] itself: the settling lagoons and sludge-flats around the Ledger's fill-rise, on three sides of it, under a permanent chemical haze. Where the city's drainage comes out — the Wall's run-off, the Foot's sewage, the Stack's foundry water, the Basin's dust when it rains. "Uncrossable in daylight, lethal in the wrong places, and the reason nobody has ever walked out of the Ledger without help" ([[coldwater-outfall]]). The district file promises the crew will cross it once, in the dark, with the strike behind them, and this is the Challenge for that crossing.

It is the way off the causeway for anyone who decides three kilometers of raised road under floodlights is a killing ground ([[breakout-04-the-causeway]]); the way out by water from the landing stage ([[breakout-03-the-wire]]); and the way past a Gun Turret at `lockdown` 6. It rejoins the job at the coast road ([[breakout-05-a-name-and-a-place]]) — later than the road, wetter, and unseen.

## Limits

| Limit | Tier |
|---|---|
| cross the flats | 4 |
| find the culvert line | 3 |
| by water | 3 |

**cross the flats** at 4 is the tier for doing it blind. **find the culvert line** at 3 is the tier for doing it with a map the Outfall itself provides — the raised concrete spine of the culverts, which a shed crew that has worked the dredging season knows exists; a Flashback about the Ledger's routine can be the Discover that finds it. **by water** at 3 is the skiff, if the outboard starts.

## Tags & statuses

a crust over sludge, chemical haze to the knee, culvert mouths the size of tunnels, the tide coming in, no light but the gate's · *lethal-in-the-wrong-places-3*

## Specials

**Nobody Walks Out Unaided:** 4 blind; 3 with the culvert line or the skiff.

**The Haze Is Also Cover:** the drone gets no face here; `noticed` does not advance from the flats.

**Poison Underneath:** Hazard Zone (Core p. 310) with a shape; every physical status is one the Row's surgeon will price.

**Past The Wire:** nothing from the camp follows (Bible §6).

## Threats / Consequences

› The crust sags under the eleventh step.
» Through it, to the thigh (*mired-3*, *burned-2*)
» Two in it now (*split-up-2*)

› The haze thickens and the gate's light goes.
» Turned around (*lost-3*; cross the flats cannot advance until it is reduced)
» The haze in the lungs (*choking-2*, cumulative)

› A culvert mouth breathes out.
» Swept off the line (*swept-3*; burn a carried gear tag)
» The line is found (*the culvert line*; find the culvert line advances)

› The tide comes in behind.
» No way back (*the tide is behind you*)
» The skiff floats free; the outboard coughs (by water advances or Set Back)

› A searchlight out over the lagoons, and the haze turns it into a wall.
» Present a New Challenge: Surveillance Drone (Core p. 320), blind
» They stop; the tide does not (cross the flats loses a tier)

## Power Sets

None.

## Canon and flags

- The Outfall as a poisoned Fringe Zone; the lagoons as the reason the Ledger has no wall; the crew crossing it once, at night: [[coldwater-outfall]] (BC-17, BC-18, BC-24). Escapee list without bounty; a body in the Outfall cheaper written off than followed: Bible §6; [[ledger-line-security]].
- **[BUILD CHOICE]** (BC-148) tiers, the culvert line, the skiff, and the haze as cover from the drone. The profile reuses Hazard Zone (Core p. 310) and Surveillance Drone (Core p. 320) in addition to, not instead of, the book (Brief §0.1).
- **[OPEN]** (OQ-14) nothing in the flats is Tao; the haze is chemistry. (OQ-38) the culverts discharge what the city flushes, and nothing the Ledger makes.
