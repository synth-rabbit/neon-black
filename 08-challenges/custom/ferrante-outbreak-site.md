---
type: challenge
name: "Nanite Hot Zone"
slug: ferrante-outbreak-site
status: review
source: custom
page: ""
owner: WP5
canon_refs: ["Bible §2", "Bible §3", "Core p. 294–300", "Core p. 310"]
flags: [OPEN]
player_safe: false
role: barrier
scale: 2
alias: "Don't Touch Anything"
short_description: "A nanite-digested ruin inside the quarantine wall — pure tech, no Tao. A progress Limit tracks a fresh flare-up as the site keeps eating itself."
limits:
  - {name: navigate, tier: 4}
  - {name: flare-up, tier: 5}
default_tags: ["grey dust to the depth of a man", "lattice-eaten structures", "no Nearspace at all"]
default_statuses: ["contaminated-1"]
specials:
  - {name: "Weak Foundations", text: "Whenever someone (PC or Challenge) takes an action that could disturb the ruin's structure, this Challenge takes flare-up-1. An explosive or forceful action gives flare-up-3 instead (pattern per Crumbling Building, Core p. 310)."}
  - {name: "Pure Tech", text: "Nothing in this Challenge is Tao. It is not tagged [TAO-REINTERPRETED] anywhere and nothing here should be read as a Tao-dense site — see [[ferrante-basin]] and [[open-questions|OQ-15]], which this profile does not touch."}
threats:
  - threat: "Grey dust kicks up underfoot, fine as ash, and clings to everything."
    consequences:
      - {text: "contaminated advances a tier for anyone without sealed gear.", statuses: ["contaminated-1"], tags: []}
  - threat: "A patrol drone's rotors catch the light, pitted and streaked with rust."
    consequences:
      - {text: "Present a New Challenge: Surveillance Drone (generic reuse, [[generic-reuse-map]]) sweeps the area.", statuses: [], tags: []}
  - threat: "Something in the lattice-eaten structure groans and shifts underfoot."
    consequences:
      - {text: "Navigate carefully or take a fall (navigate Limit tested; failure gives buried-by-debris-3).", statuses: ["buried-by-debris-3"], tags: []}
      - {text: "flare-up advances a tier regardless.", statuses: [], tags: []}
  - threat: "The dust thickens and the silence gets total — no Nearspace here at all."
    consequences:
      - {text: "Comms and AR go dead; anyone relying on a signal takes cut-off-2.", statuses: ["cut-off-2"], tags: []}
  - threat: "flare-up maxes out at 5."
    consequences:
      - {text: "The site digests further: a section of structure gives way, the contaminated radius expands, and the navigate Limit resets at a harder tier for anyone still inside. This is a structural and environmental escalation only — nothing here transforms, infects, or produces a new Bloodware condition; what exposure over a long term might do is left open.", statuses: ["contaminated-2"], tags: ["the ground gave way"]}
power_sets: []
reuse_of: ""
---

# Nanite Hot Zone

**Role:** barrier · **Scale:** 2 (a wide contaminated ground, several blocks of ruin) · **Alias:** Don't Touch Anything · *A nanite-digested ruin inside the quarantine wall — pure tech, no Tao.*

The setting-specific hazard [[ferrante-basin]] promises but does not itself provide mechanics for: the Lace, the walled interior where Ferrante Nanoscale's campus stood before the outbreak (Bible §2). Written on the book's Hazard Zone / Crumbling Building pattern (Core p. 310) rather than as a Bloodware-adjacent Challenge — the outbreak's origin is canon (Bible §2), but the ruin itself is environmental and structural danger, not a vampire encounter. Nothing here places Bloodware inside the wall; the Basin district file is explicit that Bloodware are not *found* there, only *from* there.

## Limits

| Limit | Tier |
|---|---|
| navigate | 4 |
| flare-up (progress) | 5 |

## Tags & statuses

grey dust to the depth of a man, lattice-eaten structures, no Nearspace at all · *contaminated-1*

## Specials

**Weak Foundations:** Any structure-disturbing action gives `flare-up-1` (or `flare-up-3` if explosive/forceful) — the Crumbling Building pattern (Core p. 310), reused because the Lace is exactly that kind of ruin.

**Pure Tech:** Nothing here is Tao; not TAO-REINTERPRETED anywhere, and not a Tao-dense site — [[open-questions|OQ-15]] stays untouched by this file.

## Threats / Consequences

› Grey dust kicks up underfoot, fine as ash, and clings to everything.
» *contaminated* advances for anyone without sealed gear

› A patrol drone's rotors catch the light, pitted and streaked with rust.
» Present a New Challenge: Surveillance Drone ([[generic-reuse-map]])

› Something in the lattice-eaten structure groans and shifts underfoot.
» Navigate or fall (*buried-by-debris-3*)
» `flare-up` advances regardless

› The dust thickens and the silence gets total — no Nearspace here at all.
» Comms and AR go dead (*cut-off-2*)

› `flare-up` maxes out at 5.
» The site digests further (*contaminated-2*, *the ground gave way*) — structural and environmental escalation only.

## Power Sets

None.

## Canon and flags

- Bible §2: the Ferrante outbreak, roughly a century old, the source of Bloodware; Bible §3: what it produced is secret, the outbreak itself is public history ([[ferrante-basin]], BC-23).
- **[OPEN]** the final Consequence deliberately states that nothing here infects or transforms anyone — the vector by which Bloodware transmits is [[open-questions|OQ-4]], left open by the Bible, and this Challenge does not resolve it.
