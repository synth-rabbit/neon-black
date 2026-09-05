import re, os
os.chdir('/home/claude/neon-black')
PK = ['WP2-vampire','WP2-werewolf','WP2-mage','WP2-changeling','WP2-hunter','WP3','WP4-trio1','WP4-trio2','WP4-trio3','WP5']
LINKFIX = {
 'WP2-vampire': [('[[overview', '[[bloodware'), ('[[existing-kits', '[[vampire-existing-kits')],
 'WP2-werewolf': [('[[overview', '[[howlers'), ('[[existing-kits', '[[werewolf-existing-kits')],
 'WP2-mage': [('[[overview', '[[casters'), ('[[existing-kits', '[[mage-existing-kits')],
 'WP2-changeling': [('[[overview', '[[doppels'), ('[[existing-kits', '[[changeling-existing-kits')],
 'WP2-hunter': [('[[overview', '[[baselines'), ('[[existing-kits', '[[hunter-existing-kits')],
 'WP3': [('[[motivations]]', '[[crew-motivations]]')],
 'WP4-trio1': [],
 'WP4-trio2': [('[[overview|Palisade]]', '[[palisade|Palisade]]')],
 'WP4-trio3': [('[[wuji-operative]]', '[[wuji-operative-challenge]]')],
 'WP5': [('[[anti-tao-countermeasure]]', '[[anti-tao-countermeasure-challenge]]')],
}
def sections(text):
    body = text.split('\n---\n', 1)[1] if text.startswith('---') else text
    parts = re.split(r'^## (.+)$', body, flags=re.M)
    out = {}
    for i in range(1, len(parts), 2):
        out[parts[i].strip()] = parts[i+1].strip('\n')
    return out
def demote(s):
    return re.sub(r'^### ', '#### ', s, flags=re.M)
reg = {'names': [], 'bc': [], 'oq': [], 'cr': [], 'cl': []}
for pk in PK:
    t = open(f'00-meta/additions/{pk}.md').read()
    for a, b in LINKFIX[pk]:
        t = t.replace(a, b)
    s = sections(t)
    def sec(key):
        for k in s:
            if k.lower().startswith(key): return demote(s[k])
        return ''
    reg['names'].append((pk, sec('names')))
    reg['bc'].append((pk, sec('build choices')))
    reg['oq'].append((pk, sec('open questions')))
    reg['cr'].append((pk, sec('conflicts')))
    reg['cl'].append((pk, sec('changelog')))
def append(path, items, heading_fmt):
    t = open(path).read().rstrip('\n') + '\n'
    for pk, body in items:
        if not body.strip(): continue
        t += f'\n{heading_fmt.format(pk=pk)}\n\n{body}\n'
    open(path, 'w').write(t)
append('00-meta/names.md', reg['names'], '### Added by {pk} — merged by WP6 (all rows are *proposals*)')
append('00-meta/build-choices.md', reg['bc'], '### Added by {pk} — merged and renumbered by WP6')
append('00-meta/open-questions.md', reg['oq'], '### Added by {pk} — merged and renumbered by WP6')
append('00-meta/conflict-register.md', reg['cr'], '### Added by {pk} — merged and renumbered by WP6')
# changelog: newest first — insert after the H1 intro paragraph
cl = open('00-meta/changelog.md').read()
head, rest = cl.split('\n## ', 1)
block = ''
for pk, body in reversed(reg['cl']):
    if not body.strip(): continue
    body = re.sub(r'^#+ .*\n', '', body, flags=re.M)  # drop inner headings
    block += f'\n## 2026-09-03 — {pk} (merged from `00-meta/additions/{pk}.md` by WP6)\n\n{body.strip()}\n'
open('00-meta/changelog.md', 'w').write(head.rstrip('\n') + '\n' + block + '\n## ' + rest)
print('merged')
