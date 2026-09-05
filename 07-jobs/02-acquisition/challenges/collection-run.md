---
type: challenge
name: "The Collection Run"
slug: collection-run
status: review
source: custom
page: "294–300, 297–298"
owner: WP7c
canon_refs: ["Brief §7.3", "Brief §8", "Plan A.6", "Core p. 290", "Core p. 294–300"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: countdown
scale: 2
alias: "a van on a Thursday"
short_description: "The digitization contract: collect, scan, certify, pulp. Job-level countdown for the Acquisition. It is not protecting the volume — it is going to destroy it, on a schedule, with a completion bonus attached."
limits:
  - {name: collected, tier: 6}
default_tags: ["a booked scanning bay in the Lattice", "a completion bonus in the contract", "a pulper that runs on Thursdays", "a manifest with numbered certificates on it"]
default_statuses: ["on-schedule-2"]
specials:
  - {name: "Job-Level Only", text: "This is a countdown for one job (Brief §7.3; **[OPEN]** OQ-9). It is not a series clock, it does not persist past [[acquisition-aftermath]], and it must never be linked to [[secret-war-goes-public]] as an input. When the Acquisition ends, this Challenge is retired whatever tier it stands at."}
  - {name: "It Wants Nothing", text: "The time-pressure vector (Core p. 290). Nobody at the records contractor, the Chancery, or the scanning bay has an opinion about the crew or the volume. There is a schedule and a bonus for beating it. Every Threat here is a schedule advancing, never an antagonist acting, and this Challenge never Presents a foe by itself."}
  - {name: "Six Days, Then Fewer", text: "collected starts at 1 when the crew learn the schedule in [[acquisition-03-the-scan-index]] (nine days). It advances to 3 in [[acquisition-05-the-prep-sequence]] when the date is brought forward (six days) — automatically if the crew were noticed in the Domain, and on the contractor's own bonus if they were not. From [[acquisition-06-the-paper-barn]] onward it advances on Threats and on reading inside the bay ([[counterpart-stacks]] *An Hour You Did Not Budget For*)."}
  - {name: "Scanned Is Not Gone", text: "A volume that is collected and scanned before the crew reach it has not stopped existing: its pages are in a records Domain in Gallery Seven under Continuity's monitors ([[the-cold-suite]], [[the-lattice]]). Maxing this Challenge therefore does not end the job — it converts the Acquisition into a different job in a district the crew cannot rob quietly, and the aftermath treats that as a real outcome rather than a failure."}
threats:
  - threat: "The scanning crew make better progress than the schedule assumed; the gantry is one run further along than it was."
    consequences:
      - {text: "collected advances a tier.", statuses: [], tags: []}
  - threat: "A client manager somewhere asks a records contractor a question about service levels."
    consequences:
      - {text: "The collection date is brought forward a week; collected advances two tiers and the crew lose a week of planning (the date moved).", statuses: [], tags: ["the date moved"]}
      - {text: "Present a New Challenge: [[envelope-detail]], newly posted on the Repository's gate because somebody has started caring about the site.", statuses: [], tags: []}
  - threat: "The crew stand in the bay and read."
    consequences:
      - {text: "collected advances a tier per exchange, and a tier comes off [[counterpart-stacks]]'s leave-no-trace.", statuses: [], tags: []}
  - threat: "The manifest is checked against the cage and a certificate number does not match."
    consequences:
      - {text: "collected advances two tiers and the theft is now a dated, documented incident rather than an absence (an incident with a number on it).", statuses: [], tags: ["an incident with a number on it"]}
  - threat: "collected maxes out at 6."
    consequences:
      - {text: "The van comes, the run is loaded, the volume is scanned in a booked bay in the Lattice, the certificate is signed and the paper is pulped. The object the crew were hired to take no longer exists.", statuses: [], tags: ["the paper is gone"]}
      - {text: "Everything that was in it is now a scan set in a Chancery records Domain in Gallery Seven, behind Continuity's monitors. Present a New Challenge: [[the-cold-suite]] — and see *Scanned Is Not Gone*.", statuses: [], tags: ["only the scan set survives"]}
power_sets: []
reuse_of: ""
---

# The Collection Run

**Role:** countdown · **Scale:** 2 (a contract, a van, and a booked bay) · **Alias:** *a van on a Thursday* · *It is not guarding the volume. It is going to destroy it.*

The Chancery's counterpart set is being digitized for the first time in sixty years, under a records-retention contract with a completion bonus in it. Volumes go out of the Repository at [[kilbride-stretch]] by van on a weekly collection run; they are scanned in a booked bay in [[the-lattice]]; the scan set is certified against the shelf list; and the paper is pulped, because storing paper in the sprawl costs money and storing it nowhere costs none.

This is the job's time-pressure vector in the book's sense (Core p. 290): not a thinking agent, but a force with a want and a push. The want is *close the shelf-run.* The push is a van, a slot, a form, and a pulper that runs on Thursdays.

**Job-level only.** Brief §7.3 permits job-level Countdown Challenges and forbids new series-level ones (**[OPEN]** OQ-9). This clock is retired at [[acquisition-aftermath]] whatever tier it stands at, and never feeds [[secret-war-goes-public]].

## Limits

| Limit | Tier |
|---|---|
| collected (progress) | 6 |

There is no other Limit. The contract cannot be argued with, bought off at the crew's level, or shut down; a crew with the money and the standing to buy a records contractor is a crew that did not need to rob a warehouse.

## Tags & statuses

a booked scanning bay in the Lattice · a completion bonus in the contract · a pulper that runs on Thursdays · a manifest with numbered certificates on it · *on-schedule-2*

## Specials

**Job-Level Only:** retired at the aftermath; never an input to the series clock.

**It Wants Nothing:** every Threat is a schedule advancing, never an antagonist acting; it never Presents a foe by itself.

**Six Days, Then Fewer:** starts at 1 in [[acquisition-03-the-scan-index]]; 3 in [[acquisition-05-the-prep-sequence]]; advances on Threats and on reading in the bay thereafter.

**Scanned Is Not Gone:** maxing it converts the job rather than ending it — the pages survive as a scan set in a Domain behind Continuity's monitors.

## Threats / Consequences

› The gantry is one run further along than it was.
» `collected` advances

› A client manager asks a records contractor about service levels.
» The date moves forward a week (*the date moved*); `collected` advances two
» Present a New Challenge: [[envelope-detail]] on the gate

› The crew stand in the bay and read.
» `collected` advances per exchange; a tier off `leave no trace`

› The manifest is checked and a certificate number does not match.
» A dated, documented incident (*an incident with a number on it*); `collected` advances two

› `collected` maxes at 6.
» The paper is pulped (*the paper is gone*)
» Only the scan set survives, in Gallery Seven (*only the scan set survives*) — Present a New Challenge: [[the-cold-suite]]

## Power Sets

None.

## Canon and flags

- Time-pressure vectors have a want and a push and are not thinking agents: Core p. 290. Job-level countdowns permitted, series-level ones forbidden: Brief §7.3.
- **[BUILD CHOICE]** the digitization contract, the collection schedule, the completion bonus, and the pulping. Registered in [[build-choices]] "Added by WP7c".
- **[OPEN]** (OQ-9) job-level only; (OQ-17) nothing here says anything about Continuity beyond the fact that it monitors the ward its client's Domain sits in.
