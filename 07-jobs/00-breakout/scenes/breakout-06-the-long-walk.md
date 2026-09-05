---
type: scene
name: "The Long Walk"
slug: breakout-06-the-long-walk
status: review
source: custom
page: "42, 76–113, 124"
owner: WP7a
canon_refs: ["Bible §3 haves and have-nots", "Bible §3 corporate security legality", "Bible §6 standing after the breakout", "Brief §7.1", "Core p. 42", "Core p. 76–113", "Core p. 124"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
job: breakout
order: 6
set_piece: "Four in the morning on the coast road into the Sinks — stilt-walks locked at every landing, the pumps running late, the Wall a grey line with a gold top on the horizon — and a joint post where the road enters the Gullet's shore end, asking five people in camp fatigues for papers."
district: lowmere-sinks
story_tags: ["the pumps are running late", "nobody official comes down here", "five in camp fatigues"]
challenges: [escapee-list, chancery-checkpoint, pack-on-the-run]
book_challenges: ["Hazard Zone (Core p. 310) — the flooded streets at high tide, if the crew leave the levee road", "Security Guard (Core p. 305) — the post's AP&I half, Scale 1"]
vectors_active: []
core_moment: false
flashback_hooks: ["Crew bonds: who under the Wall you last saw before the camp, and who might still be there — a name the crew can use tonight, or a name that is a problem. Where, with whom; not what you saw.", "Why you were here: the night you understood you were going to be sent somewhere for it — who told you, and what you did with the hours you had left. Content stays yours.", "The night you were sorted: the barge along this coast, or the truck through the Stack — the last thing you saw of the Under going in, and whether it is still there."]
outcomes_to_next: ["The crew are inside the Gullet's shore end, at the fishing shacks past the locks, with the market's roof ahead and the quay beyond it.", "escapee-list's noticed stands at 1 or 2 — the checkpoint's scanner and its call-in are its Threats here.", "Whoever passed the post has the story tag the price was paid, or broke a checkpoint, or is still on the far side of it."]
---

# The Long Walk

**Job:** [[breakout]] · **Order:** 6 · **District:** [[lowmere-sinks]] (or [[kilbride-stretch]], see below) · **Story tag:** *the pumps are running late* · **Core moment:** no

## Set piece

The coast road runs west from the Outfall along the levees, and the first thing it reaches is the Sinks.

Four in the morning. The haze thins and becomes ordinary rain. On the left, the sea; on the right, below the levee, a district a meter under water — the ground floors of everything abandoned a generation ago, life moved up to the second storey and the roofs, plank bridges and cable-ways strung between rooftops across streets that are canals tonight because the tide is in and the pumps, as they say here, are running late. Every landing on every stilt-walk is locked. Nobody in the Sinks opens a landing to strangers at this hour, and five people in grey AP&I fatigues with numbers on the back, wet to the waist, walking in from the direction nobody walks in from, are strangers. Faces watch from the rooftops. The pump-house on the levee — Pump-house Six, a brick fortress with four diesels the size of trucks — has its lights on and its door shut.

This is the Under (Core p. 42): "blank spots in the surveillance net," "almost every part … someone's turf." The Run hunts here at night — packs come down from the Yards across the levees, and the families lock the walks and wait for dawn — and a pack going home along the levee at four in the morning is the one thing on this road the crew should not be.

The Wall is ahead the whole way. From the Sinks it fills the western sky: a grey face the height of the weather, tier-lights in bands, the Crest a line of white and gold along the top, lit as it is lit at every hour. The Gullet is at its foot, where the run-off channel comes out — a dark notch in the base of the Wall with the port's cranes against it and a roof of corrugated plastic glowing from beneath. Two hours' walk. Everything the crew own is on their backs and stenciled with the Ledger's inventory marks.

**The post.** Where the coast road enters [[gullet-market]] at the shore end — the fishing hamlet past the locks, stilt shacks and smokehouses on the flood line — a joint post: a Chancery constable in a booth with a heater, and, this month, an AP&I security contractor beside him, because the Stack's logistics office pays for a man on the shore road ([[chancery-checkpoint]]: corporate security exactly as legal as the police, Bible §3). A scanner on a pole. A price list that is unwritten and known. And, on the AP&I contractor's slate, nothing yet about the Outfall — the Ledger has not been said out loud to anyone by anyone, and will not be ([[corp-c]]: *keep the Ledger unsaid*).

Five in camp fatigues, though, is a thing a contractor notices.

**Ways past the post:** the price (the Chancery's, `bribe` 2 — it is always available); papers (none; `bluff or present papers` 3 — a story that five people in AP&I-stamped grey are a work detail walking off a shift, which is true); force (`force-through` 4 — *broke a checkpoint* follows the crew into the Gullet and *wanted-2* in the district on their first morning); around — the fishing hamlet's shacks are on stilts over the flood line and the smokehouse crews do not love the post; or the water — a fishing skiff for whatever the crew can pay.

## The other road

**[[kilbride-stretch]]** (story tag *nobody official comes down here*). If the crew leave the coast road for the levee causeways inland, the Stretch is the sprawl: kilometers of prefab grid, automats, drone-lanes overhead, a police station every ten kilometers that does not leave its walls. Dawn there is the Kilbride Interchange — the bus terminus, the service-lift depot where the Crest's domestic staff queue at first light in company greys not so different from the Ledger's — and five more grey coats in that queue are nothing anyone looks at twice. The post then is the Interchange's tier-lift checkpoint rather than the shore road's, same profile ([[chancery-checkpoint]]), staffed by the Chancery alone, and the way into the Gullet is down the Foot's grid under the Stack's bottom bays. Longer; drier; more cameras, all of them the Chancery's. The choice is the crew's and the scene runs the same.

## Challenges

- [[escapee-list]] — watcher. *A face in a crowd-scan flags a partial match to Ledger intake photos* — the post's scanner (» `noticed-1`, quietly). *An RFID reader somewhere logs a signature that shouldn't exist anymore* — the same scanner reads collar chips ([[ledger-issue-fatigues]], *broadcasts your location if not stripped*) if nobody cut the seam (» `noticed-1`, *a name goes on the list*). *Not Worth the Bounty*: nothing here becomes a hunting party. In session one `noticed` ends at 2 at most (**[BUILD CHOICE]** BC-145).
- [[chancery-checkpoint]] — barrier, Scale 1. *A guard steps out and raises a hand, palm out* (» *stopped-2*); *a scanner beeps on a bag, a body, or a piece of gear* (» *flagged-2* — the shed toolkit's stencils, a collar chip, a guard's fob); *radios crackle; the post calls it in* (» `alert-1`; » if bluff and bribe both fail, Present Security Guard, Core p. 305, Scale 1, in AP&I colors). *Exactly as Legal as the Police*: on this road the AP&I half of the post is who answers a failed bribe. `bribe` maxed: *the price was paid*, and `alert` is gone.
- [[pack-on-the-run]] — pursuer, Scale 1, **optional**: four to six of the Run going home along the levee from a night in the Sinks, *settled-3* and coming down. *Not Worth It* (`convince-them-you're-not-worth-it` 3) is the intended exit; a crew in camp grey with nothing to take is nearly there already. *It Was A Gang Fight* covers whatever happens. If a PC is a Howler, the pack knows it at forty meters and the scene is a different conversation; the file does not write it.
- Hazard Zone (Core p. 310) — the flooded streets at high tide, only if the crew leave the levee road for the stilt-walks. *Poison* is the water.
- Security Guard (Core p. 305), Scale 1 — the post's AP&I contractor, if it comes to that. *Gun for hire.*

## Vectors active

None. The Ledger's vectors ended at the causeway (*No Bounty Beyond The Wire*); Continuity's went west in the van; the fence's begins at the counter door. This scene is the Under with nobody pushing on the crew but the city itself, which is the point of it.

## Flashback slots

Prompts only (Core p. 125). The walk is long and the slots are the walk's.

- **Crew bonds — who is out here.** Who under the Wall you last saw before the camp, and who might still be there: a name the crew can use tonight, or a name that is a problem. *Where, with whom* — not what you saw. May create a relationship story tag with an NPC the player names, or a story tag between two PCs who knew the same person.
- **Why you were here — the hours you had left.** The night you understood you were going to be sent somewhere for it: who told you, and what you did with the time between knowing and the truck. Content stays the player's ([[saw-something-i-shouldnt]]; OQ-12); the prompt asks for the shape of the night, not the thing at its center. May fill weakness D on that kit (*what sets off the worst of it*) as a story tag for the Gullet.
- **The night you were sorted — the coast.** The barge along this shore, or the truck through the Stack: the last thing you saw of the Under going in, and whether it is still there when you look now. A Discover about the Gullet or the Sinks as they were; the MC answers with what changed.

## What carries forward

- The crew are inside the Gullet's shore end — the fishing shacks past the locks, the smokehouses, the market's roof ahead and the quay beyond it ([[breakout-07-the-counter-door]]) — or at the Interchange lift on the Stretch, an hour further off.
- [[escapee-list]] `noticed` at 1 or 2. *The List Doesn't Forget*.
- The post: *the price was paid*, or *broke a checkpoint* and *wanted-2* in [[gullet-market]], or a story about a work detail that held.
- Loadout still on their backs: [[ledger-issue-fatigues]], and whatever came out of the sheds. The first thing Tally will do is weigh it.

## Canon and flags

- The Under as the caste bottom; the Sinks below sea level and the Run's hunting ground; the Stretch as the sprawl and the Interchange's dawn queue; the Gullet's shore end as a fishing hamlet: [[lowmere-sinks]], [[kilbride-stretch]], [[gullet-market]] (BC-17). Corporate security's legality and the joint post: Bible §3; [[chancery-checkpoint]]. Escapee list, no bounty: Bible §6.
- **[BUILD CHOICE]** (BC-141) the coast road and the shore-road post as scene locations; (BC-145) `noticed` capped at 2 in session one.
- **[OPEN]** (OQ-14) the Sinks assert nothing about Tao on this road; a Caster PC who notices something in the marsh is answered with weather. (OQ-13) five in camp fatigues walking together is a fact the post sees and nobody explains.
