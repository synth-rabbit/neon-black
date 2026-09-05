---
type: challenge
name: "The Secret War Goes Public"
slug: secret-war-goes-public
status: review
source: custom
page: "297–300, 118"
owner: WP1
canon_refs: ["Bible §2 hunter public role", "Bible §3 Masquerade", "Bible §3 power structure", "Bible §5 the clock", "Brief §4.1", "Brief §7.3", "Brief §11.5", "Core p. 297–300", "Core p. 118–120"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: countdown
scale: 4
alias: "Rumors on the Wall"
short_description: "The Big Three and Continuity are already at war; Palisade has not noticed yet. Series-level Countdown, progress Limit public-war at tier 6."
limits:
  - {name: public-war, tier: 6}
default_tags: ["civil agreements nominally in force", "the Noise absorbs incidents", "Baselines take the blame"]
default_statuses: ["deniable-3"]
specials:
  - {name: "Series-Level", text: "This Challenge is always in play, in every scene of the Series, in the background. Its statuses never expire at the end of a scene and are never restored by downtime. Only the Consequences below and the aftermath sections of jobs (WP7) add tiers to public-war; the crew cannot raise or lower it with a single roll."}
  - {name: "The Noise Absorbs", text: "Tiers accrue to public-war only from events that are public and witnessed — on the feeds, in front of a crowd, in a district where people talk. Private violence, however extreme, adds nothing (Brief §4.1). When a Threat below is voiced in a place with no witnesses, it produces its story tags but not its public-war tier."}
  - {name: "Cleanup Crews", text: "Once between any two jobs, a corporation may remove one tier from public-war by producing a Baseline to blame for the most recent incident (Bible §2 hunter). The Baseline must be a real person; the corp names them on the feeds. If the crew supplied the name, they earned a favor. If the crew contains a Baseline, they are a candidate. Cleanup cannot reduce public-war below the tier at which the last job ended, and it stops working entirely at public-war-5."}
  - {name: "Everyone Smells Opportunity", text: "Each time public-war reaches a new tier, one Key Player acts on the opening (Bible §5). The act is voiced as a street-level tell from the table in this file's notch guide, and it is a Threat the crew can respond to in the next scene set in that Key Player's territory."}
threats:
  - threat: "A job ends with something left behind that no Baseline could have done — a body drained to the iron, a door torn off its rails, a face that was somebody else's yesterday — and the feeds got there before cleanup."
    consequences:
      - {text: "The corporate war shows through the cover story. Add public-war-1 (public-war-2 if the incident is in a Big Three HQ district or on the Crest).", statuses: ["public-war-1"], tags: []}
      - {text: "Cleanup names a Baseline anyway. The named person becomes a story tag in that district for the next job.", statuses: [], tags: ["a Baseline was blamed"]}
  - threat: "Two sets of corporate security, or corp security and a Continuity crisis-response team, arrive at the same incident and draw on each other in front of a crowd."
    consequences:
      - {text: "Open combat between corporate forces in public. Add public-war-2. The district's tier lifts lock down for the rest of the job.", statuses: ["public-war-2"], tags: ["tier lifts locked down"]}
      - {text: "Present a New Challenge: a corporate security element or a Continuity response team (generic reuse, WP5) that treats the crew as the third side.", statuses: [], tags: []}
  - threat: "A Chancery spokesman is put in front of a camera and asked, in so many words, whether the corporations are at war."
    consequences:
      - {text: "The government denies it, badly. Add public-war-1 and the city stops believing what the Chancery says for the rest of the Series.", statuses: ["public-war-1"], tags: ["the Chancery is not believed"]}
      - {text: "The government names it — an emergency, a curfew, a request for corporate 'assistance.' Add public-war-2; corporate security now operates as police openly in the named districts.", statuses: ["public-war-2"], tags: ["corp security is the police here"]}
  - threat: "One of the Big Three publicly withdraws from, or publicly accuses another of breaking, one of the civil agreements — a supply compact, a no-poaching clause, a territorial line under the Wall."
    consequences:
      - {text: "The stalemate cracks in the open. Add public-war-2 and remove the tag civil agreements nominally in force.", statuses: ["public-war-2"], tags: []}
      - {text: "Prices double in the Gullet and the Almoners raise the cost of Leash; the Run gets restless.", statuses: [], tags: ["prices doubled under the Wall", "the Run is restless"]}
  - threat: "A Big Three HQ district, or the Lattice, is struck — visibly, from outside, by something that is not a Baseline with a gun."
    consequences:
      - {text: "Add public-war-3. Every corporation goes to open security posture: checkpoints at every tier lift, drones over the Face, Continuity teams 'deployed for public safety' wherever a corp will pay for them.", statuses: ["public-war-3"], tags: ["checkpoints at every lift", "drones over the Face"]}
  - threat: "public-war reaches 6."
    consequences:
      - {text: "The war is public. See 'When it maxes' below. This Challenge is then retired and replaced by whatever the Key Players do next (WP4 agendas; a successor Countdown is the GM's to authorize — Brief §7.3, OQ-9).", statuses: [], tags: ["the war is public"]}
power_sets: []
reuse_of: ""
---

# The Secret War Goes Public

**Role:** countdown · **Scale:** 4 (Megacity-wide; the table's largest listed rank, Core p. 118) · **Alias:** Rumors on the Wall · *The Big Three and Continuity are already at war; Palisade has not noticed yet.*

The one clock the Bible confirms (§5): "the conflict between the Big Three and the upstart escalates until the public knows there is a war going on rather than a secret one." **[BUILD CHOICE]** (BC-5, interviewer's choice) It is written as a series-level Countdown Challenge with a single progress Limit at tier 6 — the hardest the book allows, "incredibly difficult" (Core p. 298) — advanced by job aftermaths and by the Consequences below (Brief §7.3). Its context and the kinds of events that move it are in [[spine-and-clock]]; the Masquerade model it strains against is in [[palisade|Palisade]] (Brief §4.1).

## Limits

| Limit | Tier |
|---|---|
| public-war (progress) | 6 |

There is no other Limit. The Challenge cannot be *overcome* — the war is real (Bible §5); it can only be delayed, and only by cleanup (see Specials). Anything else is immune ("–").

## Tags & statuses

civil agreements nominally in force, the Noise absorbs incidents, Baselines take the blame · *deniable-3*

*deniable-3* is what the corporations start with: three tiers of plausible denial that the Noise and the cover story give them for free. It is not a Limit. It is the reason `public-war` is hard to move, and it erodes as the tags above are removed by Consequences.

## Specials

**Series-Level:** Always in play, in the background of every scene. Its statuses never expire and are never restored by downtime. Only the Consequences here and the aftermath sections of jobs (WP7) add tiers; no single roll raises or lowers it.

**The Noise Absorbs:** Tiers accrue only from public, witnessed events. Private violence adds nothing (Brief §4.1). A Threat voiced without witnesses yields its story tags, not its tier.

**Cleanup Crews:** Once between any two jobs, a corporation may remove one tier by producing a real Baseline to blame on the feeds (Bible §2 hunter). Cleanup cannot reduce `public-war` below the tier at which the last job ended, and stops working at `public-war-5`.

**Everyone Smells Opportunity:** Each new tier, one Key Player acts on the opening (Bible §5), voiced through the notch guide below and presented as a Threat in that Key Player's territory next scene.

## Threats / Consequences

› A job ends with something left behind that no Baseline could have done, and the feeds got there before cleanup.
» The corporate war shows through (*public-war-1*; *public-war-2* in a Big Three HQ district or on the Crest)
» Cleanup names a Baseline anyway (*a Baseline was blamed*, a story tag in that district next job)

› Two corporate forces — or corp security and a Continuity crisis-response team — draw on each other in front of a crowd.
» Open combat in public (*public-war-2*; *tier lifts locked down* for the job)
» Present a New Challenge: a security element treating the crew as the third side (generic reuse, WP5)

› A Chancery spokesman is asked on camera whether the corporations are at war.
» Denied, badly (*public-war-1*; *the Chancery is not believed*)
» Named — emergency, curfew, corporate "assistance" (*public-war-2*; *corp security is the police here*)

› One of the Big Three publicly withdraws from, or accuses another of breaking, a civil agreement.
» The stalemate cracks in the open (*public-war-2*; remove *civil agreements nominally in force*)
» Prices double, Leash costs more, the Run gets restless (*prices doubled under the Wall*, *the Run is restless*)

› A Big Three HQ district, or the Lattice, is struck visibly from outside by something that is not a Baseline with a gun.
» Open security posture everywhere (*public-war-3*; *checkpoints at every lift*, *drones over the Face*)

› `public-war` reaches 6.
» The war is public (*the war is public*). Retire this Challenge.

## The notch guide — what Palisade looks like at each tier

Each tier is a change the crew can *see* on the street. The MC voices these as Threats from the Key Players in their own districts (`05-megacity/districts/`); none of them is a scripted event.

| public-war | The street-level tell | Which Key Players move |
|---|---|---|
| **0** | Rumor. The stalemate is intact as far as anyone can see. Corp security polices; the Chancery collects; the Ledger is a secret. | Continuity is already moving; nobody else knows to. |
| **1** | Extra corporate security on the Face tiers. A press release blames "another Baseline with a gun." Tally's prices tick up. | The Almoners stock up. Baselines get looked at harder on the Foot. |
| **2** | Checkpoints at some tier lifts. A joint Chancery statement nobody asked for. Continuity crisis-response vans parked where they were not before. | AP&I quietly recounts what it lost at the Ledger. Orison sells to everyone. |
| **3** | Corp security seen in open combat somewhere under the Wall; the footage lasts an hour before it is scrubbed. "Baseline" starts to be a joke on the feeds. | The Run tests a corp-owned block. The Wuji move an asset they had left in the open. |
| **4** | One of the Big Three publicly withdraws from a civil agreement. Continuity teams "deployed for public safety" in a Patched district at a corp's expense. The Cutloose vanish deeper. | The Chancery takes a fourth bidder. The Almoners sell Leash to a corporate buyer. |
| **5** | An HQ district or the Lattice is struck. Emergency declared; corp security *is* the police in named districts; drones over the Face day and night. Cleanup can no longer keep up. | Everyone. |
| **6** | **The war is public.** | See below. |

## When it maxes — what becomes true in Palisade

Stated inside canon; nothing here reveals what the Bible keeps secret.

1. **Everyone in Palisade knows the Big Three and Continuity are at war.** It is on the feeds, in the Chancery's statements, in the price of bread under the Wall. The civil agreements are dead; nobody pretends otherwise.
2. **Corporate security is openly at war on the streets.** It was always exactly as legal as the police (Bible §3); now it acts like an army and the police get out of its way. The Chancery is openly whichever corporation's client it was quietly.
3. **The Masquerade stops holding for the corporate war** — and *only* for the corporate war (Brief §4.1). Incidents caused by corporate forces are no longer blamed on Baselines; the public knows corp security did it, and says so.
4. **The Masquerade for the secret splats holds.** Bloodware, Howlers, the Wuji, and the Cutloose remain secret (Bible §3). The cover story changes shape: what was blamed on Baselines is now blamed on *the war* — a Howler frenzy is "a corporate strike team," a drained body is "Continuity's work." The corporations keep cleaning up; they now have a better excuse.
5. **What Continuity is stays hidden.** The public knows Continuity is at war with the Big Three. It does not know why Continuity wanted the war, or who runs it (Bible §2, §5). **[OPEN]** (OQ-17) What it would cost for that to become known is the GM's, and this Challenge never answers it.
6. **The Series' question sharpens.** Fix it or take it: a public war is a city that can be saved from something visible, or seized while everyone is looking elsewhere (Bible §1, §4). The Key Players' agendas (WP4) say what each does next; a successor clock, if any, is the GM's to authorize (OQ-9).

## Power Sets

None.

## Canon and flags

- The clock: Bible §5. The Masquerade: Bible §3, Brief §4.1 (CR-4). Baselines blamed: Bible §2. Corp security's legality: Bible §3.
- **[BUILD CHOICE]** (BC-5) series-level Countdown at tier 6 — interviewer's choice. **[BUILD CHOICE]** (BC-13) the Specials, Threats, tier values, notch guide, and the "maxed" statement are this package's specification of BC-5; the GM may re-tier.
- **[OPEN]** (OQ-9) no other series-level clock; **[OPEN]** (OQ-17) the cost of Continuity's secret.
- Scale 4 is the table's largest listed rank (a block / a host, Core p. 118); the Challenge is Megacity-wide and the MC may treat its Scale as beyond the table when a Scaled action targets it.
