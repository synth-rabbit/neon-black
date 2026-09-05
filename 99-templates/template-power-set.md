---
# TEMPLATE — copy to 02-splats/<splat>/power-sets/ or 08-challenges/power-sets/, rename to <slug>.md, delete the `template` line and any comments you do not need.
template: true                   # marks this file as a template (BC-10); remove on instantiation
type: power-set                  # fixed → JournalEntry page + Foundry Actor `threat` with is_template: true (foundry-mapping §4.2)
name: "Placeholder Power Set"    # display name; must equal the H1
slug: placeholder-power-set      # file name without .md; kebab-case ASCII
status: review                   # draft | review | approved
source: custom                   # core | tokyo | custom (core when adapting Chromed Up, Shapechanger, Inhumanly Fast, Arcane, Corporate Sponsored, Connected & Protected — Core p. 326–333)
page: ""                         # book page(s) when source is core/tokyo, e.g. "332"
owner: WP0                       # the work package that created the file
canon_refs: ["Brief §8", "Core p. 326–333"]   # Bible/Brief sections this file relies on
flags: []                        # RULES CONFLICT | BUILD CHOICE | TAO-REINTERPRETED | OPEN (TAO-REINTERPRETED for any Mythos Power Set re-based on Tao)
player_safe: false                # vault-only (BC-128): true only if every line of the file can be shown to players; false if it carries an MC-only section, a twist, or supply-chain fact. WP8 builds the session-zero packet from this flag.
splat: werewolf                  # vault-only: vampire | werewolf | mage | changeling | hunter | none — the splat this overlay expresses
category: Noise                  # Self | Mythos | Noise — the book's Power Set grouping (Core p. 326, 330, 332)
applies_to: "Any Challenge representing a … (one line)."   # what kind of Challenge takes this overlay
default_tags: ["placeholder tag"]   # tags the overlay adds (inheritance through template_ids is unverified — foundry-mapping §8-4)
default_statuses: []             # statuses the overlay adds, `name-tier`
# Optional (BC-129): Limits the overlay adds to its host Challenge, in the `challenge` schema's shape — the book's own Power Sets do this (Lucky: out of luck 3; Spirit-Possessed: exorcise 3, banish 3 — Core p. 330–331). Splat overlays carry canon exposures here (Bloodware: EM + the Kernel). Omit or leave empty when none.
limits: []
#  - {name: em-field, tier: 3}
# Specials → gmmove subtype custom on the template threat.
specials:
  - {name: "Placeholder Special", text: "Rules text."}
# Threats (soft) with Consequences (hard), as in a Challenge profile.
threats:
  - threat: "The visible tell, one line."
    consequences:
      - {text: "What happens if unaddressed.", statuses: ["placeholder-3"], tags: []}
---

# Placeholder Power Set

**Applies to:** Any Challenge representing a … · **Category:** Noise · **Splat:** werewolf

## Tags & statuses

placeholder tag

## Specials

**Placeholder Special:** Rules text.

## Threats / Consequences

› The visible tell, one line.
» What happens if unaddressed (*placeholder-3*)

## Canon and flags

- Splat canon this overlay must obey (Plan A.6).
- Markers as needed.
