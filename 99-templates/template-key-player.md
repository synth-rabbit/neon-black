---
# TEMPLATE — copy to 06-key-players/<kp-slug>/<kp-slug>.md (folder slug per BC-7; the file carries the folder's slug so [[<kp-slug>]] resolves — BC-125), delete the `template` line and any comments you do not need.
template: true                   # marks this file as a template (BC-10); remove on instantiation
type: key-player                 # fixed → Foundry JournalEntry page (foundry-mapping §5)
name: "Placeholder Key Player"   # display name from names.md; must equal the H1
slug: placeholder-key-player
status: review                   # draft | review | approved
source: custom                   # core | tokyo | custom
page: ""                         # book pages used for the template format, e.g. "283–284"
owner: WP0                       # the work package that created the file
canon_refs: ["Bible §3", "Bible §5", "Brief §6.4"]   # Bible/Brief sections this file relies on
flags: []                        # RULES CONFLICT | BUILD CHOICE | TAO-REINTERPRETED | OPEN
player_safe: false                # vault-only (BC-128): true only if every line of the file can be shown to players; false if it carries an MC-only section, a twist, or supply-chain fact. WP8 builds the session-zero packet from this flag.
kp_role: corp-a                  # corp-a | corp-b | corp-c | upstart | syndicate | government | tao-society | packs | changeling-cells (the folder slug, BC-7)
specialty: bio                   # vault-only, corps only: weapons | bio | cybernetics — must match names.md §3 (BC-8); empty for non-corps
base_concept: "One sentence in the book's Key Player template voice (Core p. 283)."
twist: "The twist, one or two sentences."   # Bible-given for the upstart (vampire-run); invented for the rest (Brief §6.4)
twist_source: invented           # bible | invented
agenda: "What this Key Player is trying to do this Series."
resources: ["placeholder resource", "placeholder resource"]     # people, money, gear, cyberspace Domains, territory (Core p. 283–284)
motifs: ["placeholder motif", "placeholder motif"]              # recurring images; also feed WP-I image briefs
key_characters: [placeholder-given-surname]                     # npc slugs in this folder's characters/
challenges: [placeholder-challenge]                             # challenge slugs in this folder's challenges/
territory: [placeholder-district]                               # district slugs (WP1) where this Key Player holds ground
vector_face: placeholder-given-surname                          # the npc slug of at least one vector face usable in the pilot jobs (Brief §6.4)
---

# Placeholder Key Player

**Role:** corp-a · **Specialty:** bio · **Territory:** [[placeholder-district]]

## Base concept

One paragraph (Core p. 283).

## Twist

**Source:** invented. One paragraph. Mark **[OPEN]** (OQ-n) where the twist touches an open question rather than answering it.

## Key characters

- [[placeholder-given-surname]] — vector face; one line (want / push in the npc file).

## Resources

- placeholder resource — one line each.

## Agenda

One paragraph: what they want this Series and what they will do to get it.

## Motifs

- placeholder motif — one line each.

## Standing toward the other Key Players

| Key Player | Standing (one line) |
|---|---|
| [[corp-a]] / [[corp-b]] / [[corp-c]] / [[upstart]] / [[syndicate]] / [[government]] / [[tao-society]] / [[packs]] / [[changeling-cells]] | … (this is the stalemate map; omit the row for self) |

## What the upstart's destabilization means here

One paragraph: the opportunity this Key Player smells (Bible §5).

## Challenges

- [[placeholder-challenge]] — signature foe.
- [[placeholder-challenge]] — signature hazard, system, or location.
- See [[placeholder-key-player-reuse]] (`challenges/<kp-slug>-reuse.md`, type index) for core/tokyo Challenges fielded.

## Membership

See [[placeholder-key-player-membership]] (`<kp-slug>-membership.md`, type membership; Tokyo pattern).

## Canon and flags

- Markers as needed.
