import re, os
os.chdir('/home/claude/neon-black')
# ---- running-shape scope
p='06-key-players/packs/challenges/running-shape.md'; t=open(p).read()
old=t[t.index('**Note for WP6.**'):]; old=old[:old.index('\n')+1]
new='**Two Howler overlays (WP6, BC-133).** The vault keeps two: [[running-on-leash]] (WP2) is the splat package\'s general overlay for any Howler on a dose — a Gang Member, a Leg-Breaker, a named body anywhere in Palisade — and is the one [[leash-frenzy-pack]] layers. This file is the **Run\'s own** overlay, built on Meliora\'s settling mechanism (BC-108) so the *settled* clock is something the pack reads and the crew cannot; the packs\' Challenges use it. Never put both on one Challenge. Under either, a dosed Howler stays a person who can come down and be talked to; neither is a frenzy (OQ-49 records the wording difference for the GM).\n'
t=t.replace(old,new)
t=t.replace('**[OPEN]** (OQ-46) whether WP2\'s werewolf Power Set supersedes this file.','**[OPEN]** (OQ-46) resolved by WP6 — both overlays kept, scoped (BC-133); (OQ-49) how much of a person a dosed Howler remains, for the GM.')
open(p,'w').write(t)
# ---- running-on-leash scope + soften Nothing to Reason With
p='02-splats/werewolf/power-sets/running-on-leash.md'; t=open(p).read()
t=t.replace('any attempt to convince, frighten, bribe, or bargain with this Challenge resolves one success level lower."}',
            'any attempt to convince, frighten, bribe, or bargain with this Challenge resolves one success level lower. It can still be talked to — the dose makes a Howler hard to reach, not mindless; see Come Down."}')
t=t.replace('**Nothing to Reason With:** While the dose holds, any attempt to convince, frighten, bribe, or bargain with this Challenge resolves one success level lower.',
            '**Nothing to Reason With:** While the dose holds, any attempt to convince, frighten, bribe, or bargain with this Challenge resolves one success level lower. It can still be talked to — the dose makes a Howler hard to reach, not mindless (see Come Down).')
old='The overlay for the hour the dose is working. Layer it onto a Gang Member, a Syndicate Leg-Breaker, or a named pack Challenge; before the dose goes in, that profile runs as printed and this Power Set is not on it.'
new=old+'\n\n**Two Howler overlays (WP6, BC-133).** This is the general overlay for any Howler on a dose anywhere in Palisade, and the one [[leash-frenzy-pack]] layers. The Run\'s own overlay, [[running-shape]] (WP4-trio2), models the same dose through Meliora\'s settling mechanism and a *settled* clock the pack can read; the packs\' named Challenges use that one. Never apply both to one Challenge. Under either, a Howler on the dose remains a person — hindered here, not mindless — who comes down and can be talked to (OQ-49 records the difference in wording for the GM). [[pack-tactics]] stacks with either.'
assert old in t; t=t.replace(old,new)
open(p,'w').write(t)
# ---- leash-frenzy-pack
p='08-challenges/custom/leash-frenzy-pack.md'; t=open(p).read()
t=t.replace('  - {name: "Pending WP2 Power Set", text: "This profile stands alone; it does not require the werewolf splat\'s own Power Set to function. When WP2 writes the werewolf splat\'s Power Set (pending WP2, `02-splats/werewolf/power-sets/`), an MC may layer it on top of this Challenge for full crunch — until then, the tags and Specials above already carry the heightened strength, senses, and regeneration a Howler mid-Leash has (Bible §2)."}',
            '  - {name: "Howler Overlay", text: "This profile stands alone; the tags and Specials above already carry the heightened strength, senses, and regeneration a Howler mid-Leash has (Bible §2). Layer [[running-on-leash]] on top for full crunch (the dose as running-3, Come Down as the crash). A pack of the Run in the Cinder Yards uses [[running-shape]] instead — never both. Under any overlay the pack are people, not beasts: coordinated, counting their doses, able to break off and to be talked to (BC-133, OQ-49); Dogs Off the Chain is the street\'s account, not the fact."}')
t=t.replace('**Pending WP2 Power Set:** Stands alone; a future werewolf Power Set from WP2 layers on top rather than being required.',
            '**Howler Overlay:** Stands alone; layer [[running-on-leash]] for full crunch, or [[running-shape]] for a Run pack — never both. The pack are people, not beasts (BC-133, OQ-49).')
t=t.replace('None required — see the "Pending WP2 Power Set" Special above.','[[running-on-leash]] (general) or [[running-shape]] (the Run) — optional, never both; see the *Howler Overlay* Special. [[pack-tactics]] stacks with either.')
t=t.replace('power_sets: []','power_sets: [running-on-leash]')
open(p,'w').write(t)
# ---- anti-tao pair
p='08-challenges/custom/anti-tao-countermeasure-challenge.md'; t=open(p).read()
t=t.replace('power_sets: []','power_sets: [anti-tao-countermeasure]')
t=re.sub(r'## Power Sets\n\nNone\.\n','## Power Sets\n\n[[anti-tao-countermeasure]] (WP2-mage) — the Noise overlay for any countermeasure element: *Grounding*, *Null Field*, *It Went in the Log*. This profile is the fixed installation the overlay sits on; apply it rather than restating it (BC-134). Both are Noise-category engineering, never a Tao effect, and neither gives Tao a will.\n',t)
open(p,'w').write(t)
p='02-splats/mage/power-sets/anti-tao-countermeasure.md'; t=open(p).read()
t=t.replace('- The cross-cutting **Challenge profile** for an anti-Tao countermeasure is WP5\'s (`08-challenges/custom/`, pending WP5). This file is the overlay only; a WP5 profile should apply it rather than restate it.',
            '- The cross-cutting **Challenge profile** for an anti-Tao countermeasure is [[anti-tao-countermeasure-challenge]] (WP5): the fixed installation, with `detect` and `shutdown-or-override` Limits. This file is the overlay only; that profile applies it (BC-134). The man-portable versions are [[null-field-emitter]] and [[tao-null-round]].')
t=t.replace('- Which corporations field which countermeasures, who sells them, and how good they are is WP4\'s (`06-key-players/corp-a/`, `corp-c/`, pending WP4). **[OPEN]** (OQ-24).',
            '- Which corporations field which countermeasures: Meliora\'s **Adjunct Series** and AP&I\'s **Field Assurance** ([[corp-a]], [[corp-c]], [[corp-b]]; BC-117). How good they are, and whether either can reproduce a working, stays **[OPEN]** (OQ-24).')
t=t.replace('- [[corp-b|Orison Defense Systems]] (pending WP4) is the corporation','- [[corp-b|Orison Defense Systems]] is the corporation')
open(p,'w').write(t)
# ---- wuji-operative pair
p='06-key-players/tao-society/challenges/wuji-operative-challenge.md'; t=open(p).read()
t=t.replace('**Arcane** (Core p. 330) — **[TAO-REINTERPRETED]** (CR-1) as above.','[[wuji-operative]] (WP2-mage) is the overlay for any *other* practitioner Challenge acting for the House — an instructor, a placed member on an errand; this profile is the House\'s field agent written in full and does not stack it (its *Arrest* and *The Condition* describe the same discipline from two sides — BC-134). **Arcane** (Core p. 330) — **[TAO-REINTERPRETED]** (CR-1) as above.')
open(p,'w').write(t)
p='02-splats/mage/power-sets/wuji-operative.md'; t=open(p).read()
old='**MC only.** Everything about this overlay assumes facts a Caster PC does not have ([[casters]] §2).'
new=old+' The House\'s field agent written as a full Challenge is [[wuji-operative-challenge]] (WP4-trio3); this overlay is for any other practitioner Challenge acting for the House and is not stacked on that profile (BC-134).'
assert old in t; t=t.replace(old,new)
open(p,'w').write(t)
print('ok')
