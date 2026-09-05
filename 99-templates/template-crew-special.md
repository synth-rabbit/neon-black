---
# TEMPLATE — copy to 04-crew/crew-specials/, rename to <slug>.md, delete the `template` line and any comments you do not need.
template: true                   # marks this file as a template (BC-10); remove on instantiation
type: crew-special               # fixed → JournalEntry page; optionally also Foundry Item `improvement` (foundry-mapping §3.4)
name: "Placeholder Crew Special" # display name; must equal the H1
slug: placeholder-crew-special   # file name without .md; kebab-case ASCII
status: review                   # draft | review | approved
source: custom                   # core | tokyo | custom (core for the p. 155 list; tokyo for the p. 75 pattern)
page: ""                         # book page(s) when source is core/tokyo, e.g. "155" or "Tokyo 75"
owner: WP0                       # the work package that created the file
canon_refs: ["Brief §5.2", "Core p. 155", "Tokyo p. 75"]   # Bible/Brief sections this file relies on
flags: []                        # RULES CONFLICT | BUILD CHOICE | TAO-REINTERPRETED | OPEN
player_safe: true                # vault-only (BC-128): true only if every line of the file can be shown to players; false if it carries an MC-only section, a twist, or supply-chain fact. WP8 builds the session-zero packet from this flag.
prerequisite: "Placeholder condition the crew must have met."   # condition-gated, Tokyo p. 75 pattern; chosen as a crew theme upgrade
persists_through_theme_replacement: false   # crew Specials are upgrades on the crew theme; set true only if written as a card-level Special
tied_to: []                      # vault-only: slugs of the district, Key Player, or NPC the condition depends on (e.g., the fence)
# Optional Item conversion → Foundry `improvement`
improvement:
  name: "Placeholder Crew Special"
  description: "The rules text, as it appears on the card."
  effect_class: ""
  uses: 0                        # 0 = no use limit; otherwise the per-session / per-job count stated in the text
---

# Placeholder Crew Special

**Prerequisite:** Placeholder condition the crew must have met.

*The Special's rules text in one paragraph, in the Tokyo p. 75 register: what the crew gains, when, and any status or story tag it creates (statuses as `name-tier`).*

## Ties

- [[placeholder-slug]] — what in the Megacity this Special depends on.

## Canon and flags

- Markers as needed.
