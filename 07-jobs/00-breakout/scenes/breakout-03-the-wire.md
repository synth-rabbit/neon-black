---
type: scene
name: "The Wire"
slug: breakout-03-the-wire
status: review
source: custom
page: "76–113, 118–120, 305, 310"
owner: WP7a
canon_refs: ["Bible §3 corporate security legality", "Bible §5 the inciting incident", "Bible §6 (all)", "Brief §7.1", "Core p. 76–113", "Core p. 118–120", "Core p. 305", "Core p. 310"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
job: breakout
order: 3
set_piece: "The shed row and the fence line behind it, three ways through — the gap the cell cut and is holding, the landing-stage post by the water, and the fifth block's unfinished fence — with a diesel turning over somewhere behind the sheds."
district: coldwater-outfall
story_tags: ["nobody's supposed to be here", "torch line on the yard", "the diesel is turning over"]
challenges: [the-strike-hour, ledger-security-system, ledger-line-security, landing-stage-post, continuity-crisis-response-cell]
book_challenges: ["Security Guard (Core p. 305) — the shift sergeant's torch line, Scale 1, gun for hire", "Crumbling Building (Core p. 310) — the fifth block, half-built, Weak Foundations literal", "Hazard Zone (Core p. 310) — the shed floor, if machinery is run in the dark"]
vectors_active: [hanne-oyelaran, vera-solano, ledger-security-system]
core_moment: false
flashback_hooks: ["The Ledger's routine: which guard counts twice, which shed door sticks, where the fence was patched last winter — a Discover about the route, learned on the line and never used until now.", "The work crew under Rook: the day he walked you past the landing-stage post without either guard looking up, and what he did to make that happen. Establish what you saw; not why he could.", "The shed floor: the shift the quota board was short and the machinery was run past its rate — who got hurt, who covered, what you carry from it (a story tag from the-ledger's tag E or B)."]
outcomes_to_next: ["The crew are through the wire — by the gap, the landing stage, or the fifth block — or on the lagoons in the skiff.", "generators-up stands where the diesel left it (2 or 3); if it maxed here, ledger-security-system is live at alert-2, lockdown-2, and the floodlights are on.", "Anyone who took the landing-stage post's fob and baton has guard-baton-and-fob; anyone who took the shed roll has reclamation-worksheds-toolkit."]
---

# The Wire

![[assets/jobs/breakout/breakout-03-the-wire.png]]

**Job:** [[breakout]] · **Order:** 3 · **District:** [[coldwater-outfall]] · **Story tag:** *nobody's supposed to be here* · **Core moment:** no

## Set piece

Behind the yard, the shed row: four long sheds of corrugated steel where the crew have worked every shift they have been here, doors rolled down for the night, the quota board on the end wall with tonight's number chalked and nothing under it. Behind the sheds, the fence line — chain-link, razor coil, the towers dark — and beyond the fence, on three sides, the lagoons, and on the fourth the causeway. Behind the sheds too, the low brick generator shed, where a diesel the size of a truck is being turned over by two guards and a mechanic with a torch in his teeth, and catching, and dying, and being turned over again.

Three ways through the wire tonight. The crew know all three; two of them Rook showed them.

1. **The gap.** The section the cell dropped flat coming in, forty meters along from the shed row, where the crowd is going and where the torch line is converging. The cell is holding it — two responders at the gap, not stopping anyone, stepping around everyone — and the shift sergeant's line is closing on the same point with a shotgun and the only working authority left in the camp. Whoever goes through the gap goes through the middle of both.
2. **The landing stage.** The shed door that sticks — the third shed, the water side — opens onto the fenced apron where the barges tie up: a concrete stage on the lagoon, a chain-link gate onto it, a guard post of two on a hardship rate ([[landing-stage-post]]), and a maintenance skiff chained to a bollard that nobody has used since the last dredging season. From the stage, a hundred meters of fence to the causeway's foot along the water, or the lagoons themselves ([[the-sludge-flats]]).
3. **The fifth block.** At the far end of the row, the block that was going up when the Series opened: scaffold, half a roof, and a fence line that is posts and no wire for thirty meters because the wire had not been delivered. Crumbling Building (Core p. 310), *Weak Foundations* literal — it is being built by people who are not being paid to build it well — and the shortest dark route to the causeway's foot if the scaffold holds.

Behind all of it, the diesel. Every time it catches, one tower light flickers and holds for a breath.

## Challenges

- [[the-strike-hour]] — countdown. The diesel is its main Threat here: *somewhere beyond the sheds a diesel turns over, catches, dies* (» `generators-up-1`; » a single tower light flickers and holds — *exposed-2* to whoever is under it). *A breaching frame's countdown is heard through a wall*: the cell is blowing the gate house at the causeway's foot for [[breakout-04-the-causeway]]; anyone inside the gate house when it goes takes *concussed-3*. *The block doors bang shut behind the last people out* (» `the-yard-empties-1`; » anyone still inside a block is locked in with the shift: *separated-3*).
- [[ledger-security-system]] — barrier, dormant until `generators-up` maxes. If it does, here: *When The Generators Come Up* — floodlights over the yard and the shed row (*exposed-2* to anyone in the open), the speakers click on, the readers wake (*RFID Fatigues*: uncut collar chips are read at every gate, no roll), the system enters at *alert-2* and `lockdown` 2. **[BUILD CHOICE]** (BC-142).
- [[ledger-line-security]] — barrier. Threats live in the dark: *a guard walks a shed row counting heads, gets a number he does not like, and starts again* (» a second count out of sequence — adds `lockdown-1` only once the system is up; » the nearest body pulled off the line: *separated-3*; Present Security Guard). *The shed klaxon sounds early* cannot fire (no mains). *Debt Is The Lock*: any Consequence here may instead be *arrears-2* — months added by a sergeant who has the crew's numbers by torchlight — which follows them out ([[escapee-recovery-desk]]).
- [[landing-stage-post]] — attacker. Two guards, a rifle and a shotgun, a stun baton and a fob, a chain on a skiff. `hurt or subdue` 3, `bluff` 3, `bribe` 4. *Hardship Rate*: the first tier-2 status they take, they choose between the wire and the water and stop shooting at anyone not shooting at them.
- [[continuity-crisis-response-cell]] — attacker, as hazard, at the gap. *A responder holds a breaching frame against a doorway and counts down out loud* (» the gate house and the room with it: *concussed-3*; » two entrances at once: *pinned-down-3* — only to whoever is inside). *Stepped Around*: through the gap, the cell delivers no Consequence to the crew; the torch line does.
- Security Guard (Core p. 305), Scale 1 — the shift sergeant's torch line, *gun for hire*. Torches, one shotgun, one rifle, and the count in their heads. They are the only law on the fill-rise (Bible §3) and they know the crew's faces.
- Crumbling Building (Core p. 310) — the fifth block, if the crew go that way. *Weak Foundations*; scaffold that was not finished; a roof that is half a roof.
- Hazard Zone (Core p. 310) — the shed floor, only if somebody starts the machinery in the dark for cover or for a weapon.

## Vectors active

- [[hanne-oyelaran]] — push: the gap held, the gate house blown, Rook walked through the middle of it toward the causeway. `contract-complete` climbs by 1 when the gate goes.
- [[vera-solano]] — push: the sergeant, the torch line, the diesel, and the arrears column read into a torch beam. Want: a number she can give the Stack.
- [[ledger-security-system]] — the diesel. `generators-up` is the scene's clock.

## Flashback slots

Prompts only (Core p. 125). A Flashback here is the heist pattern — a Discover in hindsight about a route the crew learned on the line — and its Consequence may be the same as the book's: the PC ran out of past, and has no Flashback left.

- **The Ledger's routine.** Which guard counts twice; which shed door sticks; where the fence was patched last winter and with what. — a Discover about the route: create a story tag for the scene (*the door that sticks*, *the patched section*, *the sergeant counts the third shed twice*).
- **The work crew under Rook.** The day he walked you past the landing-stage post and neither guard looked up, and what he did to make that happen. Establish what you *saw* — the thug story told again, a load moved, a guard's name used — and nothing about why he could ([[tomas-adair]]: Texture only; OQ-10).
- **The shed floor.** The shift the quota board was short and the machinery was run past its rate; who got hurt, who covered, what you carry from it. — a story tag from [[the-ledger]] (tag B *learned to carry more than I thought I could* or tag E *scarred where the work sheds left their mark*) for the rest of the session.

## What carries forward

- The crew are through the wire — by the gap, the landing stage, or the fifth block — onto the apron at the causeway's foot ([[breakout-04-the-causeway]]); or on the lagoons in the skiff ([[the-sludge-flats]]), which is the route past the causeway entirely and rejoins the job at [[breakout-05-a-name-and-a-place]] by the coast road.
- `generators-up` stands where the diesel left it. If it maxed here, [[ledger-security-system]] is live: *alert-2*, `lockdown` 2, floodlights on, readers reading collar chips.
- Loadout: [[guard-baton-and-fob]] from the landing-stage post (the fob opens the apron gate once the mains are back, and reports the guard's name when it does); [[reclamation-worksheds-toolkit]] from the third shed (pry bar, cutters, torch — and the camp's inventory marks stenciled on the roll); [[ledger-issue-fatigues]] on everyone's back, collar chips uncut unless someone used the cutters on the seam.

## Canon and flags

- Corporate security as the only law on the fill-rise (Bible §3); the camp's layout — sheds, fence, towers, landing stage, causeway, the fifth block under construction — from [[coldwater-outfall]] (BC-24) and [[corp-c]]; the strike's method from [[continuity-crisis-response-cell]].
- **[BUILD CHOICE]** (BC-141) the landing-stage post and the generator shed as scene locations; the skiff as a third exit; (BC-142) the generator clock and what wakes when it maxes.
- **[OPEN]** (OQ-38) the sheds and the quota board: a number chalked, nothing under it; the product line proposed in [[breakout]] is strikeable and nothing here depends on it.
