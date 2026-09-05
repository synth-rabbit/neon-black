---
# TEMPLATE — copy to 07-jobs/<nn-job>/<job-slug>.md (e.g. 07-jobs/00-breakout/breakout.md; file names are unique vault-wide — BC-125), delete the `template` line and any comments you do not need.
template: true                   # marks this file as a template (BC-10); remove on instantiation
type: job                        # fixed → Foundry JournalEntry (one entry per job; scenes as pages) (foundry-mapping §5)
name: "Placeholder Job"          # display name; must equal the H1
slug: placeholder-job
status: review                   # draft | review | approved
source: custom                   # core | tokyo | custom (the starter job is a structural reference only — Brief §7.1)
page: ""                         # book pages used for structure, e.g. "284–293"
owner: WP0                       # the work package that created the file
canon_refs: ["Bible §5", "Bible §6", "Brief §7"]   # Bible/Brief sections this file relies on
flags: []                        # RULES CONFLICT | BUILD CHOICE | TAO-REINTERPRETED | OPEN
player_safe: false                # vault-only (BC-128): true only if every line of the file can be shown to players; false if it carries an MC-only section, a twist, or supply-chain fact. WP8 builds the session-zero packet from this flag.
job_type: [investigation]        # one or more of the book's job types (Core p. 285–287): acquisition | investigation | extraction | breakout | … (never exorcism / ritual performance / source-hunting in the pilot, Brief §7.2)
sessions: 2                      # expected session count (the four-act starter job is the scale reference)
series_pole: paycheck            # paycheck | misfits | pivot (Brief §1.2)
hooks: ["How the crew is offered the job, one line each."]   # hired through the fence or the fence's network for Jobs 1 and 2
goal: "What the crew is hired to accomplish, one sentence."
vectors: [placeholder-given-surname]      # npc slugs with want/push active in this job (vectors.md in the folder holds the detail)
core_moments: [placeholder-scene]         # scene slugs flagged core_moment: true
scenes: [placeholder-scene]               # scene slugs in order
climax: placeholder-scene                 # the climax scene slug
aftermath: placeholder-job-aftermath      # the aftermath file in this folder (<job-slug>-aftermath.md)
twist_for_pivot: false                    # true on the job that carries the Paycheck→Misfits twist (Brief §1.2, §7.2)
key_players_touched: [corp-c, upstart]    # Key Player folder slugs the job touches (Investigation: ≥2; Plan WP7b)
districts_touched: [placeholder-district] # district slugs (Investigation: ≥3)
complications: ["From the book's job-type list, one line each (Core p. 285–287)."]
---

# Placeholder Job

**Type:** investigation · **Sessions:** 2 · **Pole:** paycheck · **Pivot twist:** no

## Hooks

- How the crew is offered the job.

## Goal

One sentence.

## Structure

1. [[placeholder-scene]] — one line.
2. … → climax: [[placeholder-scene]] → [[placeholder-job-aftermath]].

## Vectors

See [[placeholder-job-vectors]] (`<job-slug>-vectors.md`) in this folder: [[placeholder-given-surname]] (want / push).

## Ties to PC themes

One line per splat: the Identity / Ritual / Itch the job presses (Plan WP7b).

## Complications

- From the job-type list.

## Key Players and districts

[[corp-c]], [[upstart]] · [[placeholder-district]]

## Canon and flags

- Markers as needed; the crew leader's motives stay unrevealed beyond canon (OQ-10).
