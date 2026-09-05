---
type: scene
name: "The Causeway"
slug: breakout-04-the-causeway
status: review
source: custom
page: "76–113, 118–120, 302, 319, 320"
owner: WP7a
canon_refs: ["Bible §3 corporate security legality", "Bible §5 the inciting incident", "Bible §6 standing after the breakout", "Brief §7.1", "Core p. 76–113", "Core p. 118–120", "Core p. 302", "Core p. 319", "Core p. 320"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
job: breakout
order: 4
set_piece: "The causeway gate, down, with a truck held on the far side and its engine running; a hundred people against it; and beyond it three kilometers of raised road with no cover — floodlit at the camp end, dark after, and the dark is where the Under begins."
district: coldwater-outfall
story_tags: ["nobody's supposed to be here", "everyone at the gate", "no cover for three kilometers"]
challenges: [the-strike-hour, ledger-security-system, ledger-line-security, continuity-crisis-response-cell, hanne-oyelaran-challenge, the-sludge-flats, escapee-list]
book_challenges: ["Gun Turret (Core p. 319) — on the gate, only at lockdown 6", "Surveillance Drone (Core p. 320) — AP&I perimeter drone over the lagoons, launched when the mains return", "Flying Taxi Driver (Core p. 302) — the truck driver, a Stack logistics contractor, as a civilian transit worker"]
vectors_active: [hanne-oyelaran, vera-solano, ledger-security-system]
core_moment: false
flashback_hooks: ["Why you were here — the road, not the room: the last time you were on a road out of somewhere at night, before the Ledger, and who was driving. Where, with whom, what it cost. Not what you saw.", "The night you were sorted — the causeway the other way: the truck's tailgate, the gate going up, the first floodlight. What you told yourself then about how long this would be."]
outcomes_to_next: ["The crew are past the dark end of the causeway on the coast road, or in the flats beside it, or in the truck.", "ledger-security-system is live behind them at whatever lockdown reached; past the causeway's far end it does not pursue (No Bounty Beyond The Wire).", "escapee-list's noticed stands at 1 (a drone over the lagoons; collar chips read at the gate if the mains were up) or 0 if nothing read them.", "The cell and Rook are ahead of the crew on the road, or the van is already at the turn."]
---

# The Causeway

![[assets/jobs/breakout/breakout-04-the-causeway.png]]

**Job:** [[breakout]] · **Order:** 4 · **District:** [[coldwater-outfall]] · **Story tag:** *nobody's supposed to be here* · **Core moment:** no · **Climax**

## Set piece

The causeway gate is the only light in the Outfall, and it is down.

A steel barrier across the head of the road, a gate house beside it with one window lit, a floodlight on a mast over both, all of it on the gate house generator — the one thing the strike did not cut. On the far side of the barrier a truck, held, its engine running, its driver a logistics contractor from the Stack who arrived with a manifest and has spent the last twenty minutes watching the camp go dark through his windscreen. On the near side, a hundred people, arriving at a run, stopping because there is nowhere to go, and pressing.

Past the gate: **the causeway**. Three kilometers of raised road across the sludge-flats, two lanes wide, a meter above the crust, a rail on one side and nothing on the other. Floodlit for the first two hundred meters by the gate mast; dark after that, all the way to the coast road. No cover. Nothing to hide behind but distance. On either side, the lagoons — concrete-edged pools and flats under a haze that catches the gate light and turns it yellow — and the smell of everything Palisade flushes.

And at the far end, for the first time from the outside: **the Under**. A scatter of lights along the coast that is [[lowmere-sinks|the Sinks]], whatever still works; further off, the flat glow of [[kilbride-stretch|the Stretch]] with the drone-lanes blinking over it; and on the horizon, a grey line the height of the sky with a band of white and gold along its top — the Wall, seen from the bottom, from the wrong end of the map. The Crest is a kilometer straight up and a lifetime away. The Gullet is at its foot, where the run-off comes out.

**Getting through the gate.** Four ways, and the crowd takes the first that opens:

- The cell blows the gate house. This is what the cell came to do — its contract is on the near side of the barrier and the van is on the far side — and the breaching-frame countdown from [[breakout-03-the-wire]] ends here. The gate house goes; the barrier's control goes with it; the barrier stays down, but it is a barrier and not a wall, and a hundred people go over it.
- Over the barrier, before the cell arrives, into the truck's headlights.
- Through the gate house, if somebody with [[guard-baton-and-fob]] reaches the panel first — the fob opens the barrier only if the gate house generator is feeding the panel, which it is.
- Off the road, into the flats ([[the-sludge-flats]]), for anyone who decides the causeway is a killing ground and the lagoons are not.

**The walk.** Three kilometers at a run, in fatigues, in a crowd that thins as it goes. Two hundred meters of floodlight, then dark. The truck, if anyone took it, goes past everyone. Behind them, the diesel.

**When the generators come up** — during the walk, at the crew's back — the camp's floodlights return all at once, every tower, and the speakers click on, and [[vera-solano|Solano]]'s voice reads the count into an empty yard: *Block One. Block Two. Block Three —* and the difference, and the silence. On the causeway the crew are either past the reach of the tower lights or on the lit road with their backs to them. The readers wake: anyone whose collar chip passed the gate reader after this moment is logged, by number, at the causeway gate, leaving. [[ledger-security-system]] is live at *alert-2*, `lockdown` 2. A perimeter drone lifts off the administration block roof and goes out over the lagoons, and [[escapee-list]] begins.

**At lockdown 6** — if the count out of sequence, the gate line going hot, and a reader chime on every collar seam in a running crowd have all been voiced — the Ledger is sealed: Gun Turret (Core p. 319) on the gate mast, live and facing *out*; the causeway lit end to end; guards at Scale +1 at the gate. Anyone still on the lit road is *pinned-in-the-open-3*; the way off the road is the flats. Past the far end of the causeway nothing from the camp follows (*No Bounty Beyond The Wire*).

## Challenges

- [[the-strike-hour]] — countdown, ending. *The crowd hits the causeway gate and stops* (» *trampled-2*; » `the-yard-empties-2` and *everyone at the gate*). *The diesel turns over* (» `generators-up-1`). When `generators-up` maxes: *When The Generators Come Up*, and this Challenge ends.
- [[ledger-line-security]] — barrier. *The causeway gate comes down and a truck is held on the far side of it with its engine running* — already true when the scene opens; its Consequences stand: the dry route is closed (Deny Them Something They Want; `lockdown-1` once the system is up) and *whoever was on the causeway when it dropped is in the open* (*pinned-in-the-open-3*). *An officer's voice reads a name* — the count into the empty yard: if it reads a PC's number, *shamed-2* and *arrears-2*, and the account follows them out. *No Bounty Beyond The Wire*: hands off at the far end.
- [[ledger-security-system]] — barrier, live once the mains return. *Floodlights snap on over a work block* (» *exposed-2*; » `alarm-1`); *the gate line goes hot and every reader starts logging every signature it sees* (» `lockdown-1`, *gates sealed*; » the truck gate and landing stage close — the causeway is the only way out and it is watched); *RFID Fatigues*: uncut collar chips are read, no roll ([[ledger-issue-fatigues]]). At `lockdown` 6: *the Ledger is sealed*, Gun Turret on the gate.
- [[continuity-crisis-response-cell]] — attacker, as hazard. *A responder holds a breaching frame against a doorway and counts down out loud* — the gate house (» *concussed-3* to anyone inside; the barrier's control is gone). *Cleanup Is The Product* does not apply here: nobody outside the wire is watching and there is nothing to clean.
- [[hanne-oyelaran-challenge]] — pursuer. `contract-complete` climbs to 3 at the gate and 4 at the van. *She raises her carbine to a low ready and says a number out loud* — only if something on the causeway threatens the contract; the number is never a PC's unless a PC is in front of Rook.
- [[the-sludge-flats]] — barrier, beside the road for the whole three kilometers. The way off the causeway for anyone who needs one, and the way past a turret.
- [[escapee-list]] — watcher, beginning. *An RFID reader somewhere logs a signature that shouldn't exist anymore* (» `noticed-1`, *a name goes on the list*) — the gate reader, if the mains were up when a PC's collar passed it. Surveillance Drone (Core p. 320) over the lagoons: its report is a second `noticed-1` only if it gets a face, and the haze over the flats is against it.
- Gun Turret (Core p. 319) — the gate mast, at `lockdown` 6 only.
- Flying Taxi Driver (Core p. 302) — the truck's driver, as the civilian transit worker he is: a Stack logistics contractor with a manifest for *remediation* crates, who wants to be anywhere else and can be talked, bribed, or thrown out of his cab.

## Vectors active

- [[hanne-oyelaran]] — push: the gate house blown, the contract walked through the barrier and ahead of the crowd down the road to the van. She has no reason to stop anyone on the causeway and does not.
- [[vera-solano]] — push: the generators, the count, the floodlights, the drone. Want: the number; she reads it into an empty yard and it is not level.
- [[ledger-security-system]] — this is the scene where it wakes. From `generators-up` maxing to the far end of the causeway is the whole of its reach.

## Flashback slots

Prompts only (Core p. 125). Both open on the dark part of the road, after the gate.

- **Why you were here — the road, not the room.** The last time you were on a road out of somewhere at night, before the Ledger, and who was driving. *Where, with whom, what it cost.* Not what you saw — that stays yours ([[saw-something-i-shouldnt]]; OQ-12). A Flashback here may fill one blank on that kit as a story tag for the rest of the session (tag F *who I told, or almost told*, or weakness A *who's still out there because of what I saw*).
- **The night you were sorted — the causeway the other way.** The truck's tailgate; the gate going up; the first floodlight. What you told yourself then about how long this would be. — a crew bond or a tag from [[the-ledger]] (weakness A *the truck gate, the floodlights, the klaxon*, as a story tag the scene can press).

## What carries forward

- The crew are on the coast road past the dark end of the causeway ([[breakout-05-a-name-and-a-place]]); or in the flats beside it, rejoining the road at the coast; or in the truck, which reaches the coast road turn before anyone on foot and stops there because the van is across it.
- [[ledger-security-system]] is live behind them at whatever `lockdown` reached, and does not pursue past the causeway. `alarm` and `lockdown` are recorded for [[breakout-aftermath]].
- [[escapee-list]]: `noticed` at 1 if any collar chip was read at the gate after the mains returned, or the drone got a face; 0 otherwise. Its *The List Doesn't Forget* applies from here.
- `contract-complete` on [[hanne-oyelaran-challenge]] at 3.

## Canon and flags

- The causeway, the gate, the lagoons, and "where the escapee list's *not worth the bounty* is first tested": [[coldwater-outfall]] (BC-24). Escapee list, no bounty: Bible §6. Corporate security's legality: Bible §3. Line security cannot pursue past the causeway: [[ledger-line-security]].
- **[BUILD CHOICE]** (BC-142) the generators coming up during the walk as the scene's turn; (BC-145) the escapee list's `noticed` opening at 0 or 1 depending on the collar chips and the drone, never higher, in session one.
- **[OPEN]** (OQ-42) Solano reading the count into an empty yard is the last the crew hear of her; whether she keeps her post is not decided here.
