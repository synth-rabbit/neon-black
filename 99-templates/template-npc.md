---
# TEMPLATE — copy to 06-key-players/<kp-slug>/characters/ (or the folder WP1 assigns), rename to <given-surname>.md, delete the `template` line and any comments you do not need.
template: true                   # marks this file as a template (BC-10); remove on instantiation
type: npc                        # fixed → Foundry JournalEntry page; a separate `challenge` file exists if they fight (foundry-mapping §5)
name: "Placeholder Given Surname"   # display name; must equal the H1; the handle goes in `handle`, never in the slug (style-guide §9)
slug: placeholder-given-surname  # file name without .md; given-surname
status: review                   # draft | review | approved
source: custom                   # core | tokyo | custom
page: ""                         # book page(s) if adapted from a book NPC
owner: WP0                       # the work package that created the file
canon_refs: ["Bible §5", "Brief §6.4", "Core p. 290"]   # Bible/Brief sections this file relies on
flags: []                        # RULES CONFLICT | BUILD CHOICE | TAO-REINTERPRETED | OPEN
handle: ""                       # street name in quotes if the street uses one, e.g. "Tally"
affiliation: [corp-a]            # Key Player folder slugs (BC-7) this person belongs to or serves
splat: none                      # vampire | werewolf | mage | changeling | hunter | none — MC-only fact; obeys the same canon as PCs (Plan A.6)
role_in_pilot: "One line: where this person appears in the pilot jobs."
# Vector (Core p. 290): what they want from the PCs and how they push. Required for a vector face.
vector:
  want: "What they want."
  push: "How they push the PCs toward it."
challenge: null                  # slug of this person's `challenge` file, or null if they never need a profile
player_safe: false               # vault-only: true only if every line below can be shown to players (most npc files are MC-only)
---

# Placeholder Given Surname

**Handle:** — · **Affiliation:** [[corp-a]] · **Role in the pilot:** One line.

## Who they are

One or two paragraphs in the book's NPC register (Core p. 55–59 for voice). Everything a scene needs to play them: look, manner, what they carry, where they are found.

## Vector

- **Want:** What they want.
- **Push:** How they push.

## What the crew knows / does not know

Two lines. For the crew leader, this section records only what the Bible states and nothing about their motives beyond it (Plan WP4).

## Challenge

[[placeholder-challenge]] — or "none."

## Canon and flags

- Markers as needed; **[OPEN]** (OQ-n) for any fact the Bible leaves open about this person.
