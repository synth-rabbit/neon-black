---
type: challenge
name: "Fresh Cut"
slug: fresh-cut
status: review
source: custom
page: "294–300, 329"
owner: WP4-trio3
canon_refs: ["Bible §2 changeling", "Bible §3 Masquerade", "Bible §4 theme 3", "Brief §2.1", "Brief §2.5 changeling", "Brief §8", "Plan A.6", "Core p. 294–300", "Core p. 329"]
flags: [BUILD CHOICE, OPEN, RULES CONFLICT]
player_safe: false
role: target
scale: 0
alias: "someone hurt, in a coat that is not theirs"
short_description: "A Doppel days out of ownership: switch and tracker cut out, scars still taped, hunted by the people who made them, and worth money to everyone who is not the crew."
limits:
  - {name: keep-them-alive, tier: 4}
  - {name: get-them-clear, tier: 5}
  - {name: earn-their-trust, tier: 4}
  - {name: hurt-or-subdue, tier: 2}
default_tags: ["a face nobody has flagged yet", "two weeks of a special unit's interior", "surgical sites, still taped", "flinches at alarms", "nothing to their name"]
default_statuses: ["hunted-3", "post-surgical-3"]
specials:
  - {name: "The Switch Is Out", text: "Canon: an escapee has removed both the kill switch and the tracker (Bible §2). Nobody can kill this Doppel by remote, and nobody is following a signal. Every hunter in this Challenge is doing it the hard way — by the face, by the batch, by the people who knew them — which is slower, uglier, and more dangerous to everyone standing nearby."}
  - {name: "Not Well", text: "post-surgical does not heal during the job. While it is 2 or higher, every roll this Doppel makes to run, fight, climb, or hold a face is reduced by one level of success, and any physical status they take is one tier worse. Removing it takes the Sump, a fortnight, and money the cell does not have."}
  - {name: "Wears What It Needs", text: "Once per scene, if given a minute and a look at somebody, the Doppel can take that person's face and voice — Face-Dancer impersonation at the level the Bible allows (Bible §2). Doing it while post-surgical is 2 or higher costs them: add a tier to post-surgical, and if that would take it above 5, they collapse."}
  - {name: "Waiting To Be Told", text: "Eleven days is not long enough to stop being owned. The first time in each scene the crew gives this Doppel a direct order, they obey it instantly and completely, even when it is a bad order — and everyone at the table sees it happen. A crew that notices and stops giving orders gains a tier on earn-their-trust; a crew that uses it maxes hurt-or-subdue on the trust, permanently."}
  - {name: "Worth More Than They Know", text: "What this Doppel remembers about clearances, rotations and corridors is worth more than their surgery to at least three buyers: a corporation that wants the leak closed, a rival that wants the interior, and a fixer who will sell them either. Any scene where the crew asks about it can be the scene where somebody else finds out they were asked."}
threats:
  - threat: "They stop dead in a crowd because somebody ahead is wearing a coat they recognize."
    consequences:
      - {text: "They bolt, badly, in the wrong direction, and the crew loses sight of them (add a tier to get-them-clear and give the crew searching-3).", statuses: ["searching-3"], tags: []}
      - {text: "The recognition was correct, and the coat has already turned around (Present a New Challenge: Product Integrity Recovery Team, or a corporate recovery crew — Mercenary Gunslinger, Core p. 307, Scale 1).", statuses: [], tags: []}
  - threat: "They peel the tape back to look at the site and it is weeping."
    consequences:
      - {text: "The wound has opened; they cannot run tonight (add a tier to post-surgical).", statuses: ["post-surgical-4"], tags: []}
      - {text: "They need the Sump, which means the Old Sump Stair, which means a route somebody is watching (Make the Future Bleaker).", statuses: [], tags: ["they need the Sump tonight"]}
  - threat: "Somebody offers, kindly and in public, to take them somewhere safe."
    consequences:
      - {text: "They go, because being told what to do is the deepest thing in them (the crew loses them; Deny Them Something They Want).", statuses: [], tags: []}
      - {text: "The offer was a recovery contract with a clean face on it, and the crew has met a Doppel who did not run (Escalate the Situation).", statuses: [], tags: []}
  - threat: "They start telling the crew about a corridor, and a clearance, and a technician's voice."
    consequences:
      - {text: "The crew learns something about a corporation's interior that they cannot un-know, and cannot sell without saying where it came from (a fragment nobody should have).", statuses: [], tags: ["a fragment nobody should have"]}
      - {text: "Escalate the Situation: within a day, whoever the fragment belongs to hears that somebody was asking.", statuses: [], tags: []}
  - threat: "They ask, flatly, whether the crew is going to sell them, and wait for the answer with no expectation either way."
    consequences:
      - {text: "Answered honestly, either way: add a tier to earn-their-trust (an honest no) or end it (any lie they later find out about).", statuses: [], tags: []}
      - {text: "Unanswered: they decide for themselves, and are gone by the next scene, back toward the only people who ever told them what they were for (Make the Future Bleaker).", statuses: [], tags: []}
power_sets: []
reuse_of: "Sought After (Core p. 329) is the structural model for a person treated as a plot element; Shape-Changing (Tokyo p. 137) for the face, with CR-19 noted."
---

# Fresh Cut

**Role:** target · **Scale:** 0 (one person) · **Alias:** *someone hurt, in a coat that is not theirs* · *A Doppel days out of ownership, hunted by the people who made them.*

*Fresh cut* is what Gallery Nine calls a new escapee, and it is not affectionate ([[names]]; BC-124). This profile is the escapee as the thing the job is about — someone the crew has to keep alive, get clear, and be trusted by, any one of which can fail on its own. The default subject is [[corin-alvarez]]; it fits any recent escapee.

Canon first, because it is the whole shape of the Challenge: **the switch and the tracker are already out** (Bible §2). There is no remote kill, no signal to follow, and no ticking device. The danger is entirely human — makers, recovery crews, buyers, and a fixer who will sell an address — and the escapee's greatest liability is not the hunt. It is that eleven days is not long enough to stop doing what you are told.

## Limits

| Limit | Tier |
|---|---|
| keep them alive | 4 (progress — the crew's) |
| get them clear | 5 (progress — the crew's) |
| earn their trust | 4 (progress — the crew's) |
| hurt or subdue | 2 |

## Tags & statuses

a face nobody has flagged yet · two weeks of a special unit's interior · surgical sites, still taped · flinches at alarms · nothing to their name · *hunted-3* · *post-surgical-3*

## Specials

**The Switch Is Out:** No remote kill and no signal (Bible §2). Every hunter here works by the face, the batch, and the people who knew them — slower, uglier, and worse for bystanders.

**Not Well:** *post-surgical* does not heal during the job. At 2 or higher, every roll to run, fight, climb, or hold a face drops one level of success, and physical statuses land one tier worse. Removing it takes the Sump, a fortnight, and money the cell does not have.

**Wears What It Needs:** Once per scene, given a minute and a look, they can take a face and voice. Doing it while *post-surgical* is 2 or higher adds a tier to it; above 5, they collapse.

**Waiting To Be Told:** The first direct order the crew gives them each scene is obeyed instantly and completely, even when it is a bad order, in front of everyone. Noticing and stopping earns a tier on *earn their trust*; using it ends the trust permanently.

**Worth More Than They Know:** What they remember about clearances, rotations, and corridors is worth more than their surgery to at least three buyers. Any scene where the crew asks can be the scene where someone learns they asked.

## Threats / Consequences

› They stop dead in a crowd because somebody ahead is wearing a coat they recognize.
» They bolt in the wrong direction (*searching-3*; a tier to *get them clear*)
» The recognition was right, and the coat has turned around (Present a New Challenge: [[product-integrity-team]] or Mercenary Gunslinger, Core p. 307, Scale 1)

› They peel the tape back and the site is weeping.
» The wound has opened; no running tonight (*post-surgical-4*)
» They need the Sump, which means the Old Sump Stair, which means a watched route (*they need the Sump tonight*)

› Somebody offers, kindly and in public, to take them somewhere safe.
» They go, because being told is the deepest thing in them (Deny Them Something They Want)
» The offer was a recovery contract with a clean face on it (Escalate the Situation)

› They start telling the crew about a corridor, and a clearance, and a technician's voice.
» Something about a corporation's interior the crew cannot un-know or safely sell (*a fragment nobody should have*)
» Escalate the Situation: whoever it belongs to hears that somebody was asking

› They ask, flatly, whether the crew is going to sell them.
» Answered honestly: a tier on *earn their trust* — or, if it is a lie they later discover, the end of it
» Unanswered: gone by next scene, back toward the only people who ever told them what they were for (Make the Future Bleaker)

## Power Sets

**Sought After** (Core p. 329) — the structural model, and usable as written: *After Them!* and *Look Who We Found* are exactly this Challenge. **Shape-Changing** (Tokyo p. 137) for the face — **[RULES CONFLICT]** (CR-19), see `reuse.md`.

## Canon and flags

- Doppels are owned with kill switches and trackers; escapees removed both, live in constant danger, and group with other escapees; some have Face-Dancer impersonation; escaped society is purely underground with no political pull (Bible §2, §3). Ownership versus freedom (Bible §4).
- **[BUILD CHOICE]** (BC-123) *Not Well*, *Waiting To Be Told*, and the Sump's price; (BC-124) *fresh cut* as the cell's slang.
- **[RULES CONFLICT]** (CR-19) the face as Noise versus the book's Mythos Power Set — options in `reuse.md`, unresolved.
- **[OPEN]** (OQ-30) **who made them is not answered by any Consequence here.** The *fragment nobody should have* is a corridor, a clearance, and a voice — never a name and never a logo. **[OPEN]** (OQ-48) whether a recovery crew is acting lawfully.
