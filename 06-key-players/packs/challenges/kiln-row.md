---
type: challenge
name: The Kiln Row
slug: kiln-row
status: review
source: custom
page: "294–300, 310, 311"
owner: WP4-trio2
canon_refs: ["Bible §2 werewolf", "Bible §3 the Masquerade", "Bible §4 theme 3", "Brief §8", "Core p. 294–300", "Core p. 297", "Core p. 310", "Core p. 311"]
flags: [BUILD CHOICE, TAO-REINTERPRETED]
player_safe: false
role: barrier
scale: 2
alias: "six brick sheds and a lot of ash"
short_description: "Six kiln-halls on the old rail siding, scrap barricades, a sentry on every roof and a kilometre of open ash in front: the Run's home ground, where being seen coming is the whole point."
limits:
  - {name: get-in-unseen, tier: 5}
  - {name: be-invited, tier: 3}
  - {name: get-out-with-it, tier: 4}
default_tags: ["a kilometre of open ash with no cover", "scrap barricades and fire-barrels", "a sentry on every roof", "the chimney that still smokes", "cages that were for carcasses"]
default_statuses: ["watched-3"]
specials:
  - {name: "Seen Coming", text: "The flats are the defense. There is no approach to the Kiln Row that is not visible for four hundred metres, and get-in-unseen is tier 5 for that reason alone — no gate, no lock, no camera, no system. In fog, rain, smoke, or dark the tier drops to 3; on the cinder in daylight it cannot be attempted at all."}
  - {name: "Be Invited Is The Front Door", text: "Be-invited is tier 3 and is the intended route in: a name, a favor, a debt, a message for an alpha, something to sell, or a reason [[teodora-sowande]] wants to hear. A crew that walks up the siding saying who sent them is not attacked. A crew found inside without that is."}
  - {name: "Every Roof Answers", text: "Whenever the crew takes an action inside the Row that the sentries could notice, the Row may Present a New Challenge: [[pack-on-the-run]], Scale 1, from whichever hall is nearest — and each hall belongs to a different pack, so what arrives may or may not care what the others want."}
  - {name: "Nobody Comes Here", text: "The Chancery's police do not enter the flats and corporate security does not come until first light ([[cinder-yards]]). Anything the crew does here is unwitnessed by the city, which means it is deniable — and which means it does nothing to [[secret-war-goes-public]] (Brief §4.1). It also means nobody is coming for the crew either."}
threats:
  - threat: "Somewhere out on the ash, a fire-barrel is fed and two figures on a roofline stop moving."
    consequences:
      - {text: "The Row knows the crew is on the flats and has known for a while.", statuses: ["watched-3"], tags: []}
      - {text: "The nearest hall sends somebody out to ask. Present a New Challenge: [[pack-on-the-run]], Scale 1, not yet hostile.", statuses: [], tags: []}
  - threat: "The wind turns and the ash comes up off the flats in a wall."
    consequences:
      - {text: "Ash in the eyes, the throat, and every intake and joint the crew is carrying.", statuses: ["blinded-and-choking-3"], tags: []}
      - {text: "Cybernetics and drones foul (burn a tag representing a device, or give it fouled-3).", statuses: [], tags: []}
  - threat: "A hall door opens on a strip light, weight benches, mattresses, and a cage with the door standing open."
    consequences:
      - {text: "The crew sees exactly what the Run is and what it costs (a Baseline or anyone who did not know takes cannot-unsee-it-3).", statuses: ["cannot-unsee-it-3"], tags: []}
      - {text: "Whoever is healing in there is not able to be quiet about it, and the sound carries.", statuses: [], tags: ["somebody in there is not settling"]}
  - threat: "The delivery is due, and the gantry lights over the siding come on."
    consequences:
      - {text: "Three packs, one van, and everyone armed and in a good mood — the worst hour of the week to be a stranger here (see [[the-round]]).", statuses: [], tags: ["delivery night"]}
      - {text: "The crew is seen at the siding on delivery night, and both [[syndicate|the Almoners]] and the alpha now want to know why.", statuses: [], tags: ["seen at the siding"]}
power_sets: []
reuse_of: "Built beside Crumbling Building's navigate structure (Core p. 310) and the alarm structure of Thin Place Shrine (Core p. 311) with the Mythos removed."
---

# The Kiln Row

**Role:** barrier · **Scale:** 2 · **Alias:** *six brick sheds and a lot of ash* · *The Run's home ground, where being seen coming is the whole point.*

Six brick kiln-halls in a line along the old rail siding in [[cinder-yards]]: a pack's kennel or a pack's claim in each, scrap barricades, fire-barrels, a Patched sentry on every roof, and the largest hall — the one with the chimney that still smokes — belonging to [[teodora-sowande]]. In front of all of it, a kilometre of open cinder with nothing on it.

The Row is a **barrier** with no lock in it. There is no security system, no fence worth the name, and nothing to hack; the defense is that everyone inside can see you from four hundred metres away and there is nowhere to be that they cannot. It is the Seat of Power for people who own nothing else ([[cinder-yards]]), and it is the only place on the Foot where a stranger is told out loud whose ground they are standing on.

## Limits

| Limit | Tier |
|---|---|
| get in unseen | 5 (3 in fog, rain, smoke, or dark; impossible in daylight) |
| be invited | 3 |
| get out with it | 4 |

## Tags & statuses

a kilometre of open ash with no cover, scrap barricades and fire-barrels, a sentry on every roof, the chimney that still smokes, cages that were for carcasses · *watched-3*

## Specials

**Seen Coming:** No gate, no lock, no camera, no system. The flats are the defense.

**Be Invited Is The Front Door:** Tier 3, and the intended route: a name, a favor, a debt, a message, something to sell, or a reason the alpha wants to hear. A crew that walks up the siding saying who sent them is not attacked.

**Every Roof Answers:** Any noticed action inside the Row may Present a New Challenge: [[pack-on-the-run]], Scale 1, from the nearest hall — and each hall is a different pack, which may or may not care what the others want.

**Nobody Comes Here:** No police, no corporate security before first light. Everything done here is unwitnessed and therefore deniable, so it does nothing to [[secret-war-goes-public]] (Brief §4.1) — and nobody is coming for the crew either.

## Threats / Consequences

› Somewhere out on the ash, a fire-barrel is fed and two figures on a roofline stop moving.
» The Row has known the crew was on the flats for a while (*watched-3*)
» The nearest hall sends somebody out to ask (Present a New Challenge: [[pack-on-the-run]], not yet hostile)

› The wind turns and the ash comes up off the flats in a wall.
» Ash in the eyes, the throat, and every intake and joint (*blinded-and-choking-3*)
» Cybernetics and drones foul (burn a device tag, or *fouled-3*)

› A hall door opens on a strip light, weight benches, mattresses, and a cage with the door standing open.
» The crew sees exactly what the Run is and what it costs (*cannot-unsee-it-3*)
» Whoever is healing in there cannot be quiet about it (*somebody in there is not settling*)

› The delivery is due, and the gantry lights over the siding come on.
» Three packs, one van, everyone armed and in a good mood (*delivery night*; see [[the-round]])
» The crew is seen at the siding on delivery night (*seen at the siding*)

## Power Sets

None. This is ground.

## Canon and flags

- Bible §2 (packs, kennels, the delivery), §3 (the Masquerade; nobody official comes to the Yards), §4 theme 3; Brief §4.1, §8; roles per Core p. 297. **[TAO-REINTERPRETED]** Built beside Crumbling Building (Core p. 310) and the alarm structure of Thin Place Shrine (Core p. 311) with the Mythos removed — there is nothing mystical in the Yards.
- **[BUILD CHOICE]** (BC-114) the Row as a barrier with no lock, *be invited* at tier 3 as the front door, and the per-hall pack ownership.
