#!/usr/bin/env python3
"""WP6 step 1: slug-collision renames + link rewrites. Idempotent-ish; run once."""
import os, re, subprocess, sys
ROOT = '/home/claude/neon-black'
os.chdir(ROOT)

def mv(src, dst):
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        subprocess.run(['git', 'mv', src, dst], check=True)
        print('mv', src, '->', dst)

def set_slug(path, slug):
    t = open(path).read()
    t2 = re.sub(r'^slug: .*$', f'slug: {slug}', t, count=1, flags=re.M)
    assert t2 != t or f'slug: {slug}' in t, path
    open(path, 'w').write(t2)

def vault_files():
    out = []
    for root, dirs, files in os.walk('.'):
        if any(s in root for s in ['./.git', './ref', './.claude', './tools']):
            continue
        for f in files:
            if f.endswith('.md') and root != '.':
                out.append(os.path.join(root, f))
    return sorted(out)

def rewrite(pred, fn):
    """Apply fn(text)->text to every file where pred(path) is true."""
    for p in vault_files():
        if not pred(p):
            continue
        t = open(p).read()
        t2 = fn(t)
        if t2 != t:
            open(p, 'w').write(t2)
            print('  rewrote', p)

def relink(old, new, alias_default=None):
    """Return fn that rewrites [[old]] / [[old|x]] / [[old#y]] -> new."""
    pat = re.compile(r'\[\[' + re.escape(old) + r'(?=[\]|#])')
    def fn(t):
        return pat.sub('[[' + new, t)
    return fn

SPLATS = {'vampire': 'bloodware', 'werewolf': 'howlers', 'mage': 'casters', 'changeling': 'doppels', 'hunter': 'baselines'}
KPS = ['corp-a', 'corp-b', 'corp-c', 'upstart', 'syndicate', 'government', 'tao-society', 'packs', 'changeling-cells', 'fence-network']

# ---- 1. Megacity overview -> palisade
mv('05-megacity/overview.md', '05-megacity/palisade.md')
set_slug('05-megacity/palisade.md', 'palisade')
# every [[overview...]] outside 02-splats/ and 00-meta/additions/ means Palisade
rewrite(lambda p: not p.startswith('./02-splats') and not p.startswith('./00-meta/additions'),
        relink('overview', 'palisade'))

# ---- 2. Splat overviews -> setting name; existing-kits -> <splat>-existing-kits
for splat, name in SPLATS.items():
    d = f'02-splats/{splat}'
    mv(f'{d}/overview.md', f'{d}/{name}.md')
    set_slug(f'{d}/{name}.md', name)
    mv(f'{d}/theme-kits/existing-kits.md', f'{d}/theme-kits/{splat}-existing-kits.md')
    set_slug(f'{d}/theme-kits/{splat}-existing-kits.md', f'{splat}-existing-kits')
    def fn(t, name=name, splat=splat):
        t = relink('overview', name)(t)
        t = relink('existing-kits', f'{splat}-existing-kits')(t)
        return t
    rewrite(lambda p, d=d: p.startswith('./' + d), fn)

# ---- 3. Key Player overviews -> <kp>.md ; membership/reuse -> <kp>-membership / <kp>-reuse
for kp in KPS:
    d = f'06-key-players/{kp}'
    mv(f'{d}/overview.md', f'{d}/{kp}.md')
    set_slug(f'{d}/{kp}.md', kp)
    mv(f'{d}/membership.md', f'{d}/{kp}-membership.md')
    set_slug(f'{d}/{kp}-membership.md', f'{kp}-membership')
    mv(f'{d}/challenges/reuse.md', f'{d}/challenges/{kp}-reuse.md')
    set_slug(f'{d}/challenges/{kp}-reuse.md', f'{kp}-reuse')
    def fn(t, kp=kp):
        t = t.replace('See `membership.md` in this folder', f'See [[{kp}-membership]]')
        t = t.replace('See `reuse.md` in this folder', f'See [[{kp}-reuse]]')
        t = t.replace('see `reuse.md` in this folder', f'see [[{kp}-reuse]]')
        t = t.replace('see `membership.md` in this folder', f'see [[{kp}-membership]]')
        return t
    rewrite(lambda p, d=d: p.startswith('./' + d), fn)

# ---- 4. Per-folder READMEs -> <folder>-index ; crew motivations
mv('03-self-kits/README.md', '03-self-kits/self-kits-index.md'); set_slug('03-self-kits/self-kits-index.md', 'self-kits-index')
mv('04-crew/README.md', '04-crew/crew-index.md'); set_slug('04-crew/crew-index.md', 'crew-index')
mv('08-challenges/README.md', '08-challenges/challenges-index.md'); set_slug('08-challenges/challenges-index.md', 'challenges-index')
mv('09-loadout/README.md', '09-loadout/loadout-index.md'); set_slug('09-loadout/loadout-index.md', 'loadout-index')
mv('04-crew/motivations.md', '04-crew/crew-motivations.md')
def fn_misc(t):
    t = t.replace('[[../README|04-crew/README]]', '[[crew-index]]')
    t = t.replace('[[../motivations|04-crew/motivations]]', '[[crew-motivations]]')
    t = t.replace('[[crew-kits/existing-crew-kits]]', '[[existing-crew-kits]]')
    t = t.replace('[[crew-specials/existing-crew-specials]]', '[[existing-crew-specials]]')
    t = t.replace('[[crew-kits/scrape-by-together]]', '[[scrape-by-together]]')
    t = t.replace('[[crew-kits/we-take-the-city]]', '[[we-take-the-city]]')
    t = t.replace('[[crew-kits/we-owe-rook]]', '[[we-owe-rook]]')
    t = t.replace('[[README|see the index]]', '[[challenges-index|see the index]]')
    t = t.replace('[[00-breakout|07-jobs/00-breakout]]', '[[breakout|07-jobs/00-breakout]]')
    t = t.replace('[[00-breakout]]', '[[breakout]]')
    return t
rewrite(lambda p: True, fn_misc)
# 09-loadout/existing-catalog.md: [[README]] at line 15 refers to the loadout folder README (index)
def fn_loadout(t):
    return t.replace('[[README]]', '[[loadout-index]]')
rewrite(lambda p: p == './09-loadout/existing-catalog.md', fn_loadout)

# ---- 5. Duplicate slugs: Challenge gets -challenge suffix
mv('06-key-players/tao-society/challenges/wuji-operative.md', '06-key-players/tao-society/challenges/wuji-operative-challenge.md')
set_slug('06-key-players/tao-society/challenges/wuji-operative-challenge.md', 'wuji-operative-challenge')
rewrite(lambda p: p.startswith('./06-key-players'), relink('wuji-operative', 'wuji-operative-challenge'))
mv('08-challenges/custom/anti-tao-countermeasure.md', '08-challenges/custom/anti-tao-countermeasure-challenge.md')
set_slug('08-challenges/custom/anti-tao-countermeasure-challenge.md', 'anti-tao-countermeasure-challenge')
rewrite(lambda p: p.startswith('./08-challenges') or p.startswith('./09-loadout') or p.startswith('./06-key-players'),
        relink('anti-tao-countermeasure', 'anti-tao-countermeasure-challenge'))

# ---- 6. Templates: unique placeholder slugs
set_slug('99-templates/template-key-player.md', 'placeholder-key-player')
set_slug('99-templates/template-job.md', 'placeholder-job')
print('done')
