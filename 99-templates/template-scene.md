---
# TEMPLATE — copy to 07-jobs/<nn-job>/scenes/, rename to <slug>.md, delete the `template` line and any comments you do not need.
template: true                   # marks this file as a template (BC-10); remove on instantiation
type: scene                      # fixed → Foundry JournalEntry page inside the job's entry (foundry-mapping §5)
name: "Placeholder Scene"        # display name; must equal the H1
slug: placeholder-scene          # file name without .md; kebab-case ASCII
status: review                   # draft | review | approved
source: custom                   # core | tokyo | custom
page: ""                         # book pages for any reused structure
owner: WP0                       # the work package that created the file
canon_refs: ["Brief §7.1", "Core p. 76–113"]   # Bible/Brief sections this file relies on
flags: []                        # RULES CONFLICT | BUILD CHOICE | TAO-REINTERPRETED | OPEN
player_safe: false                # vault-only (BC-128): true only if every line of the file can be shown to players; false if it carries an MC-only section, a twist, or supply-chain fact. WP8 builds the session-zero packet from this flag.
job: breakout                    # the job slug this scene belongs to (the job file <job-slug>.md, BC-125)
order: 1                         # position in the job's scene list
set_piece: "One line: the location and situation as a picture."
district: placeholder-district   # district slug; its story tag is listed below
story_tags: ["placeholder district story tag"]   # the district story tag in force, plus any scene tags the set piece creates
challenges: [placeholder-challenge]   # challenge slugs in play (custom or reuse-map entries by slug)
vectors_active: [placeholder-given-surname]   # npc slugs whose want/push is live here
core_moment: false               # true if this is one of the job's core moments
flashback_hooks: []              # Flashback slot prompts tied to "why we were here" — prompts only; player-authored content is never pre-written (Brief §7.1, OQ-12)
outcomes_to_next: ["What carries into the next scene, one line each."]
---

# Placeholder Scene

**Job:** [[breakout]] · **Order:** 1 · **District:** [[placeholder-district]] · **Story tag:** *placeholder district story tag* · **Core moment:** no

## Set piece

One paragraph: what the players see, hear, and are in the middle of.

## Challenges

- [[placeholder-challenge]] — role, one line.

## Vectors active

- [[placeholder-given-surname]] — want / push in this scene.

## Flashback slots

- Prompt only, e.g. "Where were you the night before the camp?" — no pre-written answer.

## What carries forward

- One line each.

## Canon and flags

- Markers as needed.
