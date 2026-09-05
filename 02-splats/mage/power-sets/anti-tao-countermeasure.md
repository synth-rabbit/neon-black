---
type: power-set
name: Anti-Tao Countermeasure
slug: anti-tao-countermeasure
status: review
source: custom
page: "326–333, 330"
owner: WP2-mage
canon_refs: ["Bible §2 mage", "Bible §3 Masquerade", "Brief §3.1", "Brief §4.1", "Brief §8", "Plan A.6", "Core p. 326–333", "Core p. 330"]
flags: [TAO-REINTERPRETED, BUILD CHOICE, OPEN]
player_safe: false
splat: none
category: Noise
applies_to: "Any Challenge representing a corporate countermeasure: a two-person survey team with a rack, a hardened room, a fielded null generator, a vehicle-mounted sweep."
default_tags: ["grounded lattice", "reads the room and logs it", "corporate paperwork"]
default_statuses: ["shielded-2"]
specials:
  - {name: "Grounding", text: "Once per scene, this Challenge can burn a tag representing a working — a worked item, a discipline in use, a made being — before a player makes a roll."}
  - {name: "Null Field", text: "Statuses given to this Challenge with Mythos tags are reduced by 1 tier. Statuses given with Noise or Self tags are not."}
  - {name: "It Went in the Log", text: "Whenever a Mythos tag is used in this Challenge's presence, it records who used it. At the end of the scene, one PC who used a Mythos tag takes on file-2, which does not expire at the end of the scene and which corporate security, countermeasure teams, and anyone who buys the log may invoke."}
threats:
  - threat: "A light on the rack changes color and somebody says a number out loud."
    consequences:
      - {text: "Ground a working (burn up to two tags, or three status tiers, representing a working).", statuses: [], tags: []}
      - {text: "Collapse a worked item (burn a Loadout or Mythos tag representing a worked object; the object is dead metal afterward).", statuses: [], tags: []}
      - {text: "Bring the field up across the room (create the story tag grounded room; while it stands, Mythos tags are indirectly relevant here).", statuses: [], tags: ["grounded room"]}
  - threat: "The team stops talking to each other and starts talking to somebody else."
    consequences:
      - {text: "Pin the practitioner as the source of the reading (marked-3 and Escalate the Situation).", statuses: ["marked-3"], tags: []}
      - {text: "Call it in: containment is nine minutes out (Present a New Challenge, or start a Countdown).", statuses: [], tags: []}
  - threat: "Somebody packs a spent casing, a length of chalked floor, or a sample into a case."
    consequences:
      - {text: "Take the working away to be looked at properly (Deny Them Something They Want; the sample is now a Key Player's problem to give back).", statuses: [], tags: []}
---

# Anti-Tao Countermeasure

**Applies to:** Any Challenge representing a corporate countermeasure — a two-person survey team with a rack, a hardened room, a fielded null generator, a vehicle-mounted sweep · **Category:** Noise · **Setting name:** none (this is the answer to Casters, not a Caster)

**MC only.** Canon: the corporations that the practice does not run "have a few rebel Tao users and **anti-Tao solutions** of their own" (Bible §2). This overlay is what a solution looks like on the table.

Three things it is, and one thing it is not:

- It is **Noise**. Nobody outside the practice channels Tao to block Tao. This is engineering — grounding, shielding, field-nulling — built by people who cannot reproduce what they are stopping and have never needed to.
- It is **primarily detection**. The Masquerade holds because nothing gets noticed (Brief §4.1); a corporation's first problem is not stopping a working but *knowing one happened*, and *It Went in the Log* is the Special that matters most in play.
- It is **bureaucratic**. Countermeasure crews file. What they file gets sold, subpoenaed, leaked, and bought, which is how a working in a stairwell on Tuesday becomes leverage in a boardroom in six weeks.
- It is **not a Mythos effect**. Nothing here is a counter-working and nothing here understands anything. A grounded room is a room with a lot of copper in it.

## Tags & statuses

grounded lattice, reads the room and logs it, corporate paperwork, *shielded-2*

## Specials

**Grounding:** Once per scene, this Challenge can burn a tag representing a working — a worked item, a discipline in use, a made being — before a player makes a roll.

**Null Field:** Statuses given to this Challenge with Mythos tags are reduced by 1 tier. Statuses given with Noise or Self tags are not.

**It Went in the Log:** Whenever a Mythos tag is used in this Challenge's presence, it records who used it. At the end of the scene, one PC who used a Mythos tag takes ***on file-2***, which does not expire at the end of the scene and which corporate security, countermeasure teams, and anyone who buys the log may invoke.

## Threats / Consequences

› A light on the rack changes color and somebody says a number out loud.
» Ground a working (burn up to two tags, or three status tiers, representing a working)
» Collapse a worked item (burn a Loadout or Mythos tag representing a worked object; the object is dead metal afterward)
» Bring the field up across the room (create the story tag *grounded room*; while it stands, Mythos tags are indirectly relevant here)

› The team stops talking to each other and starts talking to somebody else.
» Pin the practitioner as the source of the reading (*marked-3*; Escalate the Situation)
» Call it in: containment is nine minutes out (Present a New Challenge, or start a Countdown)

› Somebody packs a spent casing, a length of chalked floor, or a sample into a case.
» Take the working away to be looked at properly (Deny Them Something They Want; the sample is now a Key Player's problem to give back)

## Limits

Suggested on the host Challenge: **wreck 3** for a rack or a generator, **hurt or subdue 3** for a two-person team, **convince 4** — a countermeasure crew are contractors with a checklist and no stake in the outcome.

## What this hands to and takes from other packages

- The cross-cutting **Challenge profile** for an anti-Tao countermeasure is [[anti-tao-countermeasure-challenge]] (WP5): the fixed installation, with `detect` and `shutdown-or-override` Limits. This file is the overlay only; that profile applies it (BC-134). The man-portable versions are [[null-field-emitter]] and [[tao-null-round]].
- The PC-side scar a practitioner carries after surviving one is [[countermeasure-scar]].
- Which corporations field which countermeasures: Meliora's **Adjunct Series** and AP&I's **Field Assurance** ([[corp-a]], [[corp-c]], [[corp-b]]; BC-117). How good they are, and whether either can reproduce a working, stays **[OPEN]** (OQ-24).
- [[corp-b|Orison Defense Systems]] is the corporation that would be worst served by these existing and best placed to sell them. Nothing here decides what it does about that.

## Canon and flags

- Canon relied on: anti-Tao solutions exist and belong to the corporations the practice does not run (Bible §2); the practice stays hidden and the corporations prefer it hidden (Bible §2, §3); the Masquerade is cheap because of the Noise plus active cleanup (Brief §4.1).
- **[TAO-REINTERPRETED]** (CR-1) This is the setting's replacement for anti-Mythos content in the book — including the *Arcane* Power Set's *Counterspell* (Core p. 330), which this overlay's *Grounding* deliberately mirrors in mechanics and inverts in category: *Counterspell* is magic answering magic; *Grounding* is copper answering a practice, and it never asks what it is grounding.
- **[BUILD CHOICE]** (BC-70) That countermeasures are Noise-category engineering, that detection outweighs suppression, and that their durable output is a **record** rather than an injury (which is what [[countermeasure-scar]] carries).
- **[OPEN]** (OQ-24) How far the countermeasure programmes actually go, and whether either corporation can reproduce a working rather than merely stop one.
