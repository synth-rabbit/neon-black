---
# TEMPLATE — copy to 04-crew/crew-kits/, rename to <slug>.md, delete the `template` line and any comments you do not need.
template: true                   # marks this file as a template (BC-10); remove on instantiation
type: crew-kit                   # fixed → Foundry Item type `themekit` with the crew themebook
name: "Placeholder Crew Kit"     # display name; must equal the H1 → Foundry document `name`
slug: placeholder-crew-kit       # file name without .md; kebab-case ASCII
status: review                   # draft | review | approved
source: custom                   # core | tokyo | custom (core when recommending Found Family / Rebellious Street Gang / Wanted by reference)
page: ""                         # book page(s) when source is core/tokyo, e.g. "155–157"
owner: WP0                       # the work package that created the file
canon_refs: ["Bible §6", "Brief §5", "Core p. 154–157"]   # Bible/Brief sections this file relies on
flags: []                        # RULES CONFLICT | BUILD CHOICE | TAO-REINTERPRETED | OPEN
player_safe: true                # vault-only (BC-128): true only if every line of the file can be shown to players; false if it carries an MC-only section, a twist, or supply-chain fact. WP8 builds the session-zero packet from this flag.
themebook: "Crew (Otherscape)"   # the shipped crew themebook's name → `system.themebook_name` (id ayN2BXLJ2IgQyfh8 — foundry-mapping §3.1)
category: Crew-OS                # fixed → `system.subtype`
motivation_type: identity        # identity | ritual | itch → `system.motivation` (see foundry-mapping §3.2 on the crew card label)
motivation: "Placeholder crew statement."   # the kit's default statement; players may pick from candidate_motivations or write their own (Brief §5.2)
fade_type: decay                 # → `system.fade_type`
system_compatibility: otherscape # → `system.system_compatiblity`
nascent_ready: true              # vault-only: the kit reads as a theme with only tag A + one weakness (end of session one, Brief §5.1)
starting_three: [A, B, C]        # vault-only: the three power tags recommended as the starting set once the theme grows (Plan WP3 acceptance)
# Exactly ten power tags A–J (A is the title tag) → `system.power_tagstk[]`; answer the crew themebook questions (Core p. 155).
power_tags:
  - {letter: A, tagname: "placeholder title tag", description: "Answers crew question A: ..."}
  - {letter: B, tagname: "placeholder tag", description: "Answers crew question B: ..."}
  - {letter: C, tagname: "placeholder tag", description: "Answers crew question C: ..."}
  - {letter: D, tagname: "placeholder tag", description: "Answers crew question D: ..."}
  - {letter: E, tagname: "placeholder tag", description: "Answers crew question E: ..."}
  - {letter: F, tagname: "placeholder tag", description: "Answers crew question F: ..."}
  - {letter: G, tagname: "placeholder tag", description: "Answers crew question G: ..."}
  - {letter: H, tagname: "placeholder tag", description: "Answers crew question H: ..."}
  - {letter: I, tagname: "placeholder tag", description: "Answers crew question I: ..."}
  - {letter: J, tagname: "placeholder tag", description: "Answers crew question J: ..."}
# Exactly four weakness tags A–D → `system.weakness_tagstk[]`.
weakness_tags:
  - {letter: A, tagname: "placeholder weakness", description: "Answers crew weakness question A: ..."}
  - {letter: B, tagname: "placeholder weakness", description: "Answers crew weakness question B: ..."}
  - {letter: C, tagname: "placeholder weakness", description: "Answers crew weakness question C: ..."}
  - {letter: D, tagname: "placeholder weakness", description: "Answers crew weakness question D: ..."}
# Up to five Specials → `system.improvements[]`; leave empty and set use_themebook_improvements: true to inherit the five Crew Theme Specials — Huddle / Last Second Leap / Sacrifice / Strong Bonds / United By The Cause (Core p. 155).
improvements:
  - {letter: A, name: "", uses: 0, description: "", effect_class: ""}
  - {letter: B, name: "", uses: 0, description: "", effect_class: ""}
  - {letter: C, name: "", uses: 0, description: "", effect_class: ""}
  - {letter: D, name: "", uses: 0, description: "", effect_class: ""}
  - {letter: E, name: "", uses: 0, description: "", effect_class: ""}
use_themebook_improvements: true # → `system.use_tb_improvements`
# Prebuilt statements players may choose from (vault-only; ≥4 per kit, Plan WP3). Each carries a one-line "acting against it looks like" so Decay is adjudicable.
candidate_motivations:
  - {type: identity, statement: "Placeholder identity.", against: "What acting against it looks like."}
  - {type: ritual, statement: "Placeholder ritual as discipline, price, or condition.", against: "What neglecting it looks like."}
  - {type: itch, statement: "Placeholder itch to indulge.", against: "What resisting it looks like."}
  - {type: identity, statement: "Placeholder identity.", against: "What acting against it looks like."}
---

# Placeholder Crew Kit

**Themebook:** Crew · **Category:** Crew-OS

*One or two sentences on who this crew is, player-facing, in the voice of the book's crew kits (Core p. 156–157).*

## Power tags

| | Tag | Answers |
|---|---|---|
| **A** (title) | placeholder title tag | Crew question A: … |
| B ★ | placeholder tag | Crew question B: … |
| C ★ | placeholder tag | Crew question C: … |
| D | placeholder tag | … |
| E | placeholder tag | … |
| F | placeholder tag | … |
| G | placeholder tag | … |
| H | placeholder tag | … |
| I | placeholder tag | … |
| J | placeholder tag | … |

★ recommended starting three (with A).

## Weakness tags

| | Tag | Answers |
|---|---|---|
| A | placeholder weakness | … |
| B | placeholder weakness | … |
| C | placeholder weakness | … |
| D | placeholder weakness | … |

## Motivation

Default: **Identity** — *Placeholder crew statement.*

Prebuilt options (or write your own):

| Type | Statement | Acting against it looks like |
|---|---|---|
| Identity | … | … |
| Ritual | … | … |
| Itch | … | … |
| Identity | … | … |

## Nascent form (end of session one)

**placeholder title tag** + one weakness + one motivation.

## Canon and flags

- Markers as needed.
