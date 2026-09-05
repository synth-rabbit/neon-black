---
type: challenge
name: "Bohdan Adeyemi, \"Weights\""
slug: bohdan-adeyemi-challenge
status: review
source: custom
page: "294–300, 321–325, 306"
owner: WP4-trio1
canon_refs: ["Bible §2 hunter", "Bible §3 haves and have-nots", "Brief §2.3", "Brief §8", "Core p. 294–300", "Core p. 306", "Core p. 321–325"]
flags: [BUILD CHOICE]
player_safe: false
role: barrier
scale: 0
alias: "the man in the water door"
short_description: "A docker, not a soldier: twenty-five years of unloading coasters, one replacement hand, one warning, and thirty people behind him who will stop working."
limits:
  - {name: hurt-or-subdue, tier: 4}
  - {name: convince, tier: 4}
  - {name: get-past-him, tier: 3}
  - {name: pushed-too-far, tier: 3}
default_tags: ["hands like a loading clamp", "works the water door", "sets the counterweights himself", "the quay backs him"]
default_statuses: ["patient-2"]
specials:
  - {name: "He Warns You Once", text: "Before Bohdan delivers any Consequence in a scene, he tells the crew plainly what will happen if they continue, in a normal voice, and then waits one beat. A crew that stops gets no Consequence and no grudge. This warning happens once per scene and never twice."}
  - {name: "The House Backs Him", text: "When Bohdan takes a status, one member of the Weighhouse Muscle may take it instead, and that Challenge's Scale drops by one. If Weighhouse Muscle is not in the scene, it arrives on the next Consequence."}
  - {name: "Pushed Too Far", text: "When pushed-too-far maxes, he stops being careful: for the rest of the scene his Consequences are delivered without the warning, hurt-or-subdue rises to 5, and anything he throws is cargo. Nobody in the Gullet has seen this since a lock-keeper's son drowned nine years ago."}
  - {name: "Baseline, And It Matters", text: "Bohdan's cybernetics are replacements only — a left hand and a hip (Bible §2). He has no augmented strength, no sculpt and no bio-work, and the profile's tiers are what twenty-five years of unloading coasters actually produces. A Fitted body that beats him has proved nothing to the quay."}
threats:
  - threat: "He fills the water door, puts the pry bar down where everyone can see him put it down, and says what will happen."
    consequences:
      - {text: "Nobody gets past the water door while he is in it (Deny Them Something They Want).", statuses: [], tags: []}
      - {text: "He takes hold of somebody by the coat and moves them, without hurting them, to where they were before (moved-2 and burn a tag describing a position or an approach).", statuses: ["moved-2"], tags: []}
  - threat: "He sets a counterweight down on the balance harder than he needs to, and the room goes quiet."
    consequences:
      - {text: "Everyone in the Weighhouse remembers whose room this is (the crew take checked-2; add pushed-too-far-1 if they press).", statuses: ["checked-2", "pushed-too-far-1"], tags: []}
  - threat: "He steps in between somebody and Tally without looking away from them."
    consequences:
      - {text: "A docker's blow, from the shoulder, with a hand that is not his original one (broken-ribs-3).", statuses: ["broken-ribs-3"], tags: []}
      - {text: "He puts somebody on the quay stones and holds them there (pinned-3), and the market decides what happens next.", statuses: ["pinned-3"], tags: []}
  - threat: "He whistles once, flat, without turning his head."
    consequences:
      - {text: "The quay stops working (Present a New Challenge: Weighhouse Muscle at Scale 2).", statuses: [], tags: []}
power_sets: []
reuse_of: ""
---

# Bohdan Adeyemi, "Weights"

**Role:** barrier · **Scale:** 0 · **Alias:** *the man in the water door* · *He warns you once, in a normal voice, and then he waits.*

The Weighhouse's water door (BC-20; [[gullet-market]]). See [[bohdan-adeyemi]]. His role is **barrier**, not attacker: he is what stands between the quay and the counter, and almost every scene involving him ends without a Consequence, because he tells people what will happen and most people believe him.

A **Baseline** (Bible §2): a replacement left hand and a replacement hip, nine years old, and nothing else. He is dangerous because he is forty and has spent twenty-five years lifting things off boats, and because behind him is a market that will stop working ([[weighhouse-muscle]]).

## Limits

| Limit | Tier |
|---|---|
| hurt or subdue | 4 (5 after *Pushed Too Far*) |
| convince | 4 |
| get past him | 3 |
| pushed too far (progress) | 3 |

**get past him** at 3 is the intended route: the door is a door, and going around it is cheaper than going through him.

## Tags & statuses

hands like a loading clamp, works the water door, sets the counterweights himself, the quay backs him · *patient-2*

## Specials

**He Warns You Once:** before any Consequence, he says plainly what will happen and waits a beat. Stopping costs nothing.

**The House Backs Him:** [[weighhouse-muscle]] takes statuses for him and loses a Scale doing it; if absent, it arrives on his next Consequence.

**Pushed Too Far:** at max — no more warnings, *hurt or subdue* rises to 5, and anything he throws is cargo.

**Baseline, And It Matters:** replacements only, no sculpt, no bio-work (Bible §2, Brief §2.3).

## Threats / Consequences

› He fills the water door, puts the pry bar down where everyone can see, and says what will happen.
» Nobody gets past while he is in it (Deny Them Something They Want)
» He takes somebody by the coat and moves them back (*moved-2*; burn a position or approach tag)

› He sets a counterweight down harder than he needs to, and the room goes quiet.
» Everyone remembers whose room this is (*checked-2*; *pushed-too-far-1* if they press)

› He steps between somebody and Tally without looking away.
» A docker's blow from the shoulder (*broken-ribs-3*)
» Somebody on the quay stones and held there (*pinned-3*)

› He whistles once, flat, without turning his head.
» The quay stops working (Present a New Challenge: [[weighhouse-muscle]] at Scale 2)

## Power Sets

None. **Chromed Up** (Core p. 332) would break Baseline canon and would also miss the point of him.

## Canon and flags

- Baseline canon — cybernetics only as replacements, no sculpting or bio-manipulation: Bible §2, Brief §2.3, Plan A.6. The Gullet's order of precedence: [[gullet-market]].
- **[BUILD CHOICE]** (BC-102) *He Warns You Once* and *Pushed Too Far*; (BC-103) tiers and Threats.
