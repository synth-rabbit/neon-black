---
type: challenge
name: "The Cold Suite"
slug: the-cold-suite
status: review
source: custom
page: "294–300, 308–309, 319, 22, 27–28"
owner: WP4-trio1
canon_refs: ["Bible §3 the upstart", "Brief §6.5", "Brief §8", "Core p. 22", "Core p. 27–28", "Core p. 294–300", "Core p. 308–309", "Core p. 319"]
flags: [BUILD CHOICE, TAO-REINTERPRETED, OPEN]
player_safe: false
role: barrier
scale: 3
alias: "the ward's house monitoring"
short_description: "Continuity's Harnessing floors and the monitored Nearspace they reach through: not a firewall but a room full of people, breathing in time, watching everyone else's Domains."
limits:
  - {name: override, tier: 5}
  - {name: spoof-credentials, tier: 4}
  - {name: turn-an-operator, tier: 3}
  - {name: traced, tier: 4}
default_tags: ["Harnessed operators breathing in time", "monitors in every tenant's Nearspace", "server halls at four degrees", "everyone's Domain is in this rock"]
default_statuses: ["firewalled-3"]
specials:
  - {name: "Harnessed, Not Automated", text: "This Challenge is people. Intrusion countermeasures can be out-hacked; a suite of Harnessed operators can also be out-thought, bored, misled, or bought. The turn-an-operator Limit is only available to approaches that treat the suite as a shift full of employees — hours, quotas, grudges, a coach who stopped showing up."}
  - {name: "Everyone's Domain Is In This Rock", text: "The Lattice physically hosts most of Palisade's Domains (Core p. 27). Whenever the crew act against the suite from inside a Domain the Lattice hosts — their own Hood, a client's, the Chancery's — the suite may, as a Consequence, take a story tag or a status from that Domain rather than from the crew. It is holding their things."}
  - {name: "The Focus Practice", text: "Suite operators run twenty minutes of a breath-and-attention discipline, sold to the ward by a wellness contractor as productivity software, before every session. Once per scene, when the suite would take a status from a cyberspace action, it removes two tiers from that status instead and takes overload-1 in its place. [TAO-REINTERPRETED] Nobody in the suite knows why the practice works; who supplies the contractor is [OPEN] (OQ-15) and this Challenge does not say."}
  - {name: "The Address Is The Point", text: "traced is the suite's real weapon. Continuity does not prosecute intrusions; it dispatches. When traced maxes, Present a New Challenge: Continuity Crisis-Response Cell at the intruder's physical location, and reset traced."}
threats:
  - threat: "A monitor icon in the corner of somebody's overlay, which was always there, turns to face them."
    consequences:
      - {text: "The suite watches back and starts building the file (traced-1 and the crew gain surveilled-2).", statuses: ["traced-1", "surveilled-2"], tags: []}
      - {text: "It reads what the crew's own gear is carrying and quotes it back at them. Escalate the Situation.", statuses: [], tags: []}
  - threat: "Every door credential in the gallery is reissued at once, and the corridor lighting changes color."
    consequences:
      - {text: "Access is revoked mid-approach (Deny Them Something They Want) and the gallery seals behind them.", statuses: [], tags: ["the gallery is sealed"]}
      - {text: "A patrol is walked to the right corridor. Present a New Challenge: Security Guard (Core p. 305) in Continuity soft-shell, Scale 1.", statuses: [], tags: []}
  - threat: "In the suite, forty operators inhale on the same beat."
    consequences:
      - {text: "A Harnessed push through the crew's own rigs (headsplitting-3 and burn a cyberspace or gear tag).", statuses: ["headsplitting-3"], tags: []}
      - {text: "The suite takes the crew's route apart behind them, closing what they came through (trapped-in-the-Tangle-3).", statuses: ["trapped-in-the-Tangle-3"], tags: []}
  - threat: "An operator's session runs deeper than the shift board says it should, and the board does not flag it."
    consequences:
      - {text: "That operator is somewhere the suite is not, and is not answering (remove the suite's coordinated posture; the crew may attempt turn-an-operator against that operator alone).", statuses: [], tags: ["one operator, alone, deep"]}
      - {text: "Whatever the operator found is now in the suite's log, with the crew in it (traced-2).", statuses: ["traced-2"], tags: []}
power_sets: []
reuse_of: ""
---

# The Cold Suite

**Role:** barrier · **Scale:** 3 (a floor of operators plus the ward's monitoring estate) · **Alias:** *the ward's house monitoring* · *Not a firewall — a room full of people, breathing in time.*

Four floors of the plaza tower in [[the-lattice]], kept at the same temperature as the server halls below because the racks and the operators cool the same way. Rows of couches, jack leads dressed into the ceiling, a shift board on the wall, and forty Harnessed intrusion specialists working other people's Domains under contract, under monitoring clauses, and — for about a fifth of the shift hours anyone audits — under nothing at all.

This is [[upstart|Continuity]]'s hacking specialty as an industrial process (Bible §3; Brief §6.5). Harnessing is attacking secure systems with a brain's processing power in a shared metaphor (Core p. 22); the Cold Suite is what that looks like when a firm staffs it in shifts and sells it by the hour. The monitors it reaches through are in every tenant's Nearspace by contract, disclosed and itemized, and no tenant has ever read the schedule.

Its recruits come up from the coffin-blocks of [[relay-fields]], where a kid with a secondhand jack and free tower bandwidth can already do things a Fitted coder pays by the minute for.

## Limits

| Limit | Tier |
|---|---|
| override | 5 |
| spoof credentials | 4 |
| turn an operator | 3 |
| traced (progress) | 4 |

**turn an operator** is cheap and is the whole design: the suite's weakness is that it is a workplace. It is available only to approaches that treat it as one (see *Harnessed, Not Automated*).

## Tags & statuses

Harnessed operators breathing in time, monitors in every tenant's Nearspace, server halls at four degrees, everyone's Domain is in this rock · *firewalled-3*

## Specials

**Harnessed, Not Automated:** the suite is people. Hours, quotas, grudges, and a coach who stopped showing up are all attack surfaces.

**Everyone's Domain Is In This Rock:** acting against the suite from inside a Lattice-hosted Domain lets the suite take a tag or status from that Domain instead of from the crew.

**The Focus Practice:** once per scene the suite removes two tiers from a cyberspace status and takes *overload-1*. **[TAO-REINTERPRETED]** (CR-1) The Lattice's third development — a Mythos cult restated as a licensed breath-and-attention discipline sold as productivity ([[the-lattice]]). Nobody in the suite knows why it works. **[OPEN]** (OQ-15).

**The Address Is The Point:** when *traced* maxes, Present a New Challenge — [[continuity-crisis-response-cell]] at the intruder's physical address — and reset *traced*.

## Threats / Consequences

› A monitor icon that was always there turns to face somebody.
» The suite watches back (*traced-1*, *surveilled-2*)
» It quotes the crew's own gear back at them (Escalate the Situation)

› Every door credential in the gallery reissues at once and the corridor light changes color.
» Access revoked mid-approach (Deny Them Something They Want; *the gallery is sealed*)
» A patrol walked to the right corridor — Present a New Challenge: Security Guard (Core p. 305) in soft-shell, Scale 1

› Forty operators inhale on the same beat.
» A Harnessed push through the crew's rigs (*headsplitting-3*; burn a cyberspace or gear tag)
» The route comes apart behind them (*trapped-in-the-Tangle-3*)

› One operator's session runs deeper than the shift board says, and the board does not flag it.
» That operator is alone and not answering (*one operator, alone, deep*)
» Whatever they found is in the log, with the crew in it (*traced-2*)

## Power Sets

None applied. **Surveillance Data Fed** (Core p. 333) is the overlay for any Continuity element working off the suite's product; **Device Hijacking** (Core p. 332) fits an operator run against the crew's own chrome.

## Canon and flags

- The upstart's hacking specialty and its cyberspace resources: Bible §3, Brief §6.5. Cyberspace as written — Nearspace, Domains, the Tangle, Harnessing: Core p. 22, 27–28. The Lattice as the physical home of Palisade's Domains: [[the-lattice]] (BC-18).
- **[BUILD CHOICE]** (BC-103) the name *the Cold Suite*. **[BUILD CHOICE]** (BC-105) Limits, Specials, and the *turn an operator* route.
- **[TAO-REINTERPRETED]** (CR-1) the focus practice, carried over from [[the-lattice]] development 3. **[OPEN]** (OQ-15) whether that is Tao in cyberspace, in the coder, or neither — not decided.
- Nothing here is Bloodware. The suite is a shift, a contract, and a cold room.
