---
type: challenge
name: "The Envelope Detail"
slug: envelope-detail
status: review
source: custom
page: "294–300, 305"
owner: WP4-trio3
canon_refs: ["Bible §3 power structure", "Bible §3 Masquerade", "Brief §6.3", "Brief §8", "Plan A.6", "Core p. 294–300", "Core p. 304", "Core p. 305"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: attacker
scale: 1
alias: "Chancery police, doing their rounds"
short_description: "A Chancery patrol detail that works for whoever paid this month: real police, real authority, and a sergeant who already knows whose report will be the record."
limits:
  - {name: hurt-or-subdue, tier: 3}
  - {name: bribe, tier: 2}
  - {name: outrun-or-lose, tier: 3}
  - {name: implicate, tier: 5}
default_tags: ["badge and authority", "Orison sidearms under a service contract", "this month's arrangement", "knows every doorway on the block"]
default_statuses: ["bored-2", "outnumbered-and-aware-of-it-2"]
specials:
  - {name: "Whose Report Is The Record", text: "The sergeant knows before arriving whether a concurrence has been sold for this address and this hour ([[chancery-process]]). If one has, the detail stands aside for the corporate force holding it, and the crew is dealing with that Challenge instead. If none has, or if two have, the detail is the lawful party and acts like it."}
  - {name: "Two Envelopes", text: "The detail is paid by more than one party this month. Once per scene, when the crew names or produces a party the detail is also being paid by, the detail must either stand down for the rest of the scene or take a tier to implicate. The crew has to know the name; guessing does not work."}
  - {name: "Cheap and Corrupt, Not Stupid", text: "The bribe Limit is 2 and always available — but a paid detail does not go away, it goes elsewhere and comes back with a reason. A bribed detail returns in the next scene in this district with alert-2 and the story tag they know what you paid to avoid."}
  - {name: "Nothing Happens Under the Wall", text: "In Foot and Under districts the detail does not call for support, does not file, and does not pursue past its own turf — because there is no budget for any of it. A crew that gets off the block has got away. What follows them is the report, not the police."}
threats:
  - threat: "A patrol vehicle rolls to a stop without cutting its engine and the sergeant gets out alone, unhurried."
    consequences:
      - {text: "Credentials, a name, and a question about who the crew works for — all of it going into a wrist holo (identified-2).", statuses: ["identified-2"], tags: []}
      - {text: "The stop is a stall; the detail is holding the block for whoever bought the hour (delayed-3).", statuses: ["delayed-3"], tags: []}
  - threat: "The sergeant names the amount, in front of everyone, the way one reads a fee schedule."
    consequences:
      - {text: "Paid — and the detail returns next scene knowing exactly what the crew will pay to be left alone (they know what you paid to avoid).", statuses: [], tags: ["they know what you paid to avoid"]}
      - {text: "Refused — the detail escalates from a stop to a search, and a search finds something (contraband-on-you-3).", statuses: ["contraband-on-you-3"], tags: []}
  - threat: "Two of them move around behind the crew while the sergeant keeps talking about the weather."
    consequences:
      - {text: "Batons and Orison sidearms, at close range, aimed to end it (beaten-3 or gunshot-wound-3).", statuses: ["beaten-3"], tags: []}
      - {text: "One PC is cuffed and put in the vehicle, and the vehicle does not go to the Chancery (taken-in-3).", statuses: ["taken-in-3"], tags: []}
  - threat: "The sergeant says a name the crew has not given him and watches their faces."
    consequences:
      - {text: "The detail is working for somebody with an interest in the crew and has been since the start of the shift (Escalate the Situation).", statuses: [], tags: []}
      - {text: "The crew's presence at this address enters a report that will be true forever (on the record at this address).", statuses: [], tags: ["on the record at this address"]}
  - threat: "A corporate team arrives at the same incident and both the sergeant and their team leader reach for paper."
    consequences:
      - {text: "Two concurrences for the same hour. The detail and the corporate force draw on each other in front of witnesses — advance public-war per [[secret-war-goes-public]].", statuses: ["public-war-2"], tags: ["tier lifts locked down"]}
      - {text: "The detail stands down and the corporate force treats the crew as the incident (Make the Future Bleaker).", statuses: [], tags: []}
power_sets: []
reuse_of: "Security Guard as police (Core p. 305) with the Chancery's arrangements layered on; the sergeant can be run as Heavy Urban Response Tactics Officer (Core p. 304) when the Hill sends a real unit."
---

# The Envelope Detail

**Role:** attacker · **Scale:** 1 (a four-officer patrol detail) · **Alias:** *Chancery police, doing their rounds* · *Real police, real authority, and a sergeant who already knows whose report will be the record.*

Chancery police are real, armed, underpaid, outnumbered on their own hill by corporate security, and carrying [[corp-b|Orison]] sidearms under a service contract that the Chancery cannot afford to end. At the Foot and under the Wall they are what is left of government (Bible §3; [[palisade|Palisade]]).

An *envelope detail* is not a special unit — it is any patrol detail with an arrangement, which is all of them ([[chancery-hill]]: every interaction with an official requires a bribe, and there is a rate card). This one has a sergeant who has worked the same blocks for eleven years, knows every doorway, and gets paid by two parties this month. He is not a monster and does not want a fight; his whole professional life is a series of small decisions about whose money is present.

What makes the detail dangerous is not the four officers. It is that they are *exactly as legal as everyone else with a gun* (Bible §3), and that they know, before they get out of the vehicle, whether somebody has already bought the right to be the lawful party at this address.

## Limits

| Limit | Tier |
|---|---|
| hurt or subdue | 3 |
| bribe | 2 |
| outrun or lose | 3 |
| implicate | 5 |

## Tags & statuses

badge and authority · Orison sidearms under a service contract · this month's arrangement · knows every doorway on the block · *bored-2* · *outnumbered-and-aware-of-it-2*

## Specials

**Whose Report Is The Record:** The sergeant knows in advance whether a concurrence was sold for this address and hour ([[chancery-process]]). If one was, the detail stands aside for the corporate force holding it. If none was — or if two were — the detail is the lawful party and behaves like it.

**Two Envelopes:** The detail is paid by more than one party this month. Once per scene, if the crew names or produces one of those parties, the detail must stand down for the scene or take a tier to *implicate*. Guessing does not work; the crew has to know the name.

**Cheap and Corrupt, Not Stupid:** *Bribe* is 2 and always available, but a paid detail goes elsewhere rather than away, and returns next scene in this district with *alert-2* and the story tag *they know what you paid to avoid*.

**Nothing Happens Under the Wall:** In Foot and Under districts the detail does not call support, does not file, and does not pursue past its own turf — there is no budget. A crew that gets off the block has got away; what follows them is the report.

## Threats / Consequences

› A patrol vehicle stops without cutting its engine and the sergeant gets out alone.
» Credentials, a name, a question, all of it into a wrist holo (*identified-2*)
» The stop is a stall; somebody bought the hour (*delayed-3*)

› The sergeant names the amount in front of everyone, the way one reads a fee schedule.
» Paid, and now they know the price of being left alone (*they know what you paid to avoid*)
» Refused — the stop becomes a search, and a search finds something (*contraband-on-you-3*)

› Two of them move around behind the crew while the sergeant talks about the weather.
» Batons and sidearms at close range (*beaten-3* or *gunshot-wound-3*)
» A PC is cuffed and put in a vehicle that does not go to the Chancery (*taken-in-3*)

› The sergeant says a name the crew never gave him, and watches their faces.
» He has been working for somebody with an interest in them since the shift started (Escalate the Situation)
» Their presence here enters a report that will be true forever (*on the record at this address*)

› A corporate team arrives at the same incident and both sides reach for paper.
» Two concurrences, one hour, witnesses (*public-war-2*, *tier lifts locked down*; [[secret-war-goes-public]])
» The detail stands down and the corporate force treats the crew as the incident (Make the Future Bleaker)

## Power Sets

**Troop-Leading** (Core p. 329) on the sergeant when the Hill sends a real unit; **Local to Ward** (Tokyo p. 132) re-flavoured as *knows every doorway on this block*, for a detail on its own turf.

## Canon and flags

- Corporate security is exactly as legal as the city police, and the government is deeply corrupt (Bible §3; Brief §6.3). Police carry Orison sidearms ([[chancery-hill]], WP1). Public incidents blamed on Baselines are a corporate cleanup, not a police one (Bible §2, §3).
- **[BUILD CHOICE]** (BC-122) *Whose Report Is The Record* is the jurisdiction twist in rules; (BC-118) the name *the Envelope Detail*.
- **[OPEN]** (OQ-9) the *public-war* tiers here come from [[secret-war-goes-public]] (BC-5, BC-13) and add no new series-level clock.
