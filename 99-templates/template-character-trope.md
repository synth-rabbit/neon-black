---
# TEMPLATE — copy to 02-splats/<splat>/tropes/, rename to <slug>.md, delete the `template` line and any comments you do not need.
template: true                   # marks this file as a template (BC-10); remove on instantiation
type: character-trope            # fixed → vault entity + Foundry JournalEntry page (no system data model; foundry-mapping §5)
name: "Placeholder Trope"        # display name; must equal the H1 → JournalEntry `name`
slug: placeholder-trope          # file name without .md; kebab-case ASCII
status: review                   # draft | review | approved
source: custom                   # core | tokyo | custom (core/tokyo only when reproducing a book trope by reference)
page: ""                         # book page(s) when source is core/tokyo, e.g. "178"
owner: WP0                       # the work package that created the file
canon_refs: ["Bible §2", "Brief §2.5(c)", "Brief §2.3"]   # Bible/Brief sections this file relies on
flags: []                        # RULES CONFLICT | BUILD CHOICE | TAO-REINTERPRETED | OPEN
player_safe: true                # vault-only (BC-128): true only if every line of the file can be shown to players; false if it carries an MC-only section, a twist, or supply-chain fact. WP8 builds the session-zero packet from this flag.
splat: hunter                    # vault-only: vampire | werewolf | mage | changeling | hunter
fixed_kits: [placeholder-kit-one, placeholder-kit-two, placeholder-kit-three]   # exactly three kit slugs inherent to the trope (Core p. 178); a vault kit is a bare slug and is wikilinked in the body; a printed book kit is `book:<slug>` (BC-126, see [[book-kits-index]]) and is cited by page, never linked
choice_kits: [placeholder-kit-four, placeholder-kit-five, placeholder-kit-six]  # exactly three theme-kit slugs the player picks the fourth theme from; none may share a theme type with the fixed three (Core p. 177)
loadout: "placeholder item (requires setup) with placeholder attachment; placeholder item (all: placeholder flaw)"   # the Loadout line in Core p. 178 format
essence_target: Real             # vault-only: the Essence the trope is built toward (hunters: Real or Cyborg — Brief §2.3)
---

# Placeholder Trope

**Splat:** hunter · **Built toward:** Real

*Two to four sentences in the voice of the book's trope blurbs (Core p. 178): who this is in the Megacity and what they do. Player-facing; no GM advice; no MC-only canon.*

## Theme kits

- [[placeholder-kit-one]] (THEMEBOOK)
- [[placeholder-kit-two]] (THEMEBOOK)
- [[placeholder-kit-three]] (THEMEBOOK)

**Choose one:**

- [[placeholder-kit-four]] (THEMEBOOK)
- [[placeholder-kit-five]] (THEMEBOOK)
- [[placeholder-kit-six]] (THEMEBOOK)

**Loadout:** placeholder item (requires setup) with placeholder attachment; placeholder item (all: placeholder flaw)

## On the sheet

Which Essence the four themes land on and the Essence minimum this trope satisfies (Brief §2.2, BC-1). For hunters: confirm no Augmentation theme except a replacement-framed one and no sculpting or bio-manipulation anywhere.

## Canon and flags

- Canon relied on: Bible §…, Brief §….
- Markers as needed.
