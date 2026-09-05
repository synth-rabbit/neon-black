---
type: challenge
name: "Wuji Operative"
slug: wuji-operative-challenge
status: review
source: custom
page: "294–300, 330"
owner: WP4-trio3
canon_refs: ["Bible §1 tech and magic", "Bible §2 mage", "Bible §3 Masquerade", "Brief §3.1–3.3", "Brief §8", "Plan A.6", "Core p. 294–300", "Core p. 330"]
flags: [BUILD CHOICE, TAO-REINTERPRETED, OPEN]
player_safe: false
role: attacker
scale: 0
alias: "somebody's assistant, waiting outside"
short_description: "A practitioner sent by Aldine House to close something quietly: an unremarkable person who keeps a discipline and would much rather buy you."
limits:
  - {name: hurt-or-subdue, tier: 4}
  - {name: break-the-condition, tier: 3}
  - {name: convince, tier: 5}
  - {name: expose, tier: 6}
default_tags: ["a tech-augmented practice", "unremarkable in every district", "a Tao-worked item that is not a weapon", "House money in the field"]
default_statuses: ["composed-2", "unhurried-2"]
specials:
  - {name: "The Condition", text: "The operative's practice runs only while a condition holds — stillness, silence, a level floor, an unbroken line of sight, whatever this one keeps. The condition is visible to anyone paying attention and is stated to the players the first time it matters. Any status that breaks the condition (deafened, jostled, blinded, drowned in Noise, dosed) also adds a tier to break-the-condition. While break-the-condition is maxed the operative has no practice at all and is an ordinary person in ordinary clothes; it resets at the end of the scene, or immediately if they are given a minute alone."}
  - {name: "Worked, Not Willed", text: "Everything this Challenge does is a discipline producing a result, never a being acting. It cannot be bargained with, banished, exorcised, commanded, or appealed to, and neither can anything it makes — there is nothing there to talk to. Book Consequences that dispel, banish, or negotiate with a Mythos do not apply; Consequences that break attention, foul the senses, or remove the item do."}
  - {name: "Buys First, Twice", text: "The operative opens with an offer and, if refused, repeats it once with more money. Only after the second refusal do they act. If the crew ever accepts, the operative leaves and does not return during this job — but the House now holds a favour, which is a story tag on the crew."}
  - {name: "Nothing Is Left Behind", text: "The operative carries one Tao-worked item and no identification, and will spend an action recovering the item before escaping, being captured, or bleeding out. If they cannot recover it, they burn it. A crew that ends a scene holding an intact Wuji item has something no laboratory in Palisade has ever had."}
threats:
  - threat: "A quiet person you had not registered as being in the room says your name, correctly, and offers to pay for the thing you are holding."
    consequences:
      - {text: "The offer is above market and comes with the House's protection attached, which is a leash (tempted-3).", statuses: ["tempted-3"], tags: ["a favour owed to the House"]}
      - {text: "Refused twice, they stop talking and set their feet, and the room gets very still (unnerved-2).", statuses: ["unnerved-2"], tags: []}
  - threat: "They stand still, breathe out, and do not move again — and something in the room stops working."
    consequences:
      - {text: "A door will not open, a weapon will not cycle, a lift will not answer (burn a loadout or equipment tag).", statuses: [], tags: []}
      - {text: "A drone, a lens, or a cybernetic eye simply does not see the operative for as long as they stand there (lost-sight-of-3).", statuses: ["lost-sight-of-3"], tags: []}
      - {text: "The fire in a doorway goes out; the water in a flooded gallery holds back; the crew's route is closed by nothing at all (Deny Them Something They Want).", statuses: [], tags: []}
  - threat: "They take an ordinary object out of a coat pocket — a lamp, a lock, a length of cord — and set it down."
    consequences:
      - {text: "The object does the impossible thing it was worked to do, once, exactly as specified (create a story tag such as a door that stays shut, a light nobody else can see by, or a knot that will not come undone).", statuses: [], tags: []}
      - {text: "Whatever the object is pointed at stops (pinned-in-place-3 or silenced-3).", statuses: ["pinned-in-place-3"], tags: []}
  - threat: "They apologize, and then move faster and more precisely than a person of that age and build should."
    consequences:
      - {text: "A short, economical, ugly piece of violence with an ordinary object (struck-3 or choked-3).", statuses: ["struck-3"], tags: []}
      - {text: "They take a hit meant for the item instead of for themselves (the operative takes the status; the item is untouched).", statuses: [], tags: []}
  - threat: "They glance once at a face they were not expecting to see here and say nothing about it."
    consequences:
      - {text: "Escalate the Situation: Aldine House now knows who was present, and a scholarship letter follows within the week.", statuses: [], tags: ["noticed by the House"]}
      - {text: "Present a New Challenge: Product Integrity Recovery Team, arriving to handle the part of this that can be handled with money.", statuses: [], tags: []}
power_sets: []
reuse_of: "Arcane (Core p. 330), reinterpreted as a Tao discipline; body and gear built from Investigator (Core p. 305) and Mercenary Gunslinger (Core p. 307) where a fight is unavoidable."
---

# Wuji Operative

**Role:** attacker · **Scale:** 0 (an individual) · **Alias:** *somebody's assistant, waiting outside* · *A practitioner sent by Aldine House to close something quietly.*

The Wuji's answer of last resort, and the House regards sending one as an admission that money failed. Not an assassin and not a mystic: a middle-aged person in unremarkable clothes who was already in the room, knows the crew's names, has the House's chequebook, and keeps a discipline that lets them do one or two impossible things if the conditions hold and nobody is shouting.

They fight badly and only when there is no alternative, and they fight the way people who do not enjoy it fight — quickly, with whatever is to hand, aiming to end it. What makes them dangerous is not damage. It is that the door will not open, the weapon will not cycle, the drone does not see them, and the crew has no vocabulary for any of it.

**[TAO-REINTERPRETED]** (CR-1) Everything here is Tao as this vault defines it: a practice kept under a condition, producing a result. No legend, no Source cult, no patron, nothing with a will (Brief §3.1; [[pillars]]). The book's **Arcane** Power Set (Core p. 330) is the closest mechanical match and can be used with every reference to a Mythos, a Source's sensibilities, and Conjurations struck out; *Counterspell* becomes "burn a tag representing a Tao-worked item or a practice being kept," and *Spellcraft*'s story tags are results of a discipline, not spells. WP2's mage Power Set (`02-splats/mage/power-sets/`) supersedes it when written.

## Limits

| Limit | Tier |
|---|---|
| hurt or subdue | 4 |
| break the condition | 3 |
| convince | 5 |
| expose | 6 |

*Break the condition* is the intended way in and is deliberately the cheapest. *Expose* is 6 because the House has spent a century making sure there is nothing to expose them with.

## Tags & statuses

a tech-augmented practice · unremarkable in every district · a Tao-worked item that is not a weapon · House money in the field · *composed-2* · *unhurried-2*

## Specials

**The Condition:** The practice runs only while a condition holds — stillness, silence, a level floor, an unbroken line of sight. The condition is visible and is stated to the players the first time it matters. Statuses that break it also add a tier to *break the condition*; while that Limit is maxed the operative is an ordinary person in ordinary clothes. It resets at the end of the scene, or after a minute alone.

**Worked, Not Willed:** Everything this Challenge does is a discipline producing a result. Nothing here can be bargained with, banished, exorcised, or commanded — there is nothing there to talk to. Consequences that dispel or negotiate with a Mythos do not apply; Consequences that break attention, foul the senses, or take the item do.

**Buys First, Twice:** Opens with an offer; repeats it once, higher. Only after a second refusal do they act. Acceptance ends the encounter and leaves the crew with *a favour owed to the House*.

**Nothing Is Left Behind:** One Tao-worked item, no identification. They will spend an action recovering the item before escaping, capture, or bleeding out, and burn it if they cannot. A crew holding an intact Wuji item has something no laboratory in Palisade has ever had.

## Threats / Consequences

› A quiet person you had not registered says your name, correctly, and offers to pay for what you are holding.
» An offer above market with the House's protection attached (*tempted-3*; *a favour owed to the House*)
» Refused twice, they stop talking and set their feet (*unnerved-2*)

› They stand still, breathe out, and do not move again — and something in the room stops working.
» A door, a weapon, a lift will not answer (burn a loadout or equipment tag)
» A drone, a lens, or a cybernetic eye does not see them while they stand there (*lost-sight-of-3*)
» A fire goes out; floodwater holds; the route closes by nothing at all (Deny Them Something They Want)

› They take an ordinary object from a coat pocket and set it down.
» It does the one impossible thing it was worked to do, exactly as specified (*a door that stays shut*, *a light nobody else can see by*, *a knot that will not come undone*)
» Whatever it is pointed at stops (*pinned-in-place-3* or *silenced-3*)

› They apologize, and then move faster and more precisely than they should.
» Short, economical, ugly violence with an ordinary object (*struck-3* or *choked-3*)
» They take a hit meant for the item (the operative takes the status; the item is untouched)

› They glance once at a face they did not expect and say nothing.
» Escalate the Situation: the House knows who was present; a scholarship letter follows (*noticed by the House*)
» Present a New Challenge: [[product-integrity-team]], for the part that money can still handle

## Power Sets

[[wuji-operative]] (WP2-mage) is the overlay for any *other* practitioner Challenge acting for the House — an instructor, a placed member on an errand; this profile is the House's field agent written in full and does not stack it (its *Arrest* and *The Condition* describe the same discipline from two sides — BC-134). **Arcane** (Core p. 330) — **[TAO-REINTERPRETED]** (CR-1) as above. **Connected & Protected** (Core p. 328) for a senior member such as [[constance-marchetti]]. **Master-Crafted** (Tokyo p. 132) for the one Tao-worked item, which is a made thing and not a blessed one.

## Canon and flags

- Casters are pure Tao users who augment the practice with technology (Bible §2); the society is secret and hides itself (Bible §2, §3); Tao is impersonal and never has a will (Brief §3.1).
- **[BUILD CHOICE]** (BC-120) the operative as the House's last resort and the *Buys First, Twice* behaviour; (BC-121) *The Condition* as the mechanical shape of a Ritual-as-discipline for NPCs, so that anti-Tao countermeasures (Meliora's Adjunct doses, AP&I's Noise flooders) have something concrete to attack.
- **[TAO-REINTERPRETED]** (CR-1) the *Arcane* Power Set and every effect above.
- **[OPEN]** (OQ-6) nobody in the scene has a word for what happened. **[OPEN]** (OQ-14) nothing here requires a Tao-dense place.
