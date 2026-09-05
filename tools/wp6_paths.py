#!/usr/bin/env python3
"""WP6 step 7: rewrite stale pre-rename file paths (BC-125) in prose and register `Where` columns.
Only literal old paths are touched; wikilinks were rewritten by wp6_rename.py."""
import os, re, glob
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SPLATS = {'vampire': 'bloodware', 'werewolf': 'howlers', 'mage': 'casters', 'changeling': 'doppels', 'hunter': 'baselines'}
KPS = ['corp-a', 'corp-b', 'corp-c', 'upstart', 'syndicate', 'government', 'tao-society', 'packs', 'changeling-cells', 'fence-network']
MAP = {'05-megacity/overview.md': '05-megacity/palisade.md',
       '03-self-kits/README.md': '03-self-kits/self-kits-index.md', '04-crew/README.md': '04-crew/crew-index.md',
       '08-challenges/README.md': '08-challenges/challenges-index.md', '09-loadout/README.md': '09-loadout/loadout-index.md',
       '04-crew/motivations.md': '04-crew/crew-motivations.md',
       '06-key-players/tao-society/challenges/wuji-operative.md': '06-key-players/tao-society/challenges/wuji-operative-challenge.md',
       '08-challenges/custom/anti-tao-countermeasure.md': '08-challenges/custom/anti-tao-countermeasure-challenge.md'}
for s, n in SPLATS.items():
    MAP[f'02-splats/{s}/overview.md'] = f'02-splats/{s}/{n}.md'
    MAP[f'02-splats/{s}/theme-kits/existing-kits.md'] = f'02-splats/{s}/theme-kits/{s}-existing-kits.md'
for k in KPS:
    MAP[f'06-key-players/{k}/overview.md'] = f'06-key-players/{k}/{k}.md'
    MAP[f'06-key-players/{k}/membership.md'] = f'06-key-players/{k}/{k}-membership.md'
    MAP[f'06-key-players/{k}/challenges/reuse.md'] = f'06-key-players/{k}/challenges/{k}-reuse.md'
# generic patterns used in register prose
GENERIC = [(r'02-splats/<splat>/overview\.md', '02-splats/<splat>/<setting-name>.md'),
           (r'02-splats/<splat-slug>/overview\.md', '02-splats/<splat-slug>/<setting-name>.md'),
           (r'06-key-players/\*/overview\.md', '06-key-players/*/<kp-slug>.md'),
           (r'06-key-players/<kp-slug>/overview\.md', '06-key-players/<kp-slug>/<kp-slug>.md'),
           (r'06-key-players/<kp>/overview\.md', '06-key-players/<kp>/<kp>.md'),
           (r'theme-kits/existing-kits\.md', 'theme-kits/<splat>-existing-kits.md'),
           (r'challenges/reuse\.md', 'challenges/<kp-slug>-reuse.md'),
           (r'06-key-players/\*/membership\.md', '06-key-players/*/<kp-slug>-membership.md'),
           (r'06-key-players/<kp-slug>/membership\.md', '06-key-players/<kp-slug>/<kp-slug>-membership.md'),
           (r'`membership\.md`', '`<kp-slug>-membership.md`'), (r'`reuse\.md`', '`<kp-slug>-reuse.md`')]
files = [p for p in glob.glob('**/*.md', recursive=True)
         if '/' in p and not p.startswith(('ref/', 'tools/', '.git/', '00-meta/additions/', '99-templates/'))
         and p != '00-meta/changelog.md']   # the changelog is history and keeps the paths of its day
changed = 0
for p in files:
    t = open(p, encoding='utf-8').read(); t0 = t
    for a, b in sorted(MAP.items(), key=lambda kv: -len(kv[0])):
        t = t.replace(a, b)
    if p.startswith("00-meta/") and p != "00-meta/changelog.md":
        for a, b in GENERIC:
            t = re.sub(a, b, t)
    if t != t0:
        open(p, 'w', encoding='utf-8').write(t); changed += 1; print('rewrote', p)
print('files changed:', changed)
