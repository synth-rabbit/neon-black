---
type: challenge
name: "The Landing-Stage Post"
slug: landing-stage-post
status: review
source: custom
page: "294–300, 305, 118–120"
owner: WP7a
canon_refs: ["Bible §3 corporate security legality", "Bible §5 the camp", "Bible §6", "Brief §7.1", "Brief §8", "Core p. 294–300", "Core p. 305", "Core p. 118–120"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: attacker
scale: 1
alias: "two torches by the water"
short_description: "The guard post on the Ledger's barge landing stage: two AP&I contractors on a hardship rate, a rifle and a shotgun, a stun baton and a gate fob, a chain on a skiff — and the shortest line from the shed row to the water."
limits:
  - {name: hurt-or-subdue, tier: 3}
  - {name: bluff, tier: 3}
  - {name: bribe, tier: 4}
default_tags: ["a rifle and a shotgun between them", "the apron gate's fob", "the skiff's chain", "hardship rate"]
default_statuses: ["nervous-2"]
specials:
  - {name: "Hardship Rate", text: "These two are gun for hire (Core p. 305), posted to a drainage waste at a rate that says so. The first time this Challenge takes a status of tier 2 or higher, its guards choose between the wire and the water and stop shooting at anyone who is not shooting at them; hurt-or-subdue is then reached with any further tier. They will not die for a landing stage."}
  - {name: "The Fob And The Baton", text: "Overcoming this Challenge by any Limit yields [[guard-baton-and-fob]]: the apron gate's fob opens the landing-stage gate now (the gate house generator does not feed it; the chain does), and once the mains return it opens whatever this post's guard could open — and logs his name at every reader it touches."}
  - {name: "The Skiff", text: "A maintenance skiff, outboard motor, chained to a bollard at the stage's end, unused since the last dredging season. Its chain is a Quick Outcome with the cutters from the shed roll ([[reclamation-worksheds-toolkit]]) and a Tracked one without. On the water, this Challenge cannot follow; Present a New Challenge: [[the-sludge-flats]] by water."}
  - {name: "Rook's Way", text: "The third shed's water-side door — the one that sticks — opens onto this apron, and the crew have been walked past this post before without either guard looking up ([[tomas-adair]]). A Flashback establishing how gives the crew a story tag for this scene (the guard who counts twice is on the far side tonight; the door that sticks; the gap in the apron fence) and asserts nothing about why Rook could."}
threats:
  - threat: "A torch beam swings off the water and across the apron, looking for the source of the noise."
    consequences:
      - {text: "It finds someone (lit-2, and the other guard turns).", statuses: ["lit-2"], tags: []}
      - {text: "It finds nothing, and the guard calls it in on a radio with nothing on the other end (Deny Them Something They Want: the guard's attention is on the shed door now).", statuses: [], tags: ["the shed door is watched"]}
  - threat: "The rifle comes up to the shoulder and a voice says stop where you are, in a tone that has never had to mean it."
    consequences:
      - {text: "Aimed fire, one target (gunshot-wound-3).", statuses: ["gunshot-wound-3"], tags: []}
      - {text: "A warning shot into the lagoon, and both guards are now committed to this (this Challenge loses nervous-2 and gains alert-2).", statuses: ["alert-2"], tags: []}
  - threat: "The stun baton comes out of its ring, and the guard holding it moves to put the apron gate between himself and the crew."
    consequences:
      - {text: "The baton (stunned-2).", statuses: ["stunned-2"], tags: []}
      - {text: "The apron gate is shut and the fob is on the far side of it (Deny Them Something They Want).", statuses: [], tags: ["the apron gate is shut"]}
  - threat: "One guard shouts for the sergeant, toward the shed row, as loud as he can."
    consequences:
      - {text: "The torch line turns toward the water. Present a New Challenge: Security Guard (Core p. 305), Scale 1, arriving along the shed row in two minutes.", statuses: [], tags: []}
      - {text: "The other guard uses the shout to get to the skiff first and is untying it (the-yard-empties-1 on [[the-strike-hour]]; the skiff is leaving without them).", statuses: [], tags: ["the skiff is leaving"]}
power_sets: []
reuse_of: "Security Guard, Core p. 305 (gun for hire), as a specific post"
---

# The Landing-Stage Post

**Role:** attacker · **Scale:** 1 (two guards and a gate) · **Alias:** *two torches by the water* · *The shortest line from the shed row to the water.*

A specific guard post inside [[coldwater-outfall|the Ledger]], for [[breakout-03-the-wire]]. The book's Security Guard (Core p. 305) is the generic — [[corp-c-reuse]] resolves its *(courageous or gun for hire or loyal)* to **gun for hire** at Coldwater, where the posting is a hardship rate — and this is that guard, twice, at the one post the crew know a way past.

The landing stage is the concrete apron on the lagoon where the barges tie up: a chain-link gate onto it from the shed row, a bollard, a mooring, a lamp on a post that is dark tonight like everything else, and a maintenance skiff nobody has used since the last dredging season. Two guards on the night post, one with a rifle and one with a shotgun, a stun baton and a fob between them, and a radio with nothing on the other end. They have been listening to the yard for twenty minutes and have not been told anything, because there is nobody to tell them. They are exactly as legal as the police (Bible §3), and they know it, and they are not paid enough for it.

## Limits

| Limit | Tier |
|---|---|
| hurt or subdue | 3 |
| bluff | 3 |
| bribe | 4 |

**bluff** at 3: five people in camp greys walking onto the apron with a story — a work detail sent to secure the barge, a sergeant's order relayed by torch — is a story two frightened men on a hardship rate want to believe. **bribe** at 4: lower than the routine's 5 ([[ledger-line-security]]), because the routine is a shift and these are two men alone by the water; still not cheap, because a guard who takes money gets a note in his own account.

## Tags & statuses

a rifle and a shotgun between them, the apron gate's fob, the skiff's chain, hardship rate · *nervous-2*

## Specials

**Hardship Rate:** the first tier-2 status, and they choose between the wire and the water.

**The Fob And The Baton:** overcoming them yields [[guard-baton-and-fob]].

**The Skiff:** a chain, a Quick Outcome with cutters; on the water — Present [[the-sludge-flats]] by water.

**Rook's Way:** a Flashback establishes how the crew were walked past this post before; a story tag, and nothing about why.

## Threats / Consequences

› A torch beam swings across the apron.
» Someone is lit (*lit-2*)
» Nothing, and the guard's attention is on the shed door (*the shed door is watched*)

› The rifle comes up and a voice says stop.
» Aimed fire (*gunshot-wound-3*)
» A warning shot, and both are committed (*alert-2*, *nervous-2* removed)

› The baton comes out and the guard puts the gate between them.
» The baton (*stunned-2*)
» The gate is shut and the fob is on the far side (*the apron gate is shut*)

› One guard shouts for the sergeant.
» Present a New Challenge: Security Guard (Core p. 305), Scale 1, two minutes out
» The other guard is untying the skiff (*the skiff is leaving*; *the-yard-empties-1*)

## Power Sets

None. **Heavily Armed** (Core p. 328) belongs to the line after lockdown, not to two men on a dock.

## Canon and flags

- Corporate security's legality; the camp, its landing stage, and the barge line: Bible §3, §5; [[coldwater-outfall]] (BC-24); the gun-for-hire reading of the Ledger's posts: [[corp-c-reuse]].
- **[BUILD CHOICE]** (BC-141) the landing-stage post as a named scene location and the skiff as a third exit; (BC-148) tiers, Specials, and Threats.
- **[OPEN]** (OQ-10) *Rook's Way* grants a story tag about what the crew saw and never about what he is or why he could.
