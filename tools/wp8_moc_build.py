#!/usr/bin/env python3
"""WP8: build or refresh the per-folder Maps of Content (BC-178). Appends/replaces a
'## Every file in this folder' section (one row per file, grouped by subfolder) in each MOC."""
import glob, re, yaml, os, subprocess, collections
MOCS = {'01-series':'series-index','02-splats':'splats-index','03-self-kits':'self-kits-index','04-crew':'crew-index',
        '05-megacity':'megacity-index','06-key-players':'key-players-index','07-jobs':'jobs-index','08-challenges':'challenges-index','09-loadout':'loadout-index'}
def rows(folder, moc):
    out = subprocess.run(['python3','tools/wp8_moc.py',folder],capture_output=True,text=True).stdout.splitlines()
    groups = collections.OrderedDict()
    for line in out:
        m = re.match(r'(\|.*\|)\s+<!-- (.*) -->$', line)
        row, sub = m.group(1), m.group(2)
        if f'[[{moc}]]' in row: continue
        groups.setdefault(sub, []).append(row)
    return groups
for folder, moc in MOCS.items():
    path = glob.glob(f'{folder}/**/{moc}.md', recursive=True)[0]
    t = open(path, encoding='utf-8').read()
    groups = rows(folder, moc)
    sec = ['## Every file in this folder', '', f'One row per file (this index excepted); *P* marks a `player_safe: true` file that may be handed to a player whole. Descriptions are drawn from each file\'s frontmatter.', '']
    for sub, rs in groups.items():
        sec.append(f'### `{sub}/`'); sec.append(''); sec.append('| File | Type | P | One line |'); sec.append('|---|---|---|---|'); sec.extend(rs); sec.append('')
    sec_text = '\n'.join(sec).rstrip('\n') + '\n'
    if '## Every file in this folder' in t:
        t = re.sub(r'## Every file in this folder.*?(?=\n## |\Z)', sec_text, t, flags=re.S)
    else:
        # insert before '## Canon and flags' if present, else append
        if '\n## Canon and flags' in t:
            t = t.replace('\n## Canon and flags', '\n' + sec_text + '\n## Canon and flags', 1)
        else:
            t = t.rstrip('\n') + '\n\n' + sec_text
    open(path, 'w', encoding='utf-8').write(t)
    print(path, sum(len(v) for v in groups.values()), 'rows')
