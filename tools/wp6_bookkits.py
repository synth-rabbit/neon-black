import re, glob, yaml, os
rows = [
(198,'Affiliation','Self',['Corporate Citizenship','Forbidden Cult','Criminal Syndicate','Counterculture']),
(199,'Affiliation','Self',['Hacker Collective','Law Enforcement','Neighborhood Hero','Street Gang']),
(202,'Assets','Self',['Code Arsenal','Guns & More Guns','Explosives','Heist Gear']),
(203,'Assets','Self',['Junk Collection','Motorcycle','Money to Burn','Safehouse']),
(206,'Expertise','Self',['Covert Agent','Impressive Physique','Gunslinger','Investigator']),
(207,'Expertise','Self',['Med Techie','Tinkerer','Ruthless Executive','Trained Killer']),
(210,'Horizon','Self',['Attain Enlightenment','Eliminate Corruption','Break the System','Exact Revenge']),
(211,'Horizon','Self',['Explore the Hidden Places','Live Honorably','Get Rich & Famous','Push Technology Further']),
(214,'Personality','Self',['Caregiver','Keeper of Secrets','Meticulous Planner','Performer']),
(215,'Personality','Self',['Rebel Without a Cause','Tough as Nails','Thrillseeker','Trendsetter']),
(218,'Troubled Past','Self',['Disaster Survivor','Tragic Loss','Escaped Servitude','Raised in Cyberspace']),
(219,'Troubled Past','Self',['Science Experiment','Target of the Government','Survived the Streets','Victim of Otherworldly Forces']),
(222,'Artifact','Mythos-OS',["Hero's Sword","Risk-Taker's Luck Charm",'Invisibility Helm','Mask of the Trickster God']),
(223,'Artifact','Mythos-OS',['Possessed Vehicle',"War God's Armor",'Scrying Crystals',"Wizard's Staff"]),
(226,'Companion','Mythos-OS',['Arcane Construct','Legendary Sidekick','Guardian Spirit','Magical Guide']),
(227,'Companion','Mythos-OS',['Nature Spirit','Tech Gremlin','Supernatural Pet','Trained Monsters']),
(230,'Esoterica','Mythos-OS',['Corpse Animation','Evil Eye',"Devil's Bargains",'Fortune Telling']),
(231,'Esoterica','Mythos-OS',['Potion Craft','Warding Signs','Spirit Summoning','Weapon Witching']),
(234,'Exposure','Mythos-OS',['Angelic Wings','Aura of Authority','Animate Shadows','Elemental Body']),
(235,'Exposure','Mythos-OS',['Floral Overgrowth','Speak with Machines','Midas Touch',"Warrior's Instincts"]),
(238,'Augmentation','Noise',['Animalistic Modifications','Boosted Mental Capacity','Armored Juggernaut','Chipped Weapon Mastery']),
(239,'Augmentation','Noise',['Enhanced Senses','Impossibly Good Looks','Hidden Gadgets','Reflex Booster Implants']),
(242,'Cutting Edge','Noise',['Advanced Railgun','Cloud of Nanites','Cloaking Jumpsuit','Cryptographic Skeleton Key']),
(243,'Cutting Edge','Noise',['Exoskeleton Suit','Force Fields','Experimental Vehicle','Self-Healing']),
(246,'Cyberspace','Noise',['Builder of Worlds','Cyberspace Ruins Explorer','Cybernetic Hijacker','Influencer']),
(247,'Cyberspace','Noise',['Information Broker','Post-Human Intelligence','Intrusion Specialist','Zeroed Identity']),
(250,'Drones','Noise',['Android Servants','Med Wagon','Giant Construction Robot','Mobile Weapons Platform']),
(251,'Drones','Noise',['RC Racing Star','Synthetic Guard Dog','Spy Satellites','Swarm of Probes']),
]
def slug(n):
    s=n.lower().replace('&','and').replace("'",'').replace('’','')
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')
kits={}
for pg,tb,cat,names in rows:
    for n in names: kits[slug(n)]=(n,tb,cat,pg)
refs={}
for p in sorted(glob.glob('02-splats/*/tropes/*.md')):
    t=open(p).read(); fm=yaml.safe_load(re.match(r'^---\n(.*?)\n---\n',t,re.S).group(1))
    for k in ('fixed_kits','choice_kits'):
        for s in fm[k]:
            s=s.replace('book:','')
            if s in kits: refs.setdefault(s,set()).add(fm['slug'])
cites={}
for p in glob.glob('02-splats/*/theme-kits/*existing-kits.md')+['03-self-kits/existing-self-kits.md']:
    t=open(p).read(); fm=yaml.safe_load(re.match(r'^---\n(.*?)\n---\n',t,re.S).group(1))
    for s,(n,tb,cat,pg) in kits.items():
        pat=r'\*\*'+re.escape(n)+r'\*\*'
        pat=pat.replace("'", "['’]")
        if re.search(pat,t): cites.setdefault(s,set()).add(fm['slug'])
BC='BC-{BC_BOOK}'
head=f'''---
type: index
name: "Book Kits Index"
slug: book-kits-index
status: review
source: core
page: "196–251, 156–157"
owner: WP6
canon_refs: ["Plan A.1 rule 1", "Plan A.4 character-trope", "Brief §0.1", "Core p. 196–251", "Core p. 156–157"]
flags: [BUILD CHOICE]
player_safe: true
---

# Book Kits Index

Every printed theme kit the vault offers or references, with themebook, category, and page, so that a reference to a book kit can be told from a reference to a vault kit. **[BUILD CHOICE]** ({BC}) Book kits have no vault file — they are offered as printed, never copied in (Plan A.1 rule 1, Brief §0.1) — so a `character-trope` lists them in `fixed_kits` / `choice_kits` as `book:<slug>` (e.g. `book:trained-killer`), while a vault kit is a bare slug that resolves to a file. Prose links this index, never a book kit. WP9 maps a `book:` entry to the system's shipped themebook by `themebook` name and leaves the kit itself to the table; it converts nothing for it.

The slug is the printed name in kebab-case ASCII (`&` → `and`, apostrophes dropped). The last two columns say which vault tropes take the kit and which "existing kits" lists offer it with a re-flavor line. Mythos kits are offered only under the Tao reinterpretation in those lists (Brief §3.2, CR-1); several are listed there as *not offered* — this index records the page, not the offer.

## Core theme kits (Core p. 196–251)

| Slug | Kit | Themebook | Category | Page | Taken by trope | Offered in |
|---|---|---|---|---|---|---|'''
lines=[head]
for s,(n,tb,cat,pg) in sorted(kits.items(), key=lambda x:(x[1][3],x[0])):
    tr=', '.join(f'[[{x}]]' for x in sorted(refs.get(s,[]))) or '—'
    ci=', '.join(f'[[{x}]]' for x in sorted(cites.get(s,[]))) or '—'
    lines.append(f'| `{s}` | {n} | {tb} | {cat} | Core p. {pg} | {tr} | {ci} |')
lines.append(f'''
## Crew theme kits (Core p. 156–157)

| Slug | Kit | Themebook | Category | Page | Offered in |
|---|---|---|---|---|---|
| `found-family` | Found Family | Crew (Otherscape) | Crew-OS | Core p. 156 | [[existing-crew-kits]] |
| `rebellious-street-gang` | Rebellious Street Gang | Crew (Otherscape) | Crew-OS | Core p. 156 | [[existing-crew-kits]] |
| `wanted` | Wanted | Crew (Otherscape) | Crew-OS | Core p. 157 | [[existing-crew-kits]] |

## Tokyo theme kits

None are referenced by a trope. Tokyo's Megacity Specials (Tokyo p. 72–74) are Specials, not kits, and are cited from the `pc-specials/` files that adapt them.

## Canon and flags

- **[BUILD CHOICE]** ({BC}) the `book:` prefix convention and this index as the single place a book kit's page is recorded.
- Kit names and pages transcribed from `ref/core-book-paged.txt`; where a page prints two kits in parallel columns, both carry that page.
''')
open('02-splats/book-kits-index.md','w').write('\n'.join(lines))
print(len(kits),'kits', len(refs),'referenced by tropes')
for p in sorted(glob.glob('02-splats/*/tropes/*.md')):
    t=open(p).read()
    def fix(m):
        key=m.group(1); items=[x.strip() for x in m.group(2).split(',')]
        items=[('book:'+x if (x in kits and not x.startswith('book:')) else x) for x in items]
        return f'{key}: [{", ".join(items)}]'
    t2=re.sub(r'^(fixed_kits|choice_kits): \[([^\]]*)\]',fix,t,flags=re.M)
    open(p,'w').write(t2)
    print(p, re.findall(r'^(?:fixed_kits|choice_kits): .*$',t2,re.M))
