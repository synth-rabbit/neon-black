---
# TEMPLATE — copy to 09-loadout/, rename to <slug>.md, delete the `template` line and any comments you do not need.
template: true                   # marks this file as a template (BC-10); remove on instantiation
type: loadout-item               # fixed → Foundry Item type `tag` with subtype loadout, one Item per tag (foundry-mapping §3.3)
name: "Placeholder Item"         # display name; must equal the H1 → Item `name`
slug: placeholder-item           # file name without .md; kebab-case ASCII
status: review                   # draft | review | approved
source: custom                   # core | tokyo | custom (core/tokyo when pointing at a Street Catalog entry by reference)
page: ""                         # book page(s) when source is core/tokyo, e.g. "269"
owner: WP0                       # the work package that created the file
canon_refs: ["Brief §9.1(g)", "Core p. 114–117", "Core p. 252–271"]   # Bible/Brief sections this file relies on
flags: []                        # RULES CONFLICT | BUILD CHOICE | TAO-REINTERPRETED | OPEN (TAO-REINTERPRETED for every tao-touched item)
player_safe: false                # vault-only (BC-128): true only if every line of the file can be shown to players; false if it carries an MC-only section, a twist, or supply-chain fact. WP8 builds the session-zero packet from this flag.
catalog: weapons                 # weapons | armor | ammo | apps | attachments | cyberspace | drones | enhancers | garments | merc-gear | tao-touched | vehicles (Core p. 252–271; "Source-Touched Items" renamed)
tags: ["placeholder loadout tag"]   # the loadout tag(s) the item grants, tag voice per style-guide §2; one `tag` Item each on emit
flaws: ["placeholder flaw"]      # the item's flaws in the Street Catalog pattern (e.g., short ranged, incriminating, requires setup); every item has ≥1 flaw or requires_setup (Plan WP5)
requires_setup: false            # true if the item needs a preparatory action before its tag can be used (Core p. 178 Loadout line convention)
key_player: ""                   # vault-only: Key Player folder slug whose branding or supply this item carries, or empty
availability: "One line: corporate | black market | DIY | camp-issue — and who sells it (Bible §1 'who owns the tech')."
---

# Placeholder Item

**Catalog:** weapons · **Tags:** *placeholder loadout tag* · **Flaws:** *placeholder flaw* · **Requires setup:** no

## Description

One paragraph in the Street Catalog voice (Core p. 252–271): what it is, what it looks like, what it does in play.

## Availability

One line.

## Canon and flags

- Markers as needed (e.g., anti-nanite gear cites Bible §2 vampire weaknesses; tao-touched items carry **[TAO-REINTERPRETED]**).
