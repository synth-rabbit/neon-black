---
# TEMPLATE — copy to 05-megacity/districts/, rename to <slug>.md, delete the `template` line and any comments you do not need.
template: true                   # marks this file as a template (BC-10); remove on instantiation
type: district                   # fixed → Foundry JournalEntry page (foundry-mapping §5)
name: "Placeholder District"     # display name; must equal the H1
slug: placeholder-district       # file name without .md; kebab-case ASCII
status: review                   # draft | review | approved
source: custom                   # core | tokyo | custom (custom: Generator-derived content is authorized invention, Plan A.1 rule 5)
page: ""                         # Generator pages used, e.g. "162–171"
owner: WP0                       # the work package that created the file
canon_refs: ["Bible §3", "Brief §6.2", "Core p. 160–172"]   # Bible/Brief sections this file relies on
flags: []                        # RULES CONFLICT | BUILD CHOICE | TAO-REINTERPRETED | OPEN (TAO-REINTERPRETED whenever a Mythoi-pillar result is restated)
player_safe: false                # vault-only (BC-128): true only if every line of the file can be shown to players; false if it carries an MC-only section, a twist, or supply-chain fact. WP8 builds the session-zero packet from this flag.
zone_code: "11-13"               # d66 rows of the District Directory this district covers (Core p. 162)
central_concept: "One sentence: what this district is."   # the Generator's central concept
story_tag: "placeholder district story tag"   # the district story tag: usable once, expires, restored after downtime (Core p. 150); tag voice per style-guide §2
pillar: "Oligarchic Corruption"  # the dominant pillar (Transhumanism | Oligarchic Corruption | Gangs, Cults & Counterculture | Technological Overdrive | Sprawling Cyberspace | Cities in Ruins | Tao Weaponized)
# Developments rolled or chosen until the district has at least one (Core p. 163 ff.). Mythoi-pillar results are restated as Tao and marked.
developments:
  - {order: 1, pillar: "Oligarchic Corruption", subtheme: "placeholder subtheme", summary: "One line."}
key_players_present: [corp-c, packs]   # Key Player folder slugs (BC-7) that hold ground here
caste_band: Patched              # Sculpted | Fitted | Patched | Stock (street slang only, BC-9) — or "mixed"
mandatory_placement: ""          # vault-only: which Plan WP1 mandatory placement this district satisfies (work camp, HQ, upstart, fence's turf, pack turf, Tao front, escapee refuge, caste gradient), or empty
---

# Placeholder District

**Zone:** 11-13 · **Pillar:** Oligarchic Corruption · **Caste band:** Patched · **Story tag:** *placeholder district story tag*

## Central concept

One paragraph. What the district is, what it looks like, who lives there — in the tone words of [[style-guide]] §4.

## Developments

1. **Placeholder subtheme** (Oligarchic Corruption) — one paragraph. Mark **[TAO-REINTERPRETED]** where a Mythoi result was restated.

## Who holds ground here

- [[corp-c]] — one line.
- [[packs]] — one line.

## Places

- **Placeholder place** — one line each; anything a scene can be set in.

## Canon and flags

- Markers as needed.
