---
type: challenge
name: "The Reach Armory Seal"
slug: reach-armory-seal
status: review
source: custom
page: "294–300, 319–320"
owner: WP4-trio3
canon_refs: ["Bible §2 mage", "Bible §3 power structure", "Brief §8", "Plan A.6", "Core p. 43", "Core p. 294–300", "Core p. 319–320"]
flags: [BUILD CHOICE, TAO-REINTERPRETED, OPEN]
player_safe: false
role: barrier
scale: 2
alias: "a very boring building"
short_description: "Orison's headquarters block and the layered seal that keeps everything — and everyone — inside it, ending at an airlock with no maintenance history."
limits:
  - {name: get-inside, tier: 5}
  - {name: reach-the-sealed-shop, tier: 6}
  - {name: wreck, tier: 6}
  - {name: take-over-or-shut-down, tier: 5}
default_tags: ["layered checkpoints", "a Nearspace so hardened it reads as dead", "drone coverage over the neck of the headland", "manifest-matched cargo", "the shop airlock, with no maintenance history"]
default_statuses: ["alert-1", "sealed-4"]
specials:
  - {name: "Reads As Dead", text: "The Armory's Nearspace is not defended, it is absent: no data fog, no AR, no handshake, nothing to hack. Cyberspace and Harnessing actions against the Armory from outside do nothing at all — treat take-over-or-shut-down as immune from outside the wall. Inside the wall it works normally, which is why everything Orison does about intruders is physical."}
  - {name: "Nothing Leaves Open", text: "Every case, crate, and pallet crossing the seal is manifest-matched twice, and a mismatch is not an alarm — it is a hold. Goods that fail the match are impounded unopened and referred to Product Integrity. Smuggling something out of the Armory is a get-inside problem run backwards; smuggling something out *opened* is impossible."}
  - {name: "The Shop Does Not Appear", text: "The sealed shop under the Armory is on no floor plan, no evacuation diagram, no maintenance schedule, and no fire certificate. Rolls to find it using Orison's own records, systems, or staff cannot max reach-the-sealed-shop; the Limit only moves through physical presence below the executive floors, or through someone who has been inside."}
  - {name: "Forty-One Faces", text: "Exactly forty-one technicians hold shop access and none has ever been rotated, replaced, or promoted. Impersonating one requires a face the door has already seen; impersonating anybody else gets you as far as the executive floors and no further."}
  - {name: "Drills, Not Alarms", text: "When alert reaches 3, the Armory does not sound an alarm — it runs a drill. Corridors seal in a published sequence, staff walk to marked squares, and the drill is over in four minutes. Anyone not on a marked square at the end of it is standing alone in an empty corridor with the drone coverage looking at them."}
threats:
  - threat: "A checkpoint officer takes the crew's credentials, does not hand them back, and asks them to wait in a room with one door."
    consequences:
      - {text: "The credentials are being run against the manifest and the day's roster (waiting-under-guard-3).", statuses: ["waiting-under-guard-3"], tags: []}
      - {text: "Present a New Challenge: Product Integrity Recovery Team, or Security Guard, Scale 1 (Core p. 305), as Orison house security.", statuses: [], tags: []}
  - threat: "The corridor lights change colour and a calm recorded voice begins a numbered sequence."
    consequences:
      - {text: "A drill. The section seals in four minutes and the crew is inside a shrinking box (sealed-in-4).", statuses: ["sealed-in-4"], tags: []}
      - {text: "The drill's roster is read out at the end; a name that does not answer is a name that is looked for (identified-2).", statuses: ["identified-2"], tags: []}
  - threat: "A drone drops off the coverage grid over the neck of the headland and holds station, low, without pinging anything."
    consequences:
      - {text: "It is watching, not scanning — it has no radio traffic to intercept and nothing to spoof (watched-with-no-way-to-tell-3).", statuses: ["watched-with-no-way-to-tell-3"], tags: []}
      - {text: "Present a New Challenge: Surveillance Drone (Core p. 320), re-flavoured as Orison range equipment, or a Gun Turret at the neck (Core p. 319).", statuses: [], tags: []}
  - threat: "The freight lift will only go down to the executive floors, and the button below them is not a button."
    consequences:
      - {text: "The shop is one floor further down than anyone can reach, and reach-the-sealed-shop does not move (Deny Them Something They Want).", statuses: [], tags: []}
      - {text: "The lift logs the attempt. The next scene in the Armory begins with the crew already on a list (in-the-company-books-3).", statuses: ["in-the-company-books-3"], tags: []}
  - threat: "The airlock at the bottom cycles, and one of forty-one people in gloves comes out carrying a case that has not been opened."
    consequences:
      - {text: "The crew sees a Pattern Four core leave the shop and cannot get near it; the door is shut before the case is out of sight (Make the Future Bleaker).", statuses: [], tags: ["you have seen the door"]}
      - {text: "The technician looks at them, says nothing, and goes back inside. Product Integrity is in the building within the hour (Escalate the Situation).", statuses: [], tags: []}
power_sets: []
reuse_of: "Extends Security System (Core p. 319) to building Scale; supporting profiles are Gun Turret (Core p. 319), Surveillance Drone (Core p. 320), and Security Guard (Core p. 305)."
---

# The Reach Armory Seal

**Role:** barrier · **Scale:** 2 (a building and its perimeter) · **Alias:** *a very boring building* · *Orison's headquarters block and the layered seal that keeps everything — and everyone — inside it.*

A squat windowless block at the neck of the headland with the company name on it in letters a metre high, and, unusually for a corporate headquarters, nothing else: no plaza, no lobby art, no public floor, no AR. Executive floors underground, armories below those, and below the armories a shop that is on no plan ([[orison-reach]]).

The Armory is the hardest Secured Site on the Wall (Core p. 43) and its hardness is unfashionable. There is no ICE to duel with, no Domain to walk into, no system to take over from a parked van, because there is nothing to reach: the Nearspace stops at the wall. What there is instead is checkpoints, manifests, drills, drone coverage over open ground, and a workforce that has been doing the same drill for thirty years. Every acquisition job in Palisade is measured against it and most are not attempted.

**[TAO-REINTERPRETED]** (CR-1) Nothing in this Challenge is mystical. The seal is architecture, procedure, and patience; what it is protecting is a practice, and the practice is not what stops the crew — the doors are.

## Limits

| Limit | Tier |
|---|---|
| get inside | 5 |
| reach the sealed shop | 6 |
| wreck | 6 |
| take over or shut down | 5 (immune from outside the wall — see *Reads As Dead*) |

## Tags & statuses

layered checkpoints · a Nearspace so hardened it reads as dead · drone coverage over the neck of the headland · manifest-matched cargo · the shop airlock, with no maintenance history · *alert-1* · *sealed-4*

## Specials

**Reads As Dead:** The Armory's Nearspace is absent rather than defended. Cyberspace and Harnessing actions from outside the wall accomplish nothing; *take over or shut down* is immune from outside and normal inside.

**Nothing Leaves Open:** Everything crossing the seal is manifest-matched twice. A mismatch is a hold, not an alarm: impounded unopened, referred to [[product-integrity-team|Product Integrity]].

**The Shop Does Not Appear:** The sealed shop is on no plan, diagram, schedule, or certificate. *Reach the sealed shop* cannot be moved through Orison's own records, systems, or staff — only through physical presence below the executive floors, or through someone who has been inside.

**Forty-One Faces:** Exactly forty-one technicians hold shop access; none has ever been rotated. Wearing one of those faces gets a Doppel to the airlock. Wearing any other face gets anyone to the executive floors and no further.

**Drills, Not Alarms:** At *alert-3* the Armory runs a drill instead of raising an alarm — a published four-minute sequence of sealing corridors and marked squares. Whoever is not standing on a square at the end is alone in an empty corridor being looked at.

## Threats / Consequences

› A checkpoint officer takes the crew's credentials, does not hand them back, and asks them to wait in a room with one door.
» The credentials are being run (*waiting-under-guard-3*)
» Present a New Challenge: [[product-integrity-team]], or Security Guard, Scale 1 (Core p. 305)

› The corridor lights change colour and a calm voice begins a numbered sequence.
» A drill; the section seals in four minutes (*sealed-in-4*)
» A name that does not answer the roster is a name that gets looked for (*identified-2*)

› A drone drops off the grid over the neck of the headland and holds station without pinging anything.
» Watching, not scanning; nothing to intercept, nothing to spoof (*watched-with-no-way-to-tell-3*)
» Present a New Challenge: Surveillance Drone (Core p. 320) as Orison range equipment, or Gun Turret (Core p. 319)

› The freight lift will only go down to the executive floors, and the button below them is not a button.
» The shop is one floor further than anyone can reach (Deny Them Something They Want)
» The lift logs the attempt (*in-the-company-books-3*)

› The airlock cycles and one of forty-one people in gloves comes out with a case that has not been opened.
» The crew sees a Pattern Four core leave the shop and cannot get near it (*you have seen the door*; Make the Future Bleaker)
» The technician says nothing and goes back in; Product Integrity arrives within the hour (Escalate the Situation)

## Power Sets

None. The supporting profiles carry any overlays: **Heavily Armed** (Core p. 328) on house security during a drill.

## Canon and flags

- Orison keeps an army openly because the civil agreements allow it (Bible §3); the Wuji's control is invisible in the district ([[orison-reach]], BC-18).
- **[BUILD CHOICE]** (BC-116) the sealed shop, the forty-one technicians, and the seal's design; (BC-118) the name *the sealed shop*.
- **[TAO-REINTERPRETED]** (CR-1) the shop holds a practice, not a relic of a legend; the barrier itself is entirely mundane.
- **[OPEN]** (OQ-15) the Armory's dead Nearspace is dead because it is switched off, not because of anything Tao; nothing here decides whether Tao touches cyberspace.
