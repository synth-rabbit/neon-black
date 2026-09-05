import re, os, collections
os.chdir('/home/claude/neon-black')
M = {}
def add(prefix, kind, n, start):
    for i in range(1, n+1):
        M[f'{kind}-{prefix}-{i}'] = f'{kind}-{start+i-1}'
    return start+n
# BC (WP5 already used BC-27..30 globally)
n = 31
n = add('WP2-vampire','BC',13,n); n = add('WP2-werewolf','BC',9,n); n = add('WP2-mage','BC',19,n)
n = add('WP2-changeling','BC',17,n); n = add('WP2','BC',8,n)  # hunter used BC-WP2-n
n = add('WP3','BC',4,n); n = add('WP4T1','BC',7,n); n = add('WP4-trio2','BC',8,n); n = add('WP4-trio3','BC',9,n)
BC_NEXT = n
# OQ
n = 22
n = add('WP2-vampire','OQ',2,n); n = add('WP2-mage','OQ',6,n); n = add('WP2-changeling','OQ',6,n)
n = add('WP3','OQ',1,n); n = add('WP4T1','OQ',6,n); n = add('WP4-trio2','OQ',4,n)
# trio3: 1 merges into the changeling "who makes Doppels" row
M['OQ-WP4-trio3-1'] = M['OQ-WP2-changeling-1']
M['OQ-WP4-trio3-2'] = f'OQ-{n}'; M['OQ-WP4-trio3-3'] = f'OQ-{n+1}'; n += 2
OQ_NEXT = n
# CR
n = 9
n = add('WP2-vampire','CR',1,n); n = add('WP2-mage','CR',2,n); n = add('WP2-changeling','CR',3,n)
n = add('WP4T1','CR',3,n); n = add('WP4-trio2','CR',1,n); n = add('WP4-trio3','CR',1,n)
CR_NEXT = n
print('next', BC_NEXT, OQ_NEXT, CR_NEXT)
# order keys longest first so BC-WP2-mage-1 is not eaten by BC-WP2-1 ; also handle "-1" vs "-10"
keys = sorted(M, key=len, reverse=True)
pat = re.compile('|'.join(re.escape(k) for k in keys) + r'(?!\d)')
hits = collections.Counter()
for root, dirs, fs in os.walk('.'):
    if any(s in root for s in ['./.git','./ref','./.claude','./tools','./00-meta/additions']): continue
    for f in fs:
        if not f.endswith('.md'): continue
        p = os.path.join(root, f); t = open(p).read()
        t2 = pat.sub(lambda m: (hits.update([m.group(0)]), M[m.group(0)])[1], t)
        if t2 != t: open(p, 'w').write(t2)
print(sum(hits.values()), 'replacements in', len(hits), 'ids')
import json; json.dump(M, open('tools/wp6_idmap.json','w'), indent=1)
