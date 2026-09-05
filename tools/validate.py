#!/usr/bin/env python3
"""Neon Black vault validator — Plan Part C checks (written by WP6; used by WP8/WP9).

Run from anywhere:  python3 tools/validate.py [--quiet] [--warnings]
Exit code 1 if any ERROR. Warnings never fail the run.

Checks (Plan Part C, A.4, A.5, A.6, A.8; BC-125..128):
  frontmatter  valid YAML; common fields present; `type` in the closed set; `slug` == basename;
               basenames unique vault-wide; H1 == name; status in draft|review|approved; player_safe bool
  kits         theme-kit / crew-kit: 10 power tags A–J (A non-empty = title tag), 4 weakness tags A–D,
               themebook in the 14 (+ Crew), motivation_type matches category
  tropes       character-trope: 3 fixed + 3 choice kits; vault kits resolve; book kits carry `book:` and
               appear in book-kits-index
  challenges   role in the nine; ≥1 Limit with tier 2–6 (999 = immune allowed); scale int; every Threat
               has ≥1 Consequence
  power sets   ≥1 Special or Threat
  markers      every inline marker has its `flags:` entry and vice versa; every (BC-n)/(OQ-n)/(CR-n) cited
               exists in its register
  links        every [[wikilink]] resolves (template placeholders and the registered pending list excepted);
               a `player_safe: true` file links only to `player_safe: true` files (Plan C.8; BC-175)
  vocabulary   forbidden terms (season, case, Danger, Rift, Logos, Mist); "splat" in player_safe prose;
               Mythos/Mythoi/legend/Conjuration/Avatar/Source outside mechanical phrases or a
               [TAO-REINTERPRETED] file  (warnings unless clearly wrong)
               Documented exceptions (BC-136), because Plan C.6 forbids these as game/TV vocabulary, not as English:
                 case    reported only when it reads as a scenario-word for a Job — capitalized `Case` (outside a
                         Special's title such as *Never Opens the Case*), `a/the/this/that/our/next/new/first/last/
                         open/closed/cold case` NOT followed by an object noun, `case file(s)`, `work(ing)/on/take/took
                         the case`. Containers (crate case, hard-shell case, dose case, weather-case), grammar, idioms
                         (in any case, worst case, in which case, make the case) and the verb `case a room` pass.
                 season  reported only as `season one/two/…`, `season finale/arc/premiere/of play`, `season-long`, or
                         `first/second/next/last/the season`; a fashion, weather or calendar season passes.
                 meta    `type: meta` files (registers, style guide) are exempt from the vocabulary and cosmology
                         checks: they quote the forbidden list itself.
  canon        Bloodware/Howler files: sun/fire/stake/garlic/silver as weaknesses; hunter kits: sculpt/bio;
               any sentence giving Tao a will
"""
import os, re, sys, glob, collections
try:
    import yaml
except ImportError:
    print("pyyaml required: pip install pyyaml"); sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
QUIET = '--quiet' in sys.argv
SHOW_WARN = '--warnings' in sys.argv or not QUIET

TYPES = {'theme-kit', 'character-trope', 'pc-special', 'crew-special', 'crew-kit', 'district', 'key-player',
         'npc', 'challenge', 'power-set', 'job', 'scene', 'loadout-item',
         'meta', 'series', 'splat-overview', 'index', 'membership'}
COMMON = ['type', 'name', 'slug', 'status', 'source', 'page', 'owner', 'canon_refs', 'flags', 'player_safe']
THEMEBOOKS = {'Affiliation', 'Assets', 'Expertise', 'Horizon', 'Personality', 'Troubled Past',
              'Artifact', 'Companion', 'Esoterica', 'Exposure', 'Augmentation', 'Cutting Edge', 'Cyberspace', 'Drones',
              'Crew', 'Crew (Otherscape)', 'Loadout'}
CATEGORY_MOTIVATION = {'Self': 'identity', 'Noise': 'itch', 'Mythos-OS': 'ritual', 'Mythos': 'ritual'}
ROLES = {'asset', 'attacker', 'barrier', 'countdown', 'mystery', 'pursuer', 'target', 'temptation', 'watcher'}
MARKERS = {'RULES CONFLICT', 'BUILD CHOICE', 'TAO-REINTERPRETED', 'OPEN'}
# Links to files a later package writes (Plan A.3): registered here, cleared by the package that writes them.
PENDING = {}   # WP7 wrote breakout / investigation / acquisition; WP8 cleared the list (BC-175). Add entries only for files a later package is assigned.
SKIP_DIRS = ('ref/', 'tools/', '.git/', '.claude/', '00-meta/additions/', 'build/')   # assets/manifest.md is validated; images are not .md; build/ is WP9's git-ignored Foundry output

errors, warnings = collections.defaultdict(list), collections.defaultdict(list)
def err(p, m): errors[p].append(m)
def warn(p, m): warnings[p].append(m)

def strip_code(text):
    text = re.sub(r'```.*?```', ' ', text, flags=re.S)
    return re.sub(r'`[^`\n]*`', ' ', text)

def split(path):
    t = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', t, re.S)
    if not m: return None, t
    return m.group(1), m.group(2)

files = [p for p in sorted(glob.glob('**/*.md', recursive=True))
         if '/' in p and not p.startswith(SKIP_DIRS)]
by_base = collections.defaultdict(list)
for p in files: by_base[os.path.basename(p)[:-3]].append(p)
for b, ps in by_base.items():
    if len(ps) > 1:
        for p in ps: err(p, f'basename `{b}` is not unique vault-wide: {ps}')

# register ids
def ids_in(path, kind):
    t = open(path, encoding='utf-8').read() if os.path.exists(path) else ''
    return set(int(x) for x in re.findall(r'\*\*' + kind + r'-(\d+)\*\*', t))
REG = {'BC': ids_in('00-meta/build-choices.md', 'BC'),
       'OQ': ids_in('00-meta/open-questions.md', 'OQ'),
       'CR': ids_in('00-meta/conflict-register.md', 'CR')}

book_kits = set(re.findall(r'^\| `([a-z0-9-]+)` \|', open('02-splats/book-kits-index.md', encoding='utf-8').read(), re.M)) \
    if os.path.exists('02-splats/book-kits-index.md') else set()

fm_by_path = {}
ps_links = collections.defaultdict(set)   # player-safe file -> link targets (Plan C.8; BC-175)
stats = collections.Counter()
for p in files:
    is_template = p.startswith('99-templates/')
    fm_text, body = split(p)
    if fm_text is None:
        err(p, 'no YAML frontmatter'); continue
    try:
        fm = yaml.safe_load(fm_text) or {}
    except Exception as e:
        err(p, f'YAML does not parse: {str(e).splitlines()[0]}'); continue
    fm_by_path[p] = fm
    base = os.path.basename(p)[:-3]
    for k in COMMON:
        if k not in fm: err(p, f'missing frontmatter field `{k}`')
    ty = fm.get('type')
    if ty not in TYPES: err(p, f'`type: {ty}` not in the closed set (BC-127)')
    if fm.get('status') not in ('draft', 'review', 'approved'): err(p, f'bad status `{fm.get("status")}`')
    if not isinstance(fm.get('player_safe'), bool): err(p, '`player_safe` must be true or false (BC-128)')
    if not is_template:
        if fm.get('slug') != base: err(p, f'slug `{fm.get("slug")}` != basename `{base}` (BC-125)')
        stats[ty] += 1
    h1 = re.search(r'^# (.+)$', body, re.M)
    if not h1: err(p, 'no H1')
    elif str(fm.get('name', '')).strip() != h1.group(1).strip():
        err(p, f'H1 `{h1.group(1).strip()}` != name `{fm.get("name")}`')
    if not isinstance(fm.get('flags'), list): err(p, '`flags` must be a list')
    if is_template:
        continue

    # --- kits
    if ty in ('theme-kit', 'crew-kit'):
        pt, wt = fm.get('power_tags') or [], fm.get('weakness_tags') or []
        if len(pt) != 10: err(p, f'{len(pt)} power tags (need 10)')
        if len(wt) != 4: err(p, f'{len(wt)} weakness tags (need 4)')
        letters = [x.get('letter') for x in pt if isinstance(x, dict)]
        if letters != list('ABCDEFGHIJ')[:len(letters)]: err(p, f'power tag letters {letters}')
        wl = [x.get('letter') for x in wt if isinstance(x, dict)]
        if wl != list('ABCD')[:len(wl)]: err(p, f'weakness tag letters {wl}')
        if pt and not str(pt[0].get('tagname', '')).strip(): err(p, 'tag A (title tag) is empty')
        for x in pt + wt:
            tn = str(x.get('tagname', ''))
            if re.search(r'\d', tn): warn(p, f'tag `{tn}` contains a number (style-guide §2.3)')
        tb = fm.get('themebook')
        if tb not in THEMEBOOKS: err(p, f'themebook `{tb}` not one of the 14 (+ Crew/Loadout)')
        cat, mt = fm.get('category'), fm.get('motivation_type')
        if mt not in ('identity', 'ritual', 'itch'): err(p, f'motivation_type `{mt}`')
        exp = CATEGORY_MOTIVATION.get(cat)
        if exp and mt != exp:
            if fm.get('splat') == 'hunter' and cat == 'Noise' and mt == 'itch':
                pass
            elif cat == 'Noise' and mt == 'itch':
                pass
            else:
                warn(p, f'category {cat} with motivation_type {mt} (expected {exp}; Plan A.5)')
        if ty == 'theme-kit' and cat not in ('Self', 'Noise', 'Mythos-OS'): err(p, f'category `{cat}`')
        if ty == 'crew-kit' and cat != 'Crew-OS': err(p, f'crew kit category `{cat}`')
    # --- tropes
    if ty == 'character-trope':
        for k in ('fixed_kits', 'choice_kits'):
            ks = fm.get(k) or []
            if len(ks) != 3: err(p, f'{k} has {len(ks)} entries (need 3)')
            for s in ks:
                s = str(s)
                if s.startswith('book:'):
                    if s[5:] not in book_kits: err(p, f'{k}: `{s}` not in book-kits-index')
                elif s not in by_base:
                    err(p, f'{k}: `{s}` is neither a vault kit nor `book:<slug>` (BC-126)')
    # --- challenges
    if ty == 'challenge':
        if fm.get('role') not in ROLES: err(p, f'role `{fm.get("role")}`')
        if not isinstance(fm.get('scale'), int): err(p, 'scale missing or not an int')
        lims = fm.get('limits') or []
        if not lims: err(p, 'no Limits')
        for l in lims:
            tier = l.get('tier') if isinstance(l, dict) else None
            if tier == 999 or tier == '-': continue
            if not isinstance(tier, int) or not 2 <= tier <= 6: err(p, f'Limit `{l.get("name") if isinstance(l, dict) else l}` tier {tier} outside 2–6')
        for th in fm.get('threats') or []:
            if not (isinstance(th, dict) and th.get('consequences')):
                err(p, f'Threat without Consequences: {str(th)[:60]}')
        if not (fm.get('threats')): err(p, 'no Threats')
    if ty == 'power-set':
        if not (fm.get('specials') or fm.get('threats')): err(p, 'power set has neither Specials nor Threats')
        for th in fm.get('threats') or []:
            if not (isinstance(th, dict) and th.get('consequences')): err(p, f'Threat without Consequences: {str(th)[:60]}')
        for l in fm.get('limits') or []:
            tier = l.get('tier') if isinstance(l, dict) else None
            if tier not in (999, '-') and not (isinstance(tier, int) and 2 <= tier <= 6):
                err(p, f'Power Set Limit tier {tier} outside 2–6')
    if ty == 'npc':
        ch = fm.get('challenge')
        if ch and ch not in by_base: err(p, f'challenge `{ch}` does not resolve')
        if ch == fm.get('slug'): err(p, 'npc and its challenge share a slug (BC-125)')
    if ty == 'key-player':
        for k in ('key_characters', 'challenges', 'territory'):
            for s in fm.get(k) or []:
                if s not in by_base: err(p, f'{k}: `{s}` does not resolve')
    if ty == 'district':
        if fm.get('type') == 'district' and p.startswith('05-megacity/districts/'):
            if not fm.get('story_tag'): err(p, 'district without story_tag')
            if not fm.get('zone_code'): err(p, 'district without zone_code')

    # --- markers and register ids
    prose = strip_code(body)
    flags = set(fm.get('flags') or [])
    for mk in MARKERS:
        used = f'[{mk}]' in prose
        if used and mk not in flags: err(p, f'marker [{mk}] used but not in flags')
        if mk in flags and not used and ty not in ('meta', 'index'): warn(p, f'flags lists {mk} but the marker is not used in the body')
    for kind, n in re.findall(r'\b(BC|OQ|CR)-(\d+)\b', prose):
        if int(n) not in REG[kind]: err(p, f'{kind}-{n} is cited but has no register row')
    if re.search(r'\b(BC|OQ|CR)-WP\d', prose): err(p, 'un-renumbered package-local register id')

    # --- links
    for m in re.finditer(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]', prose):
        tgt = m.group(1).strip()
        if tgt.startswith('assets/'): continue
        if fm.get('player_safe') is True: ps_links[p].add(tgt)
        if tgt in by_base: continue
        if tgt in PENDING: warn(p, f'[[{tgt}]] pending {PENDING[tgt]}'); continue
        err(p, f'unresolved wikilink [[{tgt}]]')

    # --- vocabulary (Plan C.6, C.2)
    prose = re.sub(r'!\[\[assets/[^\]]+\]\]', '', prose)   # image embeds are paths, not prose (assets/splats/…)
    ps = fm.get('player_safe') is True
    vocab = ty not in ('meta',)   # registers and the style guide quote the forbidden list itself
    for w in ('season', 'Danger', 'Rift', 'Logos'):
        if not vocab: break
        for m in re.finditer(r'\b' + w + r'\b', prose):
            ctx = prose[max(0, m.start()-40):m.end()+40].replace('\n', ' ')
            if w == 'Logos' and ('Foundry' in ctx or 'system' in ctx or 'initial' in ctx): continue
            if w == 'Danger' and re.search(r'Danger Everywhere|Wide Area Danger', ctx): continue   # book Special names
            if w == 'season' and not re.search(r'season (one|two|three|\d|finale|arc|premiere|of play)|(first|second|third|next|last|the) season\b(?! implants)|season-long', ctx, re.I):
                continue   # a calendar, weather or fashion season, not a Series (BC-136)
            err(p, f'forbidden term `{w}`: …{ctx}…')
    # `case` (BC-136): flag only where it reads as a scenario-word for a Job, never the container or the idiom.
    SCENARIO = r'(work(ing|s|ed)? (a|the|this|that|his|her|their|my|our|its) cases?|on the case|cold cases?|case files?|(solv|crack|clos)(e|ed|es|ing) (a|the|this|that) case|becomes? a case|cases? (too|nobody|that nobody|no one|for the)|(missing|open|old|last|next|first|new|same) cases? (nobody|that|which|he|she|they|worth)|a case (nobody|that nobody|worth|to)|case ?loads?|caseworker)'
    CONTAINER = r'((in|into|inside|out of|from|carried in|carry|rides in|sits in|opens?|opened|open|unopened|sealed|seal|lid of|handle of|latch of|close|closed|shut|lock|locked|drop|dropped|put|left|found|stolen|lost|hold|holds|holding|with|and) (a|the|this|that|his|her|their|its|one|every|each|any|no|another) (hard-?shell |sealed |locked |steel |foam |warm-handled |second |sample |dose |lens |gun |brief|carry(ing)? |road |glass |display |shipping |transit |instrument |response-kit |weather-?)?cases?\b|cases? (came|come|comes) back|cases? (of|full of|number|lid|handle|latch|strap|foam|they came for|itself)|(dose|lens|brief|weather-?|hard-?shell|gun|carry(ing)?|road|glass|display|sample|shipping|transit|instrument|response-kit|crate) ?cases?|(stretch|cut|invoiced by|moves?|moving|moved|hand(ed)?|deliver(ed|s)?|left|opens?) (a|the|this|that|his|her|their|its) case|a van and a case|van, a case|what is in the case|in a case,|a case, (a|an|the)|cases? (in|on|at|by|to|from) (the|a|his|her|their|its))'
    for m in (re.finditer(r'\b[Cc]ases?\b', prose) if vocab else []):
        word = m.group(0); ctx = prose[max(0, m.start()-70):m.end()+70].replace('\n', ' '); low = ctx.lower()
        before = prose[max(0, m.start()-40):m.start()]
        if word[0] == 'C' and not re.search(r'[.!?]\s+$|^\s*$|[|>»›]\s+$', before):
            if re.search(r'\*[^*\n]*$|-$', before): continue                                       # a Special or kit title in emphasis, or a hyphenated name (Extreme-Case)
            if re.search(r'\b(The|A|Open|Opens|Closed|Cold|Missing|Recruitment|Extreme|Hard)\s*$', before): continue   # Title Case phrase
            warn(p, f'`{word}` capitalised as a term — a Job? …{ctx}…'); continue
        if re.search(CONTAINER, low) and not re.search(r'case files?|work(ing|s|ed)? (a|the) case|on the case', low): continue
        if re.search(r'(in any case|in case|case by case|case-by-case|lower-case|upper-case|kebab-case|title-case|sentence-case|worst case|best case|in which case|in (this|that|every|either|our|my|his|her|their) case|in the case of|a case of|a case for|the case for|make(s|ing)? the case|made the case|whatever the case|use case|edge case|extreme[- ]cases?|special case|rare case|(is|was|not|as) the case|the case that)', low): continue
        if re.search(r'\b(I|we|they|you|he|she|to|and|will|would|could|should|must|then)\s+case\s+(every|each|the|a|this|that|out|it|them|both)\b', ctx): continue   # verb: to case a room
        if re.search(SCENARIO, low):
            warn(p, f'`{word}` reads as a Job: …{ctx}…')
    for m in (re.finditer(r'\bMist\b', prose) if vocab else []):
        ctx = prose[max(0, m.start()-30):m.end()+30].replace('\n', ' ')
        if 'Mist Engine' in ctx or 'City of Mist' in ctx or 'mist-hud' in ctx or 'Legend in the Mist' in ctx: continue
        err(p, f'forbidden term `Mist`: …{ctx}…')
    if ps:
        for m in re.finditer(r'\bsplats?\b', prose, re.I):
            ctx = prose[max(0, m.start()-40):m.end()+40].replace('\n', ' ')
            if '02-splats' in ctx or 'splat:' in ctx or 'Splat:' in ctx: continue
            warn(p, f'`splat` in player-safe prose: …{ctx}…')
    tao_ok = '[TAO-REINTERPRETED]' in prose or 'TAO-REINTERPRETED' in flags
    for m in (re.finditer(r'\b(Mythoi|Conjurations?|legends?|Avatars?|Sources?|Mythos)\b', prose) if vocab else []):
        w = m.group(1); ctx = prose[max(0, m.start()-45):m.end()+45].replace('\n', ' ')
        low = ctx.lower()
        mech = ('mythos-os' in low or 'mythos theme' in low or 'mythos categor' in low or 'mythos kit' in low or 'mythos tag' in low or 'mythos content' in low or 'exposure' in low or 'self themes' in low or 'strip the source' in low
                or 'mythos power set' in low or 'mythos themebook' in low or 'themebook' in low or 'essence' in low
                or 'legend-mythoi' in low or 'legend in the mist' in low or 'no legend' in low or 'not a legend' in low or 'never a legend' in low
                or 'not legend' in low or 'no mythos' in low or 'legend language' in low or 'legend re-enact' in low
                or 'mythos (' in low or 'mythos,' in low or 'mythos or' in low or 'mythos /' in low or '/ mythos' in low or 'mythos)' in low
                or 'source:' in low or 'source-touched' in low or 'source-sensitive' in low or 'open source' in low or 'the source of' in low
                or 'sourcebook' in low or 'same source' in low or 'different source' in low or 'source unto' in low or 'a source' in low
                or 'sources' in low and 'tao' in low or 'sourced' in low or 'source of' in low or 'source is' in low or 'source that' in low
                or 'source (' in low or 'source and' in low or 'source' in low and ('reinterpret' in low or 'gateway' in low or 'bible' in low or 'brief' in low or 'plan' in low)
                or 'avatar' in low and ('essence' in low or 'conduit' in low or 'cyberspace' in low or 'impersonal' in low or 'tao' in low or 'cr-8' in low or 'cr-11' in low)
                or 'legend' in low and ('tao' in low or 'brief' in low or 'bible' in low or 'plan' in low or 'style-guide' in low or 'mythos' in low or 'reinterpret' in low or 'cr-' in low)
                or 'conjuration' in low and ('tao' in low or 'brief' in low or 'reinterpret' in low or 'plan' in low or 'strip' in low or 'no ' in low)
                or 'mythos' in low and ('tao' in low or 'brief' in low or 'bible' in low or 'plan' in low or 'reinterpret' in low or 'cr-' in low or 'category' in low or 'noise' in low or 'self' in low or 'legend' in low or 'book' in low or 'core p' in low or 'foundry' in low))
        if mech or tao_ok: continue
        warn(p, f'`{w}` outside a mechanical or [TAO-REINTERPRETED] context: …{ctx}…')

    # --- splat canon (Plan C.3)
    splatty = fm.get('splat') if isinstance(fm.get('splat'), str) else ''
    if p.startswith(('02-splats/vampire/', '02-splats/werewolf/')) or splatty in ('vampire', 'werewolf'):
        for m in re.finditer(r'\b(sunlight|stake|garlic|silver|holy water|crucifix)\b', prose, re.I):
            ctx = prose[max(0, m.start()-40):m.end()+40].replace('\n', ' ')
            if re.search(r'never|not |replace|instead|absent|no ', ctx, re.I): continue
            err(p, f'classic weakness word `{m.group(1)}`: …{ctx}…')
    if p.startswith('02-splats/hunter/') and ty in ('theme-kit', 'character-trope', 'pc-special'):
        for m in re.finditer(r'\b(sculpt\w*|bio-?manipulat\w*|gene[ -]?mod\w*)\b', prose, re.I):
            ctx = prose[max(0, m.start()-50):m.end()+50].replace('\n', ' ')
            if re.search(r'\b(no|not|never|none|neither|nor|without|off-limits|forbid|forbidden|line|cannot|can\'t|permits|rule|table|line between|Sculpted\b|entertainer)', ctx, re.I): continue
            err(p, f'hunter kit mentions `{m.group(1)}`: …{ctx}…')
    for m in re.finditer(r'\bTao (wants|chooses|demands|decides|wills|favou?rs|judges|answers|listens|knows|cares|refuses|allows|grants|asks|calls|speaks|hungers|desires|intends|punishes|rewards)\b', prose):
        ctx = prose[max(0, m.start()-90):m.end()+60].replace('\n', ' ')
        if re.search(r'never|not |no |defect|forbid|nothing', ctx, re.I): continue
        err(p, f'Tao given a will: …{ctx}…')

# --- player-safe links (Plan C.8, BC-175): a player_safe: true file may link only to player_safe: true files
base_ps = {os.path.basename(q)[:-3]: fm_by_path[q].get('player_safe') for q in fm_by_path}
for p, tgts in ps_links.items():
    for tgt in sorted(tgts):
        if tgt in base_ps and base_ps[tgt] is not True:
            err(p, f'player-safe file links MC-only [[{tgt}]] (Plan C.8)')

# --- report
n_err = sum(len(v) for v in errors.values()); n_warn = sum(len(v) for v in warnings.values())
print(f'Neon Black validate — {len(files)} files ({len([f for f in files if not f.startswith("99-templates/")])} content + templates)')
print('types:', ', '.join(f'{k}={v}' for k, v in sorted(stats.items())))
kits = stats['theme-kit'] + stats['crew-kit']
print(f'kits (theme+crew)={kits}  challenges={stats["challenge"]}  power-sets={stats["power-set"]}  npcs={stats["npc"]}  '
      f'districts={len([p for p in fm_by_path if p.startswith("05-megacity/districts/")])}  key-players={stats["key-player"]}  loadout={stats["loadout-item"]}')
print(f'ERRORS: {n_err} in {len(errors)} files   WARNINGS: {n_warn} in {len(warnings)} files')
for p in sorted(errors):
    print(f'\nERROR {p}')
    for m in errors[p]: print('   -', m)
if SHOW_WARN:
    for p in sorted(warnings):
        print(f'\nWARN {p}')
        for m in warnings[p]: print('   -', m)
sys.exit(1 if n_err else 0)
