---
type: challenge
name: "The Weighhouse"
slug: the-weighhouse
status: review
source: custom
page: "294–300, 310, 303, 118–120, 159–167"
owner: WP4-trio1
canon_refs: ["Bible §1 who owns the tech", "Bible §5", "Bible §6", "Brief §4.4", "Brief §7.2", "Brief §8", "Core p. 294–300", "Core p. 303", "Core p. 310", "Tokyo p. 159–167"]
flags: [BUILD CHOICE, OPEN, TAO-REINTERPRETED]
player_safe: false
role: temptation
scale: 2
alias: "the only door that's open"
short_description: "A stone box on the quay with a water door, a counter door and a brass balance: the safest room under the Wall, the cheapest bed in Palisade, and a percentage that does not end."
limits:
  - {name: earn-standing, tier: 3}
  - {name: haggle, tier: 4}
  - {name: clear-the-slate, tier: 5}
  - {name: owed, tier: 5}
default_tags: ["the brass balance", "neutral ground the whole Foot enforces", "a back room with a bed in it", "two dozen runners in the Labyrinth", "everything gets weighed"]
default_statuses: ["welcome-2"]
specials:
  - {name: "The Percentage", text: "Anything the crew gain through the Weighhouse — a price, a bed, papers, a surgeon, a berth, a job, an introduction — they gain. They also take owed-1, chalked on the Slate by the counter door where the Gullet can read it. The house never refuses; it records."}
  - {name: "Nobody Bleeds Inside", text: "Violence inside the Weighhouse ends the scene's negotiation and gives everyone who took part barred-4: the counter is closed to them, and so, by the Foot's own enforcement, is every pawnbroker, surgeon, lock-keeper and runner in the network. barred is removed only by Tally, in person, at a price. This applies to the crew's enemies exactly as much as to the crew, which is what makes the room worth using."}
  - {name: "The Book Remembers", text: "Anything brought across the balance is weighed, described and entered — what it was, who brought it, and what they said about where it came from. Later, in any scene, a Consequence from any Key Player may be that somebody bought that page (Escalate the Situation). The crew are never told which page."}
  - {name: "Owed", text: "When owed maxes, the house collects: Tally names a job, it is not one the crew would have chosen, and refusing it converts the whole balance into barred-4 and the Slate is wiped in front of witnesses. Accepting resets owed to 2. This is the only way the Weighhouse ever threatens anyone."}
  - {name: "Asset, Not Ally", text: "While the crew are in good standing with the house (no owed-4 or higher, not barred), the Weighhouse functions as an asset: it can be used to buy, sell, hide a thing, hide a person for a night, find a surgeon, find a berth, or place a job. Each use is a Create effect through a Weighhouse contact and carries The Percentage."}
threats:
  - threat: "Tally slides the brass pan across the counter toward whatever the crew are carrying, and waits."
    consequences:
      - {text: "She names a price that is fair and lower than they need, and does not move off it (out-of-cash-3 or Have the PC choose: take the price, or take the price and owed-2).", statuses: ["out-of-cash-3"], tags: []}
      - {text: "She weighs it, asks one mild question about where it came from, and writes (The Book Remembers).", statuses: [], tags: []}
  - threat: "She puts food on the table in the back room before anyone has asked for any."
    consequences:
      - {text: "The crew are fed, warm, and inside for the first time since the Outfall (remove up to three tiers of physical exhaustion or exposure statuses; take owed-2).", statuses: ["owed-2"], tags: []}
      - {text: "She mentions, pleasantly, that the room is theirs as long as they want it, and chalks a figure.", statuses: [], tags: ["a figure on the Slate"]}
  - threat: "Somebody at the counter says a name the crew know, and Tally does not look up."
    consequences:
      - {text: "The crew learn something they needed from the network, for free, which is how the house shows what it is worth (create a story tag from the Book's knowledge; take owed-1).", statuses: ["owed-1"], tags: []}
      - {text: "Somebody else at the counter learns something about the crew on the same terms. Escalate the Situation.", statuses: [], tags: []}
  - threat: "A chalk figure by the counter door gets a line under it."
    consequences:
      - {text: "The Gullet reads the Slate. The crew's standing on the Foot moves with it (owed-2 and, at owed-4 or higher, the story tag known to be into the house).", statuses: ["owed-2"], tags: []}
      - {text: "A runner arrives with a chit and a job that is not optional (Owed; Present a New Challenge from whichever Key Player the job belongs to).", statuses: [], tags: []}
  - threat: "Somebody reaches across the balance for a person rather than an object."
    consequences:
      - {text: "Bohdan is in the doorway and the quay stops working (Present a New Challenge: Weighhouse Muscle; everyone who commits takes barred-4).", statuses: ["barred-4"], tags: []}
power_sets: []
reuse_of: ""
---

# The Weighhouse

**Role:** temptation · **Scale:** 2 (the house, its two doors, and the network that answers to the counter) · **Alias:** *the only door that's open* · *An asset and a temptation, which are the same object.*

The Gullet's old customs weighhouse on the quay: a stone box with a loading door on the water and a counter door on the market, a great brass balance under the roof that still works, a Slate by the door in chalk, and a back room that is an office, a kitchen and a vault (BC-20; [[gullet-market]]). It is [[marisol-okonkwo|Tally]]'s, and it is the safest room under the Wall, because the entire Foot needs it to exist and enforces its one rule for her.

For the crew it is the second scene of the Series and the only door open to them (Bible §5, §6). The Challenge is written as a **temptation** rather than an asset because that is the honest reading: everything it offers is real, useful, immediately necessary, and priced. The crew will take the offer. They should. The profile is what happens next.

## Limits

| Limit | Tier |
|---|---|
| earn standing | 3 |
| haggle | 4 |
| clear the Slate | 5 |
| owed (progress) | 5 |

**earn standing** at 3 is cheap and is meant to be: the house wants a working relationship and will meet a crew most of the way. **clear the Slate** at 5 is the hard one — paying off the house entirely, in a way the Gullet witnesses, and ending the percentage.

## Tags & statuses

the brass balance, neutral ground the whole Foot enforces, a back room with a bed in it, two dozen runners in the Labyrinth, everything gets weighed · *welcome-2*

## Specials

**The Percentage:** anything gained through the house is gained, and adds *owed-1*, chalked in public.

**Nobody Bleeds Inside:** violence inside gives every participant *barred-4* — counter, pawnbrokers, surgeons, lock-keepers, runners, all closed. It applies to the crew's enemies as much as to the crew, which is what makes the room worth using.

**The Book Remembers:** anything across the balance is entered. Later, in any scene, a Key Player's Consequence may be that somebody bought that page (Escalate the Situation). **[BUILD CHOICE]** (BC-102); **[OPEN]** (OQ-11, OQ-37) — who bought it is never specified by this profile.

**Owed:** at max, the house collects. Tally names a job the crew would not have chosen; refusing converts the balance to *barred-4* and wipes the Slate in front of witnesses; accepting resets *owed* to 2.

**Asset, Not Ally:** in good standing, the house buys, sells, hides a thing, hides a person for a night, finds a surgeon, finds a berth, or places a job — a Create effect through a contact, carrying The Percentage.

## Threats / Consequences

› Tally slides the brass pan across the counter and waits.
» A fair price, lower than they need (*out-of-cash-3*, or take the price and *owed-2*)
» She weighs it, asks one mild question, and writes (*The Book Remembers*)

› Food on the back-room table before anyone asked for any.
» Fed, warm and inside (remove up to three tiers of exhaustion or exposure; *owed-2*)
» The room is theirs as long as they want it (*a figure on the Slate*)

› Somebody at the counter says a name the crew know, and Tally does not look up.
» The crew learn something they needed, for free (create a story tag from the Book; *owed-1*)
» Somebody else learns something about them on the same terms (Escalate the Situation)

› A chalk figure by the counter door gets a line under it.
» The Gullet reads the Slate (*owed-2*; at *owed-4*+, *known to be into the house*)
» A runner with a chit and a job that is not optional (*Owed*; Present a New Challenge from the job's Key Player)

› Somebody reaches across the balance for a person rather than an object.
» Bohdan is in the doorway and the quay stops working (Present a New Challenge: [[weighhouse-muscle]]; *barred-4* to everyone who committed)

## Power Sets

None. The house is a room, a rule and a ledger.

## Canon and flags

- The fence as the crew's one day-one contact, referred by the crew leader; the crew at the bottom; hiring through the fence or her network: Bible §5, §6; Brief §7.1–7.2, §4.4. The Weighhouse: BC-20, [[gullet-market]].
- **[BUILD CHOICE]** (BC-102) the Slate, *owed* as the house's only weapon, and the Book as a Special rather than a secret to be discovered; (BC-103) tiers and Threats.
- **[TAO-REINTERPRETED]** (CR-1) Tao-touched goods reach the balance like everything else and are priced high because nobody can explain them ([[gullet-market]] development 3). Compare **Shady Tech Merchant** (Core p. 303) for a stall-level version of the same transaction.
- **[OPEN]** (OQ-11) nothing in this profile connects or disconnects Tally and [[upstart|Continuity]]; (OQ-37) *The Book Remembers* is the mechanism by which that question can be answered later without rewriting anything.
