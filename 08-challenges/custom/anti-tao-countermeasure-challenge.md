---
type: challenge
name: "Anti-Tao Field Installation"
slug: anti-tao-countermeasure-challenge
status: review
source: custom
page: ""
owner: WP5
canon_refs: ["Bible §2", "Bible §3", "Brief §3.1", "Core p. 294–300"]
flags: [TAO-REINTERPRETED, BUILD CHOICE]
player_safe: false
role: barrier
scale: 1
alias: "The Quiet Room"
short_description: "A corp-engineered device or field that detects and suppresses Tao-worked effects — mundane tech built to counter Tao, not itself Tao-touched."
limits:
  - {name: detect, tier: 2}
  - {name: shutdown-or-override, tier: 4}
default_tags: ["anti-Tao field emitters", "corp-engineered, not Tao itself", "sensor array tuned to worked signatures"]
default_statuses: []
specials:
  - {name: "Mundane by Design", text: "This Challenge is engineering, not a Tao construct — it has nothing that Tao can persuade, banish, or bargain with, and nothing here is TAO-REINTERPRETED as a being. Limit banish: – (immune). It is overcome only by shutdown-or-override or by destroying it as a piece of hardware."}
  - {name: "Dampening Field", text: "While active, any Tao-worked loadout tag or Mythos-category power tag used inside the field's radius is treated as though it had a negative status equal to detect's current tier applied against it. This is the field doing its job, not Tao behaving unpredictably (Tao never has a will, [[style-guide]] §6)."}
threats:
  - threat: "A low hum starts under the floor, felt before it's heard."
    consequences:
      - {text: "Anyone channeling or carrying a Tao-worked item in the radius takes null-field-1, applying to any Tao-worked tag they try to use.", statuses: ["null-field-1"], tags: []}
  - threat: "Sensor lights sweep, hunting for the telltale signature of worked Tao."
    consequences:
      - {text: "detect advances a tier; at max, the source is pinpointed and flagged.", statuses: [], tags: ["flagged as anomalous"]}
      - {text: "Present a New Challenge: Security Guard or Corporate Executive (generic reuse, [[generic-reuse-map]]) is alerted to investigate the flag.", statuses: [], tags: []}
  - threat: "The field intensifies, and the hum becomes a pressure behind the eyes."
    consequences:
      - {text: "null-field advances a tier for everyone in the radius using Tao-worked tags.", statuses: ["null-field-1"], tags: []}
  - threat: "shutdown-or-override maxes out."
    consequences:
      - {text: "The field goes dark. Remove all null-field statuses in the radius; Tao flows unimpeded here again.", statuses: [], tags: []}
      - {text: "If the shutdown was noisy, Present a New Challenge: whoever notices the field went offline.", statuses: [], tags: []}
power_sets: [anti-tao-countermeasure]
reuse_of: ""
---

# Anti-Tao Field Installation

**Role:** barrier · **Scale:** 1 (a single installation — a room, a checkpoint, a vault) · **Alias:** The Quiet Room · *A corp-engineered device or field that detects and suppresses Tao-worked effects.*

The cross-cutting anti-Tao countermeasure Plan WP5 calls for: what a Big Three corp *not* controlled by the Wuji fields on its own initiative (Bible §3; Brief §3.1 — "the other corporations have a few rebel Tao users and anti-Tao solutions of their own"). Owned by no single Key Player; any of the corps, Continuity, or even a well-funded Baseline outfit could plausibly deploy one. Its man-portable cousins are [[tao-null-round]] (ammo) and [[null-field-emitter]] (a loadout item); this profile is the fixed or larger-scale installation version of the same engineering.

**[TAO-REINTERPRETED]** in the specific sense of Brief §3.2: this Challenge is written as this package's answer to the book's Source-Touched & Conjurations *counter*-measures. It is not itself Tao-touched — it is mundane technology built to counter Tao, and that distinction is load-bearing (see Specials).

## Limits

| Limit | Tier |
|---|---|
| detect | 2 |
| shutdown or override | 4 |

## Tags & statuses

anti-Tao field emitters, corp-engineered, not Tao itself, sensor array tuned to worked signatures

## Specials

**Mundane by Design:** Engineering, not a Tao construct. `banish: –` (immune); overcome only by `shutdown-or-override` or by destroying it as hardware.

**Dampening Field:** Any Tao-worked loadout tag or Mythos-category power tag used inside the radius is treated as though it carried a negative status equal to `detect`'s current tier. The field is doing its job; Tao is not misbehaving ([[style-guide]] §6).

## Threats / Consequences

› A low hum starts under the floor, felt before it's heard.
» Anyone with a Tao-worked tag in the radius takes *null-field-1*

› Sensor lights sweep, hunting for the telltale signature of worked Tao.
» `detect` advances; at max, the source is pinpointed (*flagged as anomalous*)
» Present a New Challenge: Security Guard or Corporate Executive investigates ([[generic-reuse-map]])

› The field intensifies, and the hum becomes a pressure behind the eyes.
» `null-field` advances a tier

› `shutdown-or-override` maxes out.
» The field goes dark; all `null-field` statuses in the radius are removed
» If noisy, Present a New Challenge: whoever notices it went offline

## Power Sets

[[anti-tao-countermeasure]] (WP2-mage) — the Noise overlay for any countermeasure element: *Grounding*, *Null Field*, *It Went in the Log*. This profile is the fixed installation the overlay sits on; apply it rather than restating it (BC-134). Both are Noise-category engineering, never a Tao effect, and neither gives Tao a will.

## Canon and flags

- Bible §3, Brief §3.1: anti-Tao solutions belong to corps outside the Wuji's control; Tao is never given a will ([[style-guide]] §6, Brief §3.1).
- **[TAO-REINTERPRETED]** this profile's relationship to the book's Source-Touched material — a countermeasure, not a Source or Conjuration.
- **[BUILD CHOICE]** classifying the device as mundane rather than Tao-touched (matches the parallel choice on [[tao-null-round]] and [[null-field-emitter]]; registered once for all three in [[build-choices|BC-27 to BC-30]]).
