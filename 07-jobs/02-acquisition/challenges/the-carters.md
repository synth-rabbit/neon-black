---
type: challenge
name: "The Carters"
slug: the-carters
status: review
source: custom
page: "294–300, 306, 307, 312, 291"
owner: WP7c
canon_refs: ["Bible §3 power structure", "Brief §8", "Plan A.6", "Core p. 285", "Core p. 291", "Core p. 294–300", "Core p. 306", "Core p. 307"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: pursuer
scale: 2
alias: "a records-contractor van with a real plate"
short_description: "Five freelancers who move things for people who cannot be seen moving them. Hired eleven weeks ago through three intermediaries to take the same volume, told it must arrive unread, and waiting on the road because they are thieves on roads, not thieves in buildings."
limits:
  - {name: outrun-or-lose-them, tier: 4}
  - {name: hurt-or-subdue, tier: 4}
  - {name: buy-them-off, tier: 3}
  - {name: convince-barrow, tier: 5}
default_tags: ["a real contractor plate", "eleven weeks of watching this apron", "bonded transit boxes", "three exits and five people", "paid half in advance, half spent"]
default_statuses: ["patient-3"]
specials:
  - {name: "Thieves On Roads", text: "The Carters do not enter buildings while anybody is in them. They have never been inside the Repository and will not go in during this job. Everything they do happens on the apron, the fence line, the drone-lane underpass, or the grid — which is why the escape is the climax (Core p. 291). If the crew somehow lose the volume inside the building, the Carters simply wait; they have six days too."}
  - {name: "He Talks First", text: "Barrow opens with an offer, every time, in cash, and it is a fair price. Buy them off is tier 3 because he genuinely prefers it. The offer stands until the first shot; after that it is gone for the rest of the Series and this Challenge's convince Barrow rises to 6."}
  - {name: "It Must Arrive Unread", text: "Barrow was told the volume must arrive unread, and he does not know why; it is the only part of the job that has ever bothered him. He will ask, once, whether the crew opened it. A crew who convince him they did not gets a better price and a Carter who is later surprised. A crew who tell him the truth about what is in it can, with convince Barrow at 5, turn the ambush into a conversation — he will not switch sides, but he will take the money and deliver an empty box, and be somebody's problem instead of theirs."}
  - {name: "Three Exits", text: "There are exactly three ways off the apron, and the Carters cover all three with five people, which is the most five people can do. Any Effect that creates a fourth way out — a hole, a roof, a drone-lane, a vehicle nobody counted — drops outrun or lose them by two tiers. That is what the Prep Sequence is for."}
threats:
  - threat: "A van reverses up to the roller door with its lamp on, on a night the schedule does not have a collection."
    consequences:
      - {text: "The crew are on an apron with their hands full and somebody else's headlights on them (caught-in-the-open-2).", statuses: ["caught-in-the-open-2"], tags: []}
  - threat: "Barrow gets out first, alone, hands visible, and names a figure."
    consequences:
      - {text: "The offer is real and the crew now have to say no in front of each other (a fair price, refused).", statuses: [], tags: ["a fair price, refused"]}
      - {text: "Whatever they say, two Carters have moved to the fence cuts while he was talking (flanked-2).", statuses: ["flanked-2"], tags: []}
  - threat: "Somebody breaks for the grid, and four kilometres of identical prefab has no cover in it at all."
    consequences:
      - {text: "Run down in the open (gunshot-wound-2, or grabbed-3 if the Carters would rather not kill anyone tonight — they would rather not).", statuses: ["gunshot-wound-2", "grabbed-3"], tags: []}
      - {text: "The volume goes down in the road and somebody else picks it up (the loot changes hands).", statuses: [], tags: ["the loot changes hands"]}
  - threat: "The van, which has a real plate, drives at the crew's vehicle rather than after it."
    consequences:
      - {text: "A ramming exchange in a drone-lane underpass: run it on the vehicles' own tags and Scale (Core p. 118–120, 108). Loser takes wrecked-3.", statuses: ["wrecked-3"], tags: []}
  - threat: "A fight over a book, on an apron, in front of a night shift."
    consequences:
      - {text: "Witnessed and public. This is a Threat toward [[secret-war-goes-public]] — one tier if it reaches a feed, two if anything happens that no Baseline could have done.", statuses: [], tags: []}
  - threat: "The crew get away clean with it."
    consequences:
      - {text: "Barrow has spent half a fee he now cannot return, to a client he cannot contact, and the Carters become a standing story tag: somebody in Palisade is owed and knows the crew's faces (the Carters are owed).", statuses: [], tags: ["the Carters are owed"]}
power_sets: []
reuse_of: "Built from Mercenary Gunslinger (Core p. 307) for the four, with Barrow voiced as a Criminal Overlord (Core p. 306) scaled down to a five-person crew; the vehicle exchange uses no profile at all (Core p. 118–120)."
---

# The Carters

**Role:** pursuer · **Scale:** 2 (five people and a van) · **Alias:** *a records-contractor van with a real plate* · *Thieves on roads, not thieves in buildings.*

A freelance crew of five who move things for people who cannot be seen moving them. Bonded transit boxes, a records-contractor plate that is genuinely registered, and a working method: they never enter a building while anyone is in it, and they have never once been in the same room as a thing's owner. The street named them for what they do and they kept it, the way the Smokes and the Sidings did ([[cinder-yards]]).

They were hired eleven weeks ago, through three intermediaries, to take the Coldwater counterpart out of the Chancery's records store at Kilbride. Half in advance. The only instruction beyond the description was that it must arrive **unread**.

This is the *another team or an insider is pulling the same job* complication (Core p. 285) in its second and larger form, staged exactly as the book's own worked example stages it (Core p. 291): the rival crew want the loot and will push into direct confrontation, but being thieves they prefer an ambush — so if the crew get the volume first, the Carters set it on the escape route. Written for [[acquisition-08-collection-night]]; live as a background force from [[acquisition-05-the-prep-sequence]] onward.

**They are not Continuity's cell and must not be voiced as one.** Continuity's crisis-response teams are armoured, serialled, lawful, and arrive at a cordon ([[continuity-crisis-response-cell]]). The Carters are five people in coats with a van, and whether their client is the same account as the one in the volume is **[OPEN]** (OQ-37) and is not answered here.

## Limits

| Limit | Tier |
|---|---|
| outrun or lose them | 4 |
| hurt or subdue | 4 |
| buy them off | 3 |
| convince Barrow | 5 |

## Tags & statuses

a real contractor plate · eleven weeks of watching this apron · bonded transit boxes · three exits and five people · paid half in advance, half spent · *patient-3*

## Specials

**Thieves On Roads:** they will not enter the building during this job.

**He Talks First:** Barrow opens with a fair cash offer; the offer dies with the first shot and `convince Barrow` rises to 6.

**It Must Arrive Unread:** he asks, once. At `convince Barrow` 5 he will take the money and deliver an empty box.

**Three Exits:** five people cover exactly three; a fourth way out drops `outrun or lose them` by two.

## Threats / Consequences

› A van reverses up to the roller door on a night with no collection.
» Hands full, headlights on them (*caught-in-the-open-2*)

› Barrow gets out first, alone, hands visible, and names a figure.
» A real offer, refused in front of each other (*a fair price, refused*)
» Two Carters reach the fence cuts while he talks (*flanked-2*)

› Somebody breaks for the grid; four kilometres with no cover.
» Run down in the open (*gunshot-wound-2*, or *grabbed-3*)
» The volume goes down in the road (*the loot changes hands*)

› The van drives at their vehicle rather than after it.
» A ramming exchange on the vehicles' own tags and Scale (*wrecked-3*)

› A fight over a book in front of a night shift.
» A Threat toward [[secret-war-goes-public]]

› The crew get away clean.
» Barrow owes a client he cannot contact (*the Carters are owed*)

## Power Sets

None by default. **Surveillance Data Fed** (Core p. 333) is the correct overlay if the MC decides the Carters' client has been feeding them the crew's movements — which is a way of answering OQ-37 in play, and should be used only deliberately.

## Canon and flags

- Corporate security is exactly as legal as the police, and freelance crews are neither (Bible §3). Rival-crew ambush on the escape route: Core p. 291. Acquisition complications: Core p. 285.
- **[BUILD CHOICE]** the Carters, Barrow, their method, and their eleven-week retainer. Registered in [[build-choices]] "Added by WP7c".
- **[OPEN]** (OQ-37) their client is not named; (OQ-11) nothing here connects them to Tally.
