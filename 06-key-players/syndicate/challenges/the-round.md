---
type: challenge
name: The Round
slug: the-round
status: review
source: custom
page: "294–300, 319"
owner: WP4-trio2
canon_refs: ["Bible §2 werewolf", "Bible §3 power structure", "Bible §4 theme 3", "Brief §8", "Core p. 294–300", "Core p. 297", "Core p. 319"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: mystery
scale: 2
alias: "the vans"
short_description: "The Almoners' weekly distribution circuit: no map, no schedule, no two weeks alike — a mystery that cannot be followed, only understood, and that answers a different question than the one the crew asked."
limits:
  - {name: map-the-round, tier: 5}
  - {name: follow-a-van, tier: 3}
  - {name: read-the-ledger, tier: 6}
default_tags: ["a different order every week", "drivers who do not know the next stop", "nothing written down", "everyone on the route eats at the Kitchen"]
default_statuses: ["deniable-3"]
specials:
  - {name: "Not A Chain, A Habit", text: "The Round has no schedule to steal. Route, order, driver, and handoff are set the night before by one person and communicated verbally; a driver learns the next stop at the current one. Following a van (follow-a-van) is therefore easy and useless: max it out and the crew learns one stop, and one stop tells them nothing they did not already know."}
  - {name: "The Wrong Question", text: "Every tier the crew puts on map-the-round with surveillance, tailing, or hacking answers where the dose goes. Only tiers earned from the Kitchen's paperwork — the clinic license, a supply invoice, an aftercare requisition — answer where it comes from, which is the only answer worth anything. When map-the-round maxes without any tier from paperwork, the crew has a complete distribution map and nothing else, and the Almoners change the whole Round within a week (reset it, and give the crew watched-3)."}
  - {name: "The Ledger Is Not Evidence", text: "Read-the-ledger is tier 6 and is not a hacking problem: the ledger is pencil, in a room with people in it, and it is not a record of crimes. Maxing it gives the crew the debt structure — who owes, who collects, and that the packs are collateral. It does not give them the supply contract, which is filed somewhere else entirely (see [[first-alms]])."}
  - {name: "It Is Also A Charity", text: "Any action the crew takes against the Round that a resident of the Blocks could witness — a stopped van, a spilled crate, an arrest, a fire — costs somebody their week. The MC may give the crew hated-in-Marlow-3 as a Consequence, a compelling status cleared only by making the district whole."}
threats:
  - threat: "A washed white van pulls up at a stop that was not on it last week, and the driver waits with the engine running for exactly four minutes."
    consequences:
      - {text: "The handoff happens somewhere the crew is not, because it always does.", statuses: [], tags: ["missed the handoff"]}
      - {text: "The crew's watcher is made — not by the driver, by a neighbor.", statuses: ["marked-2"], tags: []}
  - threat: "Somebody on the route asks the crew, pleasantly, whether they are all right for food."
    consequences:
      - {text: "The offer is genuine and the crew's business is now the Kitchen's business.", statuses: [], tags: ["the Kitchen knows you are asking"]}
      - {text: "Present a New Challenge: [[almoners-volunteer]], arriving to help.", statuses: [], tags: []}
  - threat: "The Round changes shape mid-week — a stop dropped, a driver swapped, two crates that go somewhere nobody has ever followed."
    consequences:
      - {text: "Reset follow-a-van. Whatever the crew had built is a week out of date.", statuses: [], tags: []}
      - {text: "A pack that expected a delivery does not get one, and takes it out on the district. Present a New Challenge: [[pack-on-the-run]].", statuses: [], tags: ["a kennel went short this week"]}
  - threat: "A crate goes past with a shipping label on it, and the label is printed, corporate, and completely ordinary."
    consequences:
      - {text: "The crew sees the wrong half of the answer: a pharmaceutical case number and no company name. Escalate the Situation.", statuses: [], tags: ["a case number with no name"]}
      - {text: "The label is noticed being noticed. [[first-alms]] learns that somebody is reading crates, and the Round's paperwork moves.", statuses: [], tags: ["the office has been told"]}
power_sets: []
reuse_of: "Structured after Security System (Core p. 319) — an obstacle built to be worked at across a whole job rather than solved in one action."
---

# The Round

**Role:** mystery · **Scale:** 2 · **Alias:** *the vans* · *A distribution circuit that cannot be followed, only understood — and that answers a different question than the one the crew asked.*

Every week, out of the loading dock behind the Kitchen's ovens in [[marlow-blocks]], the Almoners' vans go out. They stop at the rail siding in [[cinder-yards]], at two addresses in [[gullet-market]], at a door behind the book at [[halloran-circus]], and at between four and nine other places that are different every week. Crates in, envelopes out, nobody gets out of the cab who does not have to. That is the Round, and under the Wall it is not a secret; it is a fact of the calendar, like the tide.

It is a **mystery** (Core p. 297) rather than a barrier because the interesting thing about it is not that it is hard to see. It is that seeing it teaches you nothing. The Almoners have never protected the Round with force, because the Round has no single point that matters: no warehouse, no chemist, no cutting house, no boss in a car. It is a habit performed by people who like each other, and it reconstitutes itself in a week if you break it.

The thing it hides is upstream, in a filing cabinet, on a form. A crew can spend a whole job following vans and end up with a beautiful map of a district's veins and no idea where the blood is made.

## Limits

| Limit | Tier |
|---|---|
| map the Round | 5 |
| follow a van | 3 |
| read the ledger | 6 |

## Tags & statuses

a different order every week, drivers who do not know the next stop, nothing written down, everyone on the route eats at the Kitchen · *deniable-3*

## Specials

**Not A Chain, A Habit:** There is no schedule to steal; a driver learns the next stop at the current one. *Follow a van* is easy and useless — max it and the crew learns one stop.

**The Wrong Question:** Tiers on *map the Round* from surveillance, tailing, or hacking answer *where the dose goes*. Only tiers from the Kitchen's paperwork — clinic license, supply invoice, aftercare requisition — answer *where it comes from*. Maxing *map the Round* with no paperwork tier gives a complete distribution map and nothing else; the Almoners rebuild the Round within a week (reset it; the crew takes *watched-3*).

**The Ledger Is Not Evidence:** *Read the ledger* is not a hacking problem — it is pencil, in a room with people in it, and it records no crimes. Maxing it reveals the debt structure and that the packs are collateral. It does not reveal the supply contract; that is filed elsewhere ([[first-alms]]).

**It Is Also A Charity:** Any action against the Round that a Blocks resident could witness costs somebody their week. The MC may give the crew *hated-in-Marlow-3*, compelling, cleared only by making the district whole.

## Threats / Consequences

› A washed white van pulls up at a stop that was not on it last week, and the driver waits with the engine running for exactly four minutes.
» The handoff happens somewhere the crew is not (*missed the handoff*)
» The crew's watcher is made — by a neighbor, not the driver (*marked-2*)

› Somebody on the route asks the crew, pleasantly, whether they are all right for food.
» The offer is genuine, and the crew's business is now the Kitchen's business (*the Kitchen knows you are asking*)
» Present a New Challenge: [[almoners-volunteer]], arriving to help

› The Round changes shape mid-week — a stop dropped, a driver swapped, two crates that go somewhere nobody has ever followed.
» Reset *follow a van*; whatever the crew built is a week out of date
» A pack goes short and takes it out on the district (Present a New Challenge: [[pack-on-the-run]]; *a kennel went short this week*)

› A crate goes past with a shipping label on it, and the label is printed, corporate, and completely ordinary.
» The crew sees the wrong half of the answer (Escalate the Situation; *a case number with no name*)
» The label is noticed being noticed, and the Round's paperwork moves (*the office has been told*)

## Power Sets

None. The Round is a system.

## Canon and flags

- Bible §2 (the syndicate resells the trigger to the packs), §3, §4 theme 3; Brief §8; roles per Core p. 297.
- **[BUILD CHOICE]** (BC-109) the Round, its three Limits, and the paperwork-versus-surveillance rule, which is the mechanical form of the Almoners' twist.
- **[OPEN]** (OQ-18) the Round's stops beyond the four named are deliberately unfixed; **[OPEN]** (OQ-3) the crate's case number leads to [[corp-a]] and no further in this file.
