---
# TEMPLATE — copy to 02-splats/<splat>/theme-kits/ or 03-self-kits/, rename to <slug>.md, delete the `template` line and any comments you do not need.
template: true                   # marks this file as a template (BC-10); remove on instantiation
type: theme-kit                  # fixed → Foundry Item type `themekit`
name: "Placeholder Theme Kit"    # display name; must equal the H1 → Foundry document `name`
slug: placeholder-theme-kit      # file name without .md; kebab-case ASCII; never changes after WP6
status: review                   # draft | review | approved — vault-only; WP9 converts review/approved only
source: custom                   # core | tokyo | custom → `system.sourceBook` ("OtherscapeCore" when core, else "")
page: ""                         # book page(s) when source is core/tokyo, e.g. "243"; cited in the description HTML
owner: WP0                       # the work package that created the file (replace with yours)
canon_refs: ["Bible §2", "Brief §2.5", "Plan A.5"]   # Bible/Brief sections this file relies on
flags: []                        # RULES CONFLICT | BUILD CHOICE | TAO-REINTERPRETED | OPEN — each must also appear inline with a register id
player_safe: true                # vault-only (BC-128): true only if every line of the file can be shown to players; false if it carries an MC-only section, a twist, or supply-chain fact. WP8 builds the session-zero packet from this flag.
themebook: Augmentation          # one of the 14 shipped themebooks (Affiliation, Assets, Expertise, Horizon, Personality, Troubled Past, Artifact, Companion, Esoterica, Exposure, Augmentation, Cutting Edge, Cyberspace, Drones) → `system.themebook_name`
category: Noise                  # Self | Noise | Mythos-OS → `system.subtype` (see foundry-mapping §3.1 on Mythos-OS vs Mythos)
motivation_type: itch            # identity (Self) | ritual (Mythos) | itch (Noise) → `system.motivation`
motivation: "Placeholder itch statement in the kit's voice."   # kit-fixed statement; rendered into `system.description`; voice rules in style-guide §3
fade_type: decay                 # → `system.fade_type` (Otherscape term; shipped themebooks carry "fade" — foundry-mapping §3.1)
system_compatibility: otherscape # → `system.system_compatiblity` (repo spelling; value verified from otherscape.ts)
splat: vampire                   # vault-only: vampire | werewolf | mage | changeling | hunter | any (Self kits that any splat may take)
# Exactly ten power tags, letters A–J; A is the title tag → `system.power_tagstk[]` {letter, tagname, description}.
# `description` cites the themebook question the tag answers (Plan A.5). Tag voice: style-guide §2.
power_tags:
  - {letter: A, tagname: "placeholder title tag", description: "Answers question A: ..."}
  - {letter: B, tagname: "placeholder tag", description: "Answers question B: ..."}
  - {letter: C, tagname: "placeholder tag", description: "Answers question C: ..."}
  - {letter: D, tagname: "placeholder tag", description: "Answers question D: ..."}
  - {letter: E, tagname: "placeholder tag", description: "Answers question E: ..."}
  - {letter: F, tagname: "placeholder tag", description: "Answers question F: ..."}
  - {letter: G, tagname: "placeholder tag", description: "Answers question G: ..."}
  - {letter: H, tagname: "placeholder tag", description: "Answers question H: ..."}
  - {letter: I, tagname: "placeholder tag", description: "Answers question I: ..."}
  - {letter: J, tagname: "placeholder tag", description: "Answers question J: ..."}
# Exactly four weakness tags, letters A–D → `system.weakness_tagstk[]`.
weakness_tags:
  - {letter: A, tagname: "placeholder weakness", description: "Answers weakness question A: ..."}
  - {letter: B, tagname: "placeholder weakness", description: "Answers weakness question B: ..."}
  - {letter: C, tagname: "placeholder weakness", description: "Answers weakness question C: ..."}
  - {letter: D, tagname: "placeholder weakness", description: "Answers weakness question D: ..."}
# Up to five Specials this kit may use → `system.improvements[]` {name, uses, description, effect_class} (no `letter` on emit — foundry-mapping §3.1).
# Leave all names empty and set use_themebook_improvements: true to inherit the themebook's five.
improvements:
  - {letter: A, name: "", uses: 0, description: "", effect_class: ""}
  - {letter: B, name: "", uses: 0, description: "", effect_class: ""}
  - {letter: C, name: "", uses: 0, description: "", effect_class: ""}
  - {letter: D, name: "", uses: 0, description: "", effect_class: ""}
  - {letter: E, name: "", uses: 0, description: "", effect_class: ""}
use_themebook_improvements: true # → `system.use_tb_improvements`
---

# Placeholder Theme Kit

**Themebook:** Augmentation · **Category:** Noise · **Splat:** vampire · **Source:** custom

*One or two sentences saying what this theme is, in the voice of the book's kit blurbs. No GM advice.*

## Power tags

| | Tag | Answers |
|---|---|---|
| **A** (title) | placeholder title tag | Question A: … |
| B | placeholder tag | Question B: … |
| C | placeholder tag | Question C: … |
| D | placeholder tag | Question D: … |
| E | placeholder tag | Question E: … |
| F | placeholder tag | Question F: … |
| G | placeholder tag | Question G: … |
| H | placeholder tag | Question H: … |
| I | placeholder tag | Question I: … |
| J | placeholder tag | Question J: … |

## Weakness tags

| | Tag | Answers |
|---|---|---|
| A | placeholder weakness | Weakness question A: … |
| B | placeholder weakness | Weakness question B: … |
| C | placeholder weakness | Weakness question C: … |
| D | placeholder weakness | Weakness question D: … |

## Itch

> Placeholder itch statement in the kit's voice.

## Specials

Inherits the themebook's five (Core p. NNN), or list the kit's own here.

## Nascent form

Title tag **placeholder title tag** + one weakness — one line confirming the theme still reads as a theme (Plan A.5).

## Canon and flags

- Canon relied on: Bible §…, Brief §….
- Rarity note: how this kit avoids implying the splat is common.
- Markers: **[TAO-REINTERPRETED]** / **[RULES CONFLICT]** (CR-n) / **[BUILD CHOICE]** (BC-n) / **[OPEN]** (OQ-n) as needed.
