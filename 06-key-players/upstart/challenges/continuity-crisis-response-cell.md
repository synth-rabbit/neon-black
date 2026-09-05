---
type: challenge
name: "Continuity Crisis-Response Cell"
slug: continuity-crisis-response-cell
status: review
source: custom
page: "294–300, 304, 118–120"
owner: WP4-trio1
canon_refs: ["Bible §3 power structure", "Bible §3 corporate security legality", "Bible §5 the inciting incident", "Brief §8", "Core p. 294–300", "Core p. 304", "Core p. 118–120"]
flags: [BUILD CHOICE]
player_safe: false
role: attacker
scale: 2
alias: "emergency services"
short_description: "Six to eight people in matte soft-shell with a serial where a name should be, who arrive before anyone else and declare the scene theirs."
limits:
  - {name: hurt-or-subdue, tier: 4}
  - {name: discredit, tier: 3}
  - {name: negotiate, tier: 999}
  - {name: scene-secured, tier: 4}
default_tags: ["soft-shell armor", "breaching frames", "first on scene", "medical kit"]
default_statuses: ["coordinated-3"]
specials:
  - {name: "For The Duration Of The Emergency", text: "A cell's authority at a scene it has declared is exactly as legal as the city police's (Bible §3). Any attempt to appeal to law, licence, or the Chancery inside a declared scene instead confirms the cell's standing: the cell gains superior-position-2, or Present a New Challenge — a second cell arriving as requested backup."}
  - {name: "Cell Discipline", text: "When the cell takes a status one of its members can take for it, one member takes the status instead and the cell's Scale drops by one. At Scale 0 the last responder standing fights on and the cell can no longer use Overlapping Fields."}
  - {name: "Overlapping Fields", text: "While the cell is at Scale 1 or higher, the first time in a scene that a PC moves into the open against it, the cell delivers a Consequence before the PC's action resolves."}
  - {name: "Cleanup Is The Product", text: "At the end of any scene a cell held, it removes up to two story tags describing evidence, witnesses, or recordings of what happened, and creates the story tag the official version. Removing the official version afterward takes a Tracked action against whoever is quoting it."}
threats:
  - threat: "A grey van with the side door already open stops where nothing was parked a minute ago, and people in soft-shell come out at a walk, not a run."
    consequences:
      - {text: "The cell declares the scene and sets a cordon: nobody in, nobody out, everything on the far side of a line.", statuses: [], tags: ["cordoned", "nobody in, nobody out"]}
      - {text: "A responder puts a hand on someone's shoulder and steers them, calmly, into the wrong room.", statuses: ["contained-2"], tags: []}
  - threat: "A responder holds a breaching frame against a doorway and counts down out loud, so the people inside can hear it."
    consequences:
      - {text: "The frame blows the door and the room with it (concussed-3 and the doorway is gone).", statuses: ["concussed-3"], tags: []}
      - {text: "Two responders come through opposite entrances at once and put everyone on the floor.", statuses: ["pinned-down-3"], tags: []}
  - threat: "The district's lights stutter and every Nearspace overlay in the block goes flat grey."
    consequences:
      - {text: "The cell cuts local power and the Nearspace with it: nobody calls for help, nobody records anything, nothing that runs on a feed works.", statuses: ["cut-off-3"], tags: ["no feed, no witnesses"]}
      - {text: "Doors that were locked are not locked any more, and everyone who was behind them is now in the corridor. Present a New Challenge: whatever the doors were holding.", statuses: [], tags: []}
  - threat: "Two responders walk one person out of the scene at a normal pace, one hand under an elbow, and nobody else is touched."
    consequences:
      - {text: "The extraction completes. Add scene-secured-2. What the cell came for leaves in the van.", statuses: ["scene-secured-2"], tags: []}
      - {text: "The cell spends the rest of the scene not stopping anyone else from running, because the running is the cover.", statuses: [], tags: ["everyone is running"]}
  - threat: "A responder raises a hand and says, in a voice built for frightened people, that everything is under control."
    consequences:
      - {text: "The crowd believes it and stops moving; anyone still trying to act against the cell does so alone (isolated-2).", statuses: ["isolated-2"], tags: []}
      - {text: "Somebody in the crowd decides these are the rescuers and points at the crew. Escalate the Situation.", statuses: [], tags: []}
power_sets: []
reuse_of: ""
---

# Continuity Crisis-Response Cell

**Role:** attacker · **Scale:** 2 (six to eight; a cell at half strength is Scale 1) · **Alias:** *emergency services* · *They arrive before anyone else and declare the scene theirs.*

[[upstart|Continuity Risk & Response]]'s frontline and its product in one object. Matte grey soft-shell, no livery, a serial number on the chest plate where a name would be. Breaching frames, carbines, a medical kit that gets used on bystanders in front of cameras, and four years of training as one animal. They do not shout. They arrive at a walk, and the walk is the frightening part.

A cell holds a scene the way the city police hold one, because corporate security forces are exactly as legal as the police (Bible §3), and Continuity's cells are usually the first authority present at any incident in a district it is retained in — including incidents nobody reported yet.

At [[coldwater-outfall|the Ledger]], a cell dropped the camp's power, cut its Nearspace, opened the block doors, walked one man out through the wire, and let a hundred people run for the causeway (Bible §5). Nothing about that was improvised.

## Limits

| Limit | Tier |
|---|---|
| hurt or subdue | 4 |
| discredit | 3 |
| negotiate | – |
| scene-secured (progress) | 4 |

**negotiate** is immune: a cell does not negotiate on site. Terms are agreed upstairs, by [[rosalind-ekwueme]], before or after — never at the cordon.

**discredit** at 3 is the cheap way through: a cell's authority is entirely social until somebody with a feed proves it is a contractor rather than an emergency service. Maxing it does not remove the cell; it removes *first on scene* and the crowd's cooperation.

**scene-secured** (progress): when it maxes, the cell has what it came for and leaves. Everything still burning stays burning.

## Tags & statuses

soft-shell armor, breaching frames, first on scene, medical kit · *coordinated-3*

## Specials

**For The Duration Of The Emergency:** inside a declared scene the cell's standing is the police's (Bible §3). Appeals to law or the Chancery confirm it — the cell gains *superior-position-3*, or Present a New Challenge: a second cell arriving as requested backup.

**Cell Discipline:** when the cell takes a status a member can take for it, a member takes it and Scale drops by one. At Scale 0, Overlapping Fields stops working.

**Overlapping Fields:** at Scale 1+, the first time a PC moves into the open against the cell in a scene, the cell delivers a Consequence first.

**Cleanup Is The Product:** at the end of a scene it held, the cell removes up to two story tags describing evidence, witnesses, or recordings, and creates *the official version*.

## Threats / Consequences

› A grey van with the side door already open stops where nothing was parked a minute ago.
» Cordon (*cordoned*, *nobody in, nobody out*)
» A hand on a shoulder, steering somebody into the wrong room (*contained-2*)

› A responder holds a breaching frame to a doorway and counts down out loud.
» The frame blows the door and the room with it (*concussed-3*)
» Two entrances at once; everyone on the floor (*pinned-down-3*)

› The lights stutter and every overlay in the block goes flat grey.
» Local power and Nearspace cut (*cut-off-3*; *no feed, no witnesses*)
» Locked doors are not locked any more — Present a New Challenge: whatever they were holding

› Two responders walk one person out at a normal pace, one hand under an elbow.
» The extraction completes (*scene-secured-2*)
» Nobody else is stopped, because the running is the cover (*everyone is running*)

› A responder raises a hand and says everything is under control.
» The crowd believes it (*isolated-2* to anyone still acting)
» Somebody points at the crew (Escalate the Situation)

## Power Sets

None by default. A cell fielded against a hard target adds **Heavily Armed** (Core p. 328). A cell working with the Cold Suite adds **Surveillance Data Fed** (Core p. 333) — see [[the-cold-suite]].

## Canon and flags

- Corporate security exactly as legal as the police: Bible §3. The strike's shape at the Ledger — power cut, doors open, one person walked out, general breakout as cover: Bible §5.
- **[BUILD CHOICE]** (BC-105) the cell's composition, Limits, Specials and Threats are this package's specification of the Bible's "security, crisis management" firm.
- Nothing in this profile is Bloodware. Cells are staffed by contractors who were told a name and a window ([[hanne-oyelaran]]); the twist lives only in [[upstart|Continuity]]'s MC-only section.
