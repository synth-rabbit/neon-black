---
type: power-set
name: "Chancery-Badged"
slug: chancery-badged
status: review
source: custom
page: ""
owner: WP5
canon_refs: ["Bible §3", "Core p. 304", "Core p. 326–329"]
flags: [BUILD CHOICE]
player_safe: false
splat: none
category: Self
applies_to: "Any Challenge representing a person or unit acting under Chancery or corporate legal authority — Security Guards, HURT Tactics Officers, Corporate Executives, or the tier-lift checkpoint itself."
default_tags: ["badge carries weight", "the paperwork backs them up"]
default_statuses: []
specials:
  - {name: "Badge Carries Weight", text: "When this Challenge is threatened, attacked, or legally challenged, it can invoke its standing to give whoever pressed it a status representing legal or bureaucratic trouble — assault charge, obstruction, an inspection nobody asked for — at the same tier as the pressure it took, up to tier 4."}
  - {name: "Exactly as Legal as the Police", text: "Immune to a wanted or arrest status from any authority lower in the corporate-or-government hierarchy than its own badge (Bible §3). A rival corp's security or the Chancery's own officers can still press it; the crew usually cannot."}
threats:
  - threat: "Flash a badge, a corporate seal, or a Chancery permit."
    consequences:
      - {text: "Bystanders and lower-tier security stand down (Deny Them Something They Want).", statuses: [], tags: []}
  - threat: "Cite a statute, a contract clause, or an ordinance — real or invented, and it rarely matters which."
    consequences:
      - {text: "Burn a tag representing the target's legal standing, or give them legal-trouble-2.", statuses: ["legal-trouble-2"], tags: []}
---

# Chancery-Badged

**Applies to:** Any Challenge representing a person or unit acting under Chancery or corporate legal authority. · **Category:** Self · **Splat:** none

The setting's legal-cover Power Set, on the book's Self Power Set pattern (*Connected & Protected*, *Corporate Sponsored*, Core p. 328). Every corporation's security is exactly as legal as the city police (Bible §3) — this overlay is what makes that fact bite mechanically, whether it is stacked on a Security Guard, a HURT Officer, a Corporate Executive, or [[chancery-checkpoint]] itself. It carries no splat content and applies equally to a Chancery officer and a corp's own hire, because the setting insists there is no mechanical difference between them.

## Tags & statuses

badge carries weight, the paperwork backs them up

## Specials

**Badge Carries Weight:** Pressed against, it turns the pressure back as legal or bureaucratic trouble for whoever pressed — up to tier 4.

**Exactly as Legal as the Police:** Immune to a wanted/arrest status from anything lower in the corporate-or-government hierarchy than itself (Bible §3).

## Threats / Consequences

› Flash a badge, a corporate seal, or a Chancery permit.
» Bystanders and lower-tier security stand down (Deny Them Something They Want)

› Cite a statute, a contract clause, or an ordinance — real or invented, and it rarely matters which.
» Burn a legal-standing tag, or *legal-trouble-2*

## Canon and flags

- Bible §3: corporate security forces are exactly as legal as the city police; the government is deeply corrupt. This overlay states that fact mechanically and adds no new canon.
- **[BUILD CHOICE]** this Power Set and its two Specials are this package's invention, modeled on the book's *Connected & Protected* and *Corporate Sponsored* Self Power Sets (Core p. 328) rather than reused verbatim.
