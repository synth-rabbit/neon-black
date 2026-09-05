---
type: challenge
name: "The Counting Room"
slug: the-counting-room
status: review
source: custom
page: "294–300, 310, 319"
owner: WP7b
canon_refs: ["Bible §3 haves and have-nots", "Brief §8", "Core p. 294–300", "Core p. 310", "Core p. 319"]
flags: [BUILD CHOICE]
player_safe: false
role: barrier
scale: 2
alias: "a shuttered automat with a dead menu board"
short_description: "A converted automat unit in the Stretch fitted out as a bonded store: one door that logs, a weigh-in desk, honest scales, and four hundred bundles of other people's history on numbered shelves."
limits:
  - {name: get-in-unlogged, tier: 4}
  - {name: find-the-bundle, tier: 3}
  - {name: take-it-all, tier: 6}
  - {name: get-out-unlogged, tier: 5}
  - {name: hurt-or-subdue, tier: 999}
default_tags: ["a door that logs", "four hundred bundles on numbered shelves", "honest counter scales", "a haulier's booking sheet by the door", "nothing here is his"]
default_statuses: []
specials:
  - {name: "Bonded, Not Guarded", text: "This room has no alarm, no turret and no guard. It has a lease clause. The door records every opening against a bond, and the bond is what the Factor's clients are actually paying for. Force, cutting and breaching all work perfectly and all fail the same way: the record of the opening is the thing that matters, and it survives the door."}
  - {name: "Dockets, Not Titles", text: "The bundles are indexed by docket number against the ledger on the desk, not by what they contain. Without the ledger, find-the-bundle is attempted at one tier higher and a failed attempt yields the wrong bundle, convincingly. With the ledger, shelf 388 is found in one action, no roll."}
  - {name: "Four Hundred Bundles", text: "take-it-all at 6 is honest: the consignment is roughly two hundred kilos of paper on numbered shelves in a district with no vehicles the crew own. Any crew that maxes it has arranged a vehicle, a route and a reason during the Job, and the MC should let that arranging be a scene rather than a roll."}
  - {name: "Paper Burns", text: "Fire, water or Noise destroys the consignment completely and in minutes, and this is the easiest thing anybody can do here. It also destroys the ledger, the second copies, shelf 388, and every piece of proof the crew have assembled — and it does not stop the buyer, who has the categories, the intermediaries and eighteen months of practice. The MC states this cost out loud before it is paid."}
  - {name: "The Log Is A Page", text: "Whatever the crew do here, the door's record goes to the leaseholder, and the leaseholder's records are Chancery-adjacent paper: filed on the Hill, counterparted in the paper barn. A crew that got in unlogged is a crew that is on no page [[acquisition]]'s target holds. A crew that did not is."}
threats:
  - threat: "The door reads the opening and writes it, quietly, whether or not anybody used a key."
    consequences:
      - {text: "The opening is on the bond, with a timestamp (the crew take on-the-log-2 and see The Log Is A Page).", statuses: ["on-the-log-2"], tags: []}
      - {text: "The leaseholder's night service calls the unit's line to confirm. Somebody has to answer it.", statuses: [], tags: ["a telephone nobody wants to answer"]}
  - threat: "The shelves are numbered and the numbers do not mean anything without the book on the desk."
    consequences:
      - {text: "The crew take the wrong bundle and it is convincing — eight years of shipping losses and nothing they need (add a tier to find-the-bundle).", statuses: [], tags: []}
      - {text: "Searching properly takes long enough to matter. The Consignment Window advances a tier.", statuses: [], tags: []}
  - threat: "The haulier's booking sheet by the door has a date on it, and the date is close."
    consequences:
      - {text: "Present a New Challenge, or advance it: The Consignment Window.", statuses: [], tags: []}
      - {text: "A crew that photographs the sheet instead of taking it has a date and no proof (a date, and nothing to show).", statuses: [], tags: ["a date, and nothing to show"]}
  - threat: "Two hundred kilos of paper, one door, and no vehicle."
    consequences:
      - {text: "They can carry what two people can carry, and they must choose in front of each other (Have the PCs choose: the ledger, or shelf 388, or an armful of second copies).", statuses: [], tags: []}
      - {text: "Whatever they leave is on the haulier's sheet by morning.", statuses: [], tags: []}
power_sets: []
reuse_of: "Location/Barrier in the Crumbling Building and Hazard Zone pattern (Core p. 310) with navigate replaced by find-the-bundle; the door is a Security System (Core p. 319) that records rather than resists."
---

# The Counting Room

**Role:** barrier · **Scale:** 2 (a room, its door, its index, and two hundred kilos of paper) · **Alias:** *a shuttered automat with a dead menu board* · *An obstacle in the path of the PCs, which cannot be fought.*

A converted automat unit on a service street in [[kilbride-stretch]]: shuttered frontage, dead menu board, and behind it one long room fitted out as a bonded store. Strip lights, a weigh-in desk with a lamp over it, honest counter scales, and four hundred bundles in oilcloth and string on numbered shelves, each with a docket. It smells of paper and cold fat.

It is not the Factor's. Nothing here is anybody's. That is what *bonded* means, and it is why the room's whole security model is a record rather than a wall.

The set piece of [[investigation-07-the-counting-room]] and the inside of the cordon in [[investigation-08-the-cordon]].

## Limits

| Limit | Tier |
|---|---|
| get in unlogged | 4 |
| find the bundle | 3 |
| take it all | 6 |
| get out unlogged | 5 |
| hurt or subdue | — (immune) |

*take it all* at 6 is the honest tier for two hundred kilos of paper and no vehicle. *get out unlogged* at 5 is harder than getting in, because getting out is the part somebody eventually reads.

## Tags & statuses

a door that logs, four hundred bundles on numbered shelves, honest counter scales, a haulier's booking sheet by the door, nothing here is his

## Specials

**Bonded, Not Guarded:** no alarm, no turret, no guard — a lease clause and a door that records. Breaching works and fails anyway.

**Dockets, Not Titles:** without the ledger, `find-the-bundle` is one tier harder and failure yields a convincing wrong bundle. With the ledger, shelf 388 is found in one action.

**Four Hundred Bundles:** `take-it-all` requires a vehicle, a route and a reason arranged during the Job.

**Paper Burns:** the easiest thing anybody can do here destroys every piece of proof the crew have and does not stop the buyer. Say the cost out loud first.

**The Log Is A Page:** the door's record goes to a leaseholder whose own records are filed on the Hill and counterparted in the paper barn — which is where [[acquisition]] is going.

## Threats / Consequences

› The door reads the opening and writes it, whether or not anybody used a key.
» On the bond, with a timestamp (*on-the-log-2*)
» The leaseholder's night service calls the unit's line (*a telephone nobody wants to answer*)

› The shelves are numbered and the numbers mean nothing without the book on the desk.
» The wrong bundle, convincingly (add a tier to `find-the-bundle`)
» Searching properly advances [[the-consignment-window]]

› The haulier's booking sheet by the door has a date on it, and the date is close.
» Advance [[the-consignment-window]]
» A photograph instead of the sheet (*a date, and nothing to show*)

› Two hundred kilos of paper, one door, and no vehicle.
» Have the PCs choose, in front of each other: the ledger, or shelf 388, or an armful of second copies
» Whatever they leave is on the haulier's sheet by morning

## Power Sets

None.

## Canon and flags

- The Stretch as prefab sprawl where nobody official comes and every official expects a bribe: [[kilbride-stretch]]. Paper as the medium precisely because it cannot be Harnessed: [[chancery-hill]], [[chancery-process]].
- **[BUILD CHOICE]** the bonded counting room, the docket index, and the "take it all" tier; see [[build-choices]] "Added by WP7b".
