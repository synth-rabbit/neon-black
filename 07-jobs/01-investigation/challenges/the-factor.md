---
type: challenge
name: "The Factor"
slug: the-factor
status: review
source: custom
page: "294–300, 321–325, 304"
owner: WP7b
canon_refs: ["Bible §3 haves and have-nots", "Brief §8", "Core p. 294–300", "Core p. 304", "Core p. 321–325"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: target
scale: 0
alias: "a consolidator, on commission"
short_description: "Anselm Boateng: a man in a good coat who buys other people's paper with other people's money, has never been in a room when it went badly, and genuinely does not know who he works for."
limits:
  - {name: convince, tier: 3}
  - {name: intimidate, tier: 2}
  - {name: hurt-or-subdue, tier: 3}
  - {name: get-the-ledger, tier: 4}
  - {name: name-the-principal, tier: 999}
default_tags: ["twenty years of commissions", "somebody else's money", "three intermediaries", "a good coat", "four people hired for the evening"]
default_statuses: ["unhurried-2"]
specials:
  - {name: "He Does Not Know", text: "name-the-principal is immune. There is no roll, no Consequence, no leverage and no torture that produces the buyer's name from this Challenge, because the name is not in him. Pressed, he supplies a shell company that is real, checkable, and resolves to a second shell. Any attempt to max a Limit in order to learn the principal instead maxes get-the-ledger, and the MC says so plainly rather than letting the table spend a session on it (**[OPEN]** OQ-37)."}
  - {name: "Never In The Room", text: "Every arrangement the Factor makes has somebody in it who is not him. When a Consequence would place him in physical danger, he has instead already paid a person standing nearby — a hire, a haulier, a neighbour, a clerk — and that person is in the danger. The first time this happens in a scene it costs the crew nothing; the second time it costs them a witness."}
  - {name: "Cheaper Than The Alternative", text: "He talks. Freely, courteously, at length, about categories, prices, dockets, dates and methods, because information he is not paid to keep is information he does not keep. He will confirm everything the crew already worked out and volunteer two things they had not. Only the principal is unavailable."}
  - {name: "Settled In Concurrences", text: "His payments arrive as pre-purchased concurrences, transferred rather than spent (BC-122). If the crew take his instruments, they hold Chancery paper that makes somebody lawful somewhere for an hour — usable once, at the MC's discretion, and traceable to the Office by anyone who looks."}
  - {name: "Sells The Exit", text: "Cornered, he trades. The order he trades in: the four evening hires, then the ledger, then the haulier's name, then the delivery contact he swore he did not have. He never trades a person he is standing next to before he trades a thing, which is the only principle he has."}
threats:
  - threat: "He looks up from the desk, says a name — one of theirs — and asks whether they would like to sit down."
    consequences:
      - {text: "He knows who they are because he has bought the page they are on, and he says so mildly (the crew take on-file-2).", statuses: ["on-file-2"], tags: []}
      - {text: "He offers to buy whatever they came in with, at a fair price, right now. Escalate the Situation if they consider it.", statuses: [], tags: ["an offer that is genuinely fair"]}
  - threat: "Without stopping the conversation, he closes the ledger and puts his hand flat on it."
    consequences:
      - {text: "The ledger goes into the desk drawer, which is part of the bonded fitting (add a tier to get-the-ledger and see The Counting Room).", statuses: [], tags: []}
      - {text: "Somewhere in the shelves an evening hire stops moving stock. Present a New Challenge: Gang Member (Core p. 306), ×4 at Scale 1.", statuses: [], tags: []}
  - threat: "He gives them a name for the buyer, unprompted, with an address."
    consequences:
      - {text: "It is real, it is checkable, and it is a shell — an insurance-forensics consolidator with an office on the Face and two employees (a name that goes nowhere).", statuses: [], tags: ["a name that goes nowhere"]}
      - {text: "Checking it costs a scene, and the consignment window advances a tier while they do (see The Consignment Window).", statuses: [], tags: []}
  - threat: "He asks, politely, whether they have thought about who they are standing between."
    consequences:
      - {text: "He is right, and they had not (the crew take out-of-their-depth-2).", statuses: ["out-of-their-depth-2"], tags: []}
      - {text: "He offers them the commission he has been unable to fill — the fifth category — and it is a job offer, and it is good money. Escalate the Situation.", statuses: [], tags: []}
  - threat: "Headlights outside, and he stands up before anybody else has heard anything."
    consequences:
      - {text: "He has an arrangement for tonight and it is not with the crew. Present a New Challenge: Continuity Crisis-Response Cell.", statuses: [], tags: []}
      - {text: "He begins selling: the hires, then the ledger, then the haulier (Sells The Exit).", statuses: [], tags: []}
power_sets: []
reuse_of: "Movers and Shakers format (Core p. 321–325); an unaugmented, unarmed civilian professional in the Corporate Executive register (Core p. 304), two grades down and much better at his job."
---

# The Factor

**Role:** target · **Scale:** 0 · **Alias:** *a consolidator, on commission* · *What the crew want is on him, and the thing they came for is not.*

**Anselm Boateng.** Sixties, tall, a good coat kept brushed, reading glasses on a cord, an accent from three districts up that he has never bothered to lose. He buys paper for people who do not want to be seen buying paper, and he has done it for twenty years, for insurers, for auction houses, for two of the Big Three, for a cultural foundation on [[chancery-hill]] whose name he still will not say, and now for whoever has been emptying the Book ([[fence-network]], BC-102).

He is the Job's confrontation and he is not the Job's answer. The crew will corner a man who has been careful his whole life and find out that carefulness is exactly why he cannot help them: he has never once looked into a principal, because looking is the service he charges his clients for *not* doing.

He is not brave, not armed, not augmented past a good ear and a better memory, and he does not need to be. Nothing he owns is in the room, nothing in the room is his, and the four people between him and the door were hired this evening for the price of a night's work.

## Limits

| Limit | Tier |
|---|---|
| convince | 3 |
| intimidate | 2 |
| hurt or subdue | 3 |
| get the ledger | 4 |
| name the principal | — (immune) |

*intimidate* at 2 is deliberately cheap: he folds early and he folds gracefully, and none of it gets the crew what they actually came for. *name the principal* is the only immune Limit in this Job.

## Tags & statuses

twenty years of commissions, somebody else's money, three intermediaries, a good coat, four people hired for the evening · *unhurried-2*

## Specials

**He Does Not Know:** `name-the-principal` is immune. There is no roll, no Consequence and no leverage that produces the buyer's name, because the name is not in him. Pressed, he supplies a shell that is real and checkable and resolves to a second shell. Any attempt to max a Limit in order to learn the principal instead maxes `get-the-ledger`, and the MC says so plainly rather than letting the table spend a session on it.

**Never In The Room:** every arrangement he makes has somebody in it who is not him.

**Cheaper Than The Alternative:** he talks, at length, about everything except the one thing.

**Settled In Concurrences:** his money is Chancery paper (BC-122).

**Sells The Exit:** hires, then ledger, then haulier, then the delivery contact — in that order, and never a person he is standing next to before a thing.

## Threats / Consequences

› He looks up from the desk, says one of their names, and asks whether they would like to sit down.
» He has bought the page they are on, and says so mildly (*on-file-2*)
» He offers to buy whatever they came in with, at a fair price, now (*an offer that is genuinely fair*)

› Without stopping the conversation, he closes the ledger and puts his hand flat on it.
» Into the drawer, which is part of the bonded fitting (add a tier to `get-the-ledger`; see [[the-counting-room]])
» An evening hire stops moving stock — Present a New Challenge: **Gang Member** (Core p. 306), ×4 at Scale 1

› He gives them a name for the buyer, unprompted, with an address.
» Real, checkable, and a shell (*a name that goes nowhere*)
» Checking it costs a scene, and [[the-consignment-window]] advances a tier

› He asks, politely, whether they have thought about who they are standing between.
» He is right, and they had not (*out-of-their-depth-2*)
» He offers them the commission he has been unable to fill, and it is good money

› Headlights outside, and he stands up before anybody else has heard anything.
» Present a New Challenge: [[continuity-crisis-response-cell]]
» He begins selling (*Sells The Exit*)

## Power Sets

None. He has no chrome worth naming, no Tao, and no crew.

## Canon and flags

- Corporate security's legality and the market in lawfulness he pays in: Bible §3; BC-122, [[government]]. The Book and the categories he buys: BC-102, [[fence-network]]. Delegating a vector down the hierarchy rather than using a Key Player's principals: Core p. 291 — the Factor is what a buyer looks like from below.
- **[BUILD CHOICE]** the Factor as a named intermediary and the immunity of `name-the-principal`; see [[build-choices]] "Added by WP7b".
- **[OPEN]** (OQ-37) this profile exists specifically so the Job cannot resolve the buyer. Both [[upstart]] and [[corp-c]] must remain possible after every scene he appears in.
