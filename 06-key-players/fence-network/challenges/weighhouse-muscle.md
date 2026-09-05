---
type: challenge
name: "Weighhouse Muscle"
slug: weighhouse-muscle
status: review
source: custom
page: "294–300, 306, 118–120"
owner: WP4-trio1
canon_refs: ["Bible §2 hunter", "Bible §3 haves and have-nots", "Brief §8", "Core p. 294–300", "Core p. 306"]
flags: [BUILD CHOICE]
player_safe: false
role: attacker
scale: 1
alias: "the quay stops working"
short_description: "Not soldiers — dockers, runners and stallholders who all stop what they are doing at the same moment, because the counter has to stay open."
limits:
  - {name: hurt-or-subdue, tier: 3}
  - {name: convince, tier: 4}
  - {name: bribe, tier: 999}
  - {name: outrun-them-in-the-labyrinth, tier: 5}
default_tags: ["cargo hooks and bale hooks", "knows every cut-through", "the whole quay is watching", "nothing here is a weapon until it is"]
default_statuses: ["numbers-2"]
specials:
  - {name: "The Quay Stops Working", text: "This Challenge does not arrive; it accumulates. Each round it is in a scene in Gullet Market, its Scale increases by one to a maximum of 3, as more people put down what they were carrying. Scale drops back to 1 the moment the crew are outside the market or the reason has passed — these are working people and the work is still there."}
  - {name: "Not Their Fight Until It Is", text: "The muscle will not initiate against anyone who has not touched a person, the counter, the balance, or a runner. Property is negotiable and is Tally's problem; people are not."}
  - {name: "Every Door Is Theirs", text: "In Gullet Market, outrun-them-in-the-labyrinth cannot be attempted twice in the same scene. The second attempt instead ends with the crew somewhere the runners chose."}
  - {name: "Weights Is In The Doorway", text: "If Bohdan Adeyemi is present, this Challenge gains unshakable-3 and does not act until he has given his one warning. Use his profile for him; this Challenge is everyone else."}
threats:
  - threat: "Three dockers put down what they were carrying at the same time, without looking at each other."
    consequences:
      - {text: "The crew are surrounded before anyone has raised anything (cornered-3).", statuses: ["cornered-3"], tags: []}
      - {text: "Every exit from the stall row is standing in a doorway (Deny Them Something They Want).", statuses: [], tags: []}
  - threat: "A bale hook comes off a shoulder strap, casually, the way a tool does."
    consequences:
      - {text: "A hook, used by somebody who uses one all day (torn-open-3).", statuses: ["torn-open-3"], tags: []}
      - {text: "Somebody is put through a stall front and the stall's owner joins in (gain a Scale, and burn a tag describing cover).", statuses: [], tags: []}
  - threat: "A runner ahead of the crew whistles once and does not run away."
    consequences:
      - {text: "The route the crew were taking is closed and the one they are pushed onto is not theirs (Deny Them Something They Want; the crew take herded-2).", statuses: ["herded-2"], tags: []}
      - {text: "The Labyrinth's cut-throughs deliver more of them ahead rather than behind (increase Scale by one).", statuses: [], tags: []}
  - threat: "Somebody says a name — the crew's — loudly enough for the row to hear."
    consequences:
      - {text: "The Gullet knows the crew are on the wrong side of the counter (the crew gain barred-2 in the market until Tally says otherwise).", statuses: ["barred-2"], tags: []}
power_sets: []
reuse_of: "Gang Member, Core p. 306 — re-flavored: these are employed dockers and runners, not a gang, and they disperse the moment the reason does"
---

# Weighhouse Muscle

**Role:** attacker · **Scale:** 1, rising to 3 in [[gullet-market]] · **Alias:** *the quay stops working* · *Not soldiers — everybody, at once.*

[[fence-network|Tally's]] protection is not a security detail. It is the fact that the Weighhouse's counter is the thing the entire Foot needs to keep existing, and that everyone on the quay knows it. When somebody puts hands on a person inside the Weighhouse, or on a runner in the Labyrinth, or on the balance itself, thirty people who were working stop working, and that is the whole mechanism.

They are dockers, stallholders, pawnbrokers' boys and runners. Bale hooks, cargo hooks, a pry bar, an oar. **Patched** bodies, mostly, with second-hand chrome and no training beyond twenty-five years of moving heavy objects around other people. In a stand-up fight against corporate security they lose. In [[gullet-market]] — a roofed labyrinth of stalls, cut-throughs and cabling, impossible to surveil and impossible to search — they do not have to have a stand-up fight.

Adapted from **Gang Member** (Core p. 306) and deliberately not a gang: they have jobs, the jobs are still there, and when the reason ends they go back to them.

## Limits

| Limit | Tier |
|---|---|
| hurt or subdue | 3 |
| convince | 4 |
| bribe | – |
| outrun them in the Labyrinth | 5 |

**bribe** is immune. Not incorruptibility: the counter is worth more to every one of them than any amount a stranger is carrying, and everyone can do that arithmetic.

## Tags & statuses

cargo hooks and bale hooks, knows every cut-through, the whole quay is watching, nothing here is a weapon until it is · *numbers-2*

## Specials

**The Quay Stops Working:** Scale rises by one per round in [[gullet-market]], to 3; drops to 1 when the crew are out of the market or the reason has passed.

**Not Their Fight Until It Is:** they do not initiate against anyone who has not touched a person, the counter, the balance, or a runner.

**Every Door Is Theirs:** *outrun them in the Labyrinth* cannot be attempted twice in a scene; the second attempt ends with the crew somewhere the runners chose.

**Weights Is In The Doorway:** with [[bohdan-adeyemi]] present, this Challenge gains *unshakable-3* and waits for his one warning. Use [[bohdan-adeyemi-challenge]] for him.

## Threats / Consequences

› Three dockers put down what they were carrying at the same time, without looking at each other.
» Surrounded before anything is raised (*cornered-3*)
» Every exit from the row has somebody in it (Deny Them Something They Want)

› A bale hook comes off a shoulder strap, casually, the way a tool does.
» A hook, used by somebody who uses one all day (*torn-open-3*)
» Somebody through a stall front, and the stall's owner joins in (gain a Scale; burn a cover tag)

› A runner ahead of the crew whistles once and does not run away.
» The route closes and the one they are pushed onto is not theirs (*herded-2*)
» More of them ahead rather than behind (increase Scale by one)

› Somebody says the crew's name loudly enough for the row to hear.
» The Gullet knows they are on the wrong side of the counter (*barred-2* in the market until Tally says otherwise)

## Power Sets

None. **Chromed Up** (Core p. 332) is wrong here: this is Patched chrome, second-hand and mismatched, and the profile's strength is numbers and ground, not hardware.

## Canon and flags

- The Gullet's Patched order of precedence — a Patched body with a network outranks a Fitted one with a warranty — and the Labyrinth: [[gullet-market]] (BC-17). Baseline and mixed populations: Bible §2, §3.
- **[BUILD CHOICE]** (BC-102) protection as a market-wide reflex rather than a security detail; (BC-103) tiers, Specials and Threats.
- Reuse recorded: **Gang Member** (Core p. 306), re-flavored — see `reuse.md`.
