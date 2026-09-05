---
type: power-set
name: Wuji Operative
slug: wuji-operative
status: review
source: custom
page: "326–333"
owner: WP2-mage
canon_refs: ["Bible §2 mage", "Bible §3 power structure", "Bible §3 Masquerade", "Brief §3.1", "Brief §8", "Plan A.6", "Core p. 326–333", "Core p. 297–300"]
flags: [TAO-REINTERPRETED, BUILD CHOICE, OPEN]
player_safe: false
splat: mage
category: Mythos
applies_to: "Any Challenge representing a trained practitioner acting for the practice — an instructor, a placed member on an errand, a house agent sent to close something."
default_tags: ["kept the forms for thirty years", "no record anywhere", "unhurried"]
default_statuses: ["composed-2"]
specials:
  - {name: "Nothing Rushes Them", text: "When a PC tries to hurry, startle, provoke, or crowd this Challenge, they first take off-balance-2."}
  - {name: "Arrest", text: "Once per scene, as a Consequence, this Challenge stops one moving thing dead — a vehicle, a round in the air, a person mid-step, a closing door — giving it halted-3. Anything held this way stays held while the Challenge keeps its stance and is released the moment the stance breaks."}
  - {name: "The House Answers", text: "Once per job, as a Consequence, another member arrives who was already nearby and has been for some time (Present a New Challenge: a second Wuji Operative at Scale 1, or a Chancery official, physician, or security supervisor who has been asked a favor)."}
  - {name: "Nothing to Take", text: "This Challenge carries no identification, no device, and nothing worked. Attempts to trace, tag, or prove anything about them by physical evidence fail; the story tag no record anywhere cannot be burned."}
threats:
  - threat: "Sets their stance and breathes out."
    consequences:
      - {text: "Arrest a body mid-motion, holding it where it stands.", statuses: ["held-3"], tags: []}
      - {text: "Still the room — the shouting stops, the alarm does not carry, the momentum goes out of the scene (burn a tag representing noise, alarm, panic, or momentum).", statuses: [], tags: []}
      - {text: "Take a hit without moving (burn a status they would otherwise have taken, up to tier 3).", statuses: [], tags: []}
  - threat: "Reaches inside a coat, unhurried, and does not take anything out yet."
    consequences:
      - {text: "Produce a worked item nobody saw them carrying (create a story tag such as worked shell, chalked ward, folded rule).", statuses: [], tags: ["worked item in hand"]}
      - {text: "Spend it (breached-4 against a barrier, or warded-off against an attack, or a story tag standing between the PCs and what they want).", statuses: ["breached-4"], tags: []}
  - threat: "Names something about a PC they should have no way of knowing."
    consequences:
      - {text: "Make an offer that is not a threat and is worse than one (tempted-2, or a story tag recording what was offered).", statuses: ["tempted-2"], tags: []}
      - {text: "Withdraw the offer and leave, and everything the PCs did in this scene is now on a file somewhere (Escalate the Situation).", statuses: [], tags: []}
---

# Wuji Operative

**Applies to:** Any Challenge representing a trained practitioner acting for the practice — an instructor, a placed member on an errand, a house agent sent to close something · **Category:** Mythos · **Setting name:** Caster

**MC only.** Everything about this overlay assumes facts a Caster PC does not have ([[casters]] §2). The House's field agent written as a full Challenge is [[wuji-operative-challenge]] (WP4-trio3); this overlay is for any other practitioner Challenge acting for the House and is not stacked on that profile (BC-134). Nothing an operative does in a scene needs to *say* what they are, and the overlay is written so that it does not: a bystander sees a calm person in unremarkable clothes to whom violence does not seem to apply.

## Tags & statuses

kept the forms for thirty years, no record anywhere, unhurried, *composed-2*

## Specials

**Nothing Rushes Them:** When a PC tries to hurry, startle, provoke, or crowd this Challenge, they first take *off-balance-2*.

**Arrest:** Once per scene, as a Consequence, this Challenge stops one moving thing dead — a vehicle, a round in the air, a person mid-step, a closing door — giving it *halted-3*. Anything held this way stays held while the Challenge keeps its stance and is released the moment the stance breaks.

**The House Answers:** Once per job, as a Consequence, another member arrives who was already nearby and has been for some time (Present a New Challenge: a second Wuji Operative at Scale 1, or a Chancery official, physician, or security supervisor who has been asked a favor).

**Nothing to Take:** This Challenge carries no identification, no device, and nothing worked. Attempts to trace, tag, or prove anything about them by physical evidence fail; the story tag *no record anywhere* cannot be burned.

## Threats / Consequences

› Sets their stance and breathes out.
» Arrest a body mid-motion, holding it where it stands (*held-3*)
» Still the room — the shouting stops, the alarm does not carry, the momentum goes out of the scene (burn a tag representing noise, alarm, panic, or momentum)
» Take a hit without moving (burn a status they would otherwise have taken, up to tier 3)

› Reaches inside a coat, unhurried, and does not take anything out yet.
» Produce a worked item nobody saw them carrying (create a story tag such as *worked shell*, *chalked ward*, *folded rule*)
» Spend it (*breached-4* against a barrier, or *warded off* against an attack, or a story tag standing between the PCs and what they want)

› Names something about a PC they should have no way of knowing.
» Make an offer that is not a threat and is worse than one (*tempted-2*, or a story tag recording what was offered)
» Withdraw the offer and leave, and everything the PCs did in this scene is now on a file somewhere (Escalate the Situation)

## Limits

Suggested on the host Challenge: **hurt or subdue 4**, **convince 2** (this Challenge is not persuaded; it is *paid*, and the price is a task), **catch 5**. An operative who has decided to leave leaves.

## Canon and flags

- Splat canon this overlay obeys (Plan A.6): a Caster is a pure Tao user who augments with tech (Bible §2) — an operative's effects come from a practice and a worked item, never from a mod, and never from anything that wants something. **Tao is given no intent anywhere in this file.**
- Recruitment is canon (Bible §2: the society "identifies talented people and brings them into the fold"), which is what the third Threat is: an operative who meets a talented stranger makes an offer.
- **[TAO-REINTERPRETED]** (CR-1) This overlay replaces nothing in the book, but it stands in the slot the *Arcane* Mythos Power Set occupies (Core p. 330); *Arcane*'s "access to a Source, usually an Esoteric practice" is reusable as written once *Source* is read as gateway — see [[existing-power-sets]].
- **[BUILD CHOICE]** (BC-68) The operative's signature effect is **arrest** — the same discipline as [[aldine-forms]], so that a PC who has learned the forms recognizes what is being done to them. Scale, tags, and Specials are this package's.
- **[OPEN]** (OQ-28) Whether the house fields anything more dangerous than this, and what it does about a practitioner who refuses it, are Key Player facts for WP4 (`06-key-players/tao-society/`).
