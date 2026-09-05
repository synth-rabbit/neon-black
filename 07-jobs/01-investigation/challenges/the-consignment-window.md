---
type: challenge
name: "The Consignment Window"
slug: the-consignment-window
status: review
source: custom
page: "294–300, 297–298, 290"
owner: WP7b
canon_refs: ["Brief §7.3", "Brief §8", "Core p. 290", "Core p. 294–300", "Core p. 297", "Core p. 298"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: countdown
scale: 3
alias: "a date pencilled on a booking sheet"
short_description: "The Job's time-pressure vector: an assembled consignment, a booked haulier, and a delivery window nobody in the Job chose. It has a want and a push and no face."
limits:
  - {name: consignment-clears, tier: 5}
default_tags: ["four categories, nearly complete", "a haulier booked", "a window bought in advance"]
default_statuses: []
specials:
  - {name: "It Pushes By Continuing", text: "This is the book's stated exception to the rule that vectors have a face (Core p. 290): a force that is not a thinking agent but still wants something and spends something to get it. It wants the consignment closed and it spends the passage of time. It cannot be fought, negotiated with, or intimidated, and it has no Limit but its own progress."}
  - {name: "What Advances It", text: "Add one tier of consignment-clears for each of: a Downtime period the crew take; a scene that ends with no new lead; the first time in the Job that somebody who invoices the Factor is asked about him by name; a scene spent checking the shell company; a scene spent on the Hill. Add two tiers if the crew are cordoned, arrested, hospitalised, or otherwise removed from the street for a night."}
  - {name: "What Does Not", text: "Nothing the crew do to the Factor, his hires, his room or his door slows this Challenge. The order was placed by somebody else and the window was bought by somebody else. Killing the Factor advances it, because the haulier still comes."}
  - {name: "When It Maxes", text: "The consignment clears the bonded room and stops being one object anybody can find. The Job does not end: the paper-barn lead is still reachable through [[emeric-vann]], and [[investigation-09-what-the-book-cannot-say]] still happens. What is lost is proof — the ledger, shelf 388, and Tally's paper — and what is gained is a haulier's route, which is the only thing the crew get for having been slow. See [[investigation-aftermath]], 'If the run cleared.'"}
threats:
  - threat: "A stall-holder mentions, without being asked, that somebody came round buying the same sort of thing last week and paid better."
    consequences:
      - {text: "The order is nearly full and the street knows it before the crew do (add a tier to consignment-clears).", statuses: [], tags: []}
  - threat: "A haulier's booking is confirmed for a shuttered unit in the Stretch, and confirmed bookings are public paper."
    consequences:
      - {text: "Add a tier to consignment-clears, and the date is now knowable by anyone who asks a haulier (a date anybody can buy).", statuses: [], tags: ["a date anybody can buy"]}
  - threat: "The crew spend a night indoors — resting, healing, planning, or in somebody else's custody."
    consequences:
      - {text: "Add a tier (two if they did not choose it). Downtime is the most expensive thing in this Job.", statuses: [], tags: []}
  - threat: "consignment-clears maxes at 5."
    consequences:
      - {text: "The haulier comes and the consignment goes. The crew lose every physical proof they have not already taken; Tally's percentage stands and her paper does not come back (the crew take short-of-the-mark-3).", statuses: ["short-of-the-mark-3"], tags: []}
      - {text: "They get the route instead of the goods: a haulier, a plate, and a direction, which points behind the Hill. Escalate the Situation into [[investigation-09-what-the-book-cannot-say]].", statuses: [], tags: ["a haulier, a plate, and a direction"]}
power_sets: []
reuse_of: ""
---

# The Consignment Window

**Role:** countdown · **Scale:** 3 (an order, a room, a haulier and a window) · **Alias:** *a date pencilled on a booking sheet* · *Something that advances toward a crescendo* (Core p. 297).

The time-pressure vector for [[investigation]], written as a job-level Countdown Challenge — which is what WP7 packages are permitted to propose, as against series-level clocks, which are not (Brief §7.3; the one series-level Countdown remains [[secret-war-goes-public]]).

It is the consignment closing. Four categories, four hundred bundles, a haulier booked, and a delivery window that the Factor did not set and cannot move, because his principal set it and his principal pays in instruments that expire. Nobody in the Job is doing this on purpose to the crew. It is simply happening, at the speed of commerce, while they ask questions.

It starts at `consignment-clears-1` in [[investigation-01-the-counter-door]] and nobody in that scene knows it exists.

## Limits

| Limit | Tier |
|---|---|
| consignment clears (progress) | 5 |

## Tags & statuses

four categories, nearly complete · a haulier booked · a window bought in advance

## Specials

**It Pushes By Continuing:** the book's faceless vector (Core p. 290). No Limit but its own progress.

**What Advances It:** a Downtime (+1); a scene ending with no lead (+1); the first time somebody who invoices the Factor is asked about him by name (+1); a scene spent checking the shell (+1); a scene spent on the Hill (+1); a night off the street not of the crew's choosing (+2).

**What Does Not:** nothing done to the Factor, his hires, his room or his door. Killing him advances it.

**When It Maxes:** the consignment ships; the Job continues; the crew trade proof for a route.

## Threats / Consequences

› A stall-holder mentions, unasked, that somebody came round buying the same sort of thing last week and paid better.
» Add a tier

› A haulier's booking is confirmed for a shuttered unit in the Stretch, and confirmed bookings are public paper.
» Add a tier (*a date anybody can buy*)

› The crew spend a night indoors — resting, healing, planning, or in somebody else's custody.
» Add a tier; two if they did not choose it

› `consignment-clears` maxes at 5.
» The haulier comes and the consignment goes (*short-of-the-mark-3*)
» They get the route instead of the goods (*a haulier, a plate, and a direction*)

## Power Sets

None.

## Canon and flags

- Renamed by WP8 from *The Collection Run* (slug `the-collection-run`) so that it never shares a display name with Job 2's countdown [[collection-run]], which is the Repository's van; this one is the Factor's consignment (BC-171).

- Time-running-out vectors have a want and a push and no face: Core p. 290. Progress Limits and countdown Challenges: Core p. 297–298. Job-level Countdowns are permitted; series-level ones are not: Brief §7.3, [[spine-and-clock]].
- **[BUILD CHOICE]** the run, its advance triggers, and the trade of proof for a route on max; see [[build-choices]] "Added by WP7b".
- **[OPEN]** (OQ-37) the window belongs to the buyer and the buyer is not named by this Challenge maxing.
