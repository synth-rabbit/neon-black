---
# TEMPLATE — copy to 02-splats/<splat>/pc-specials/, rename to <slug>.md, delete the `template` line and any comments you do not need.
template: true                   # marks this file as a template (BC-10); remove on instantiation
type: pc-special                 # fixed → JournalEntry page; optionally also Foundry Item `improvement` (foundry-mapping §3.4)
name: "Placeholder PC Special"   # display name; must equal the H1
slug: placeholder-pc-special     # file name without .md; kebab-case ASCII
status: review                   # draft | review | approved
source: custom                   # core | tokyo | custom (tokyo when adapting a Tokyo p. 72–74 Special)
page: ""                         # book page(s) when source is core/tokyo, e.g. "Tokyo 73"
owner: WP0                       # the work package that created the file
canon_refs: ["Bible §2", "Brief §2.4", "Tokyo p. 72–74"]   # Bible/Brief sections this file relies on
flags: []                        # RULES CONFLICT | BUILD CHOICE | TAO-REINTERPRETED | OPEN
player_safe: true                # vault-only (BC-128): true only if every line of the file can be shown to players; false if it carries an MC-only section, a twist, or supply-chain fact. WP8 builds the session-zero packet from this flag.
splat: vampire                   # vault-only: vampire | werewolf | mage | changeling | hunter | any
prerequisite: "Placeholder narrative condition the PC must have met."   # the Tokyo pattern: chosen instead of a theme upgrade only once this condition is true
persists_through_theme_replacement: true   # Megacity-style Specials live on the character card and survive theme Decay/replacement (Brief §2.4, CR-7, BC-3)
removal: "Removed only for narrative reasons; mark an Evolution point."  # the Tokyo p. 72 removal rule, restated per Special if it differs
# Optional Item conversion → Foundry `improvement` (foundry-mapping §3.4: `uses` becomes {current, max, expended} on emit)
improvement:
  name: "Placeholder PC Special"
  description: "The rules text, as it appears on the card."
  effect_class: ""
  uses: 0                        # 0 = no use limit; otherwise the per-session / per-job count stated in the text
---

# Placeholder PC Special

**Splat:** vampire · **Prerequisite:** Placeholder narrative condition the PC must have met.

*The Special's rules text in one paragraph, in the Tokyo p. 73 register: what the condition gives, what it costs, and any status or tag it creates (statuses as `name-tier`).*

## Persistence

Survives theme replacement (Brief §2.4). Removed only for narrative reasons; mark an Evolution point (Tokyo p. 72).

## Canon and flags

- The persistent condition this carries (e.g., EM vulnerability, master node, trigger dependency, kill switch, society oath, replacement prosthetic) and the Bible section that makes it inescapable.
- Markers as needed.
