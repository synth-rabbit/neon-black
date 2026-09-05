---
# TEMPLATE — copy to 06-key-players/<kp-slug>/challenges/, 07-jobs/<job>/challenges/, or 08-challenges/custom/, rename to <slug>.md, delete the `template` line and any comments you do not need.
template: true                   # marks this file as a template (BC-10); remove on instantiation
type: challenge                  # fixed → Foundry Actor type `threat` with embedded spectrum / gmmove Items (foundry-mapping §4.1)
name: "Placeholder Challenge"    # display name; must equal the H1 → Actor `name`
slug: placeholder-challenge      # file name without .md; kebab-case ASCII
status: review                   # draft | review | approved
source: custom                   # core | tokyo | custom (core/tokyo when this is a re-flavored book Challenge — then also fill reuse_of)
page: ""                         # book page(s) when source is core/tokyo, e.g. "304"
owner: WP0                       # the work package that created the file
canon_refs: ["Brief §8", "Core p. 294–300"]   # Bible/Brief sections this file relies on
flags: []                        # RULES CONFLICT | BUILD CHOICE | TAO-REINTERPRETED | OPEN
player_safe: false                # vault-only (BC-128): true only if every line of the file can be shown to players; false if it carries an MC-only section, a twist, or supply-chain fact. WP8 builds the session-zero packet from this flag.
role: attacker                   # one of: asset | attacker | barrier | countdown | mystery | pursuer | target | temptation | watcher (Core p. 297); no Foundry field — goes in the description
scale: 1                         # → `system.collectiveSize` (Scale: 0 individual, 1 small group, … per Core p. 118–120)
alias: ""                        # → `system.alias` — what the PCs see before they know it; empty emits useAlias: false
short_description: "One line."   # → `system.short_description`
# Limits → embedded `spectrum` Items {name, maxTier}; tier 2–6; immune = 999 (renders as "-"). At least one.
limits:
  - {name: hurt-or-subdue, tier: 4}
  - {name: convince, tier: 3}
default_tags: ["placeholder tag", "placeholder tag"]   # → `system.defaultTags[]` as embedded tag objects (converter expands); only what is interesting (Plan A.6)
default_statuses: ["alert-2"]    # → `system.defaultStatuses[]` as embedded status objects; `name-tier`
# Specials → embedded `gmmove` Items, subtype custom.
specials:
  - {name: "Placeholder Special", text: "Rules text."}
# Threats (subtype soft) each with Consequences (subtype hard). Consequences are concrete: a status `name-tier`, a story tag, or "Present a New Challenge".
threats:
  - threat: "The visible tell, one line."
    consequences:
      - {text: "What happens if unaddressed.", statuses: ["gunshot-wound-2"], tags: []}
      - {text: "Another Consequence.", statuses: [], tags: ["placeholder story tag"]}
power_sets: []                   # power-set slugs applied as overlays → `system.template_ids[]`
reuse_of: ""                     # the core/tokyo Challenge this adapts, with page, e.g. "Corporate Security Guard, Core p. 304"
---

# Placeholder Challenge

**Role:** attacker · **Scale:** 1 · **Alias:** — · *One line.*

## Limits

| Limit | Tier |
|---|---|
| hurt or subdue | 4 |
| convince | 3 |

## Tags & statuses

placeholder tag, placeholder tag · *alert-2*

## Specials

**Placeholder Special:** Rules text.

## Threats / Consequences

› The visible tell, one line.
» What happens if unaddressed (*gunshot-wound-2*)
» Another Consequence (*placeholder story tag*)

## Power Sets

None — or [[placeholder-power-set]].

## Canon and flags

- Splat NPCs obey PC canon (Plan A.6): vampire EM + master node; hunter replacement-only cybernetics; changeling kill switch unless escaped.
- Markers as needed.
