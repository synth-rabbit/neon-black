import os,re,collections,sys
files={}
for root,dirs,fs in os.walk('.'):
    if any(s in root for s in ['./.git','./ref','./.claude','./tools']): continue
    for f in fs:
        if f.endswith('.md') and root!='.':
            files.setdefault(f[:-3],[]).append(os.path.join(root,f))
links=collections.Counter(); where=collections.defaultdict(set)
for slug,ps in files.items():
    for p in ps:
        t=open(p).read()
        for m in re.finditer(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]',t):
            tgt=m.group(1).strip(); links[tgt]+=1; where[tgt].add(p)
for k,v in sorted(links.items(), key=lambda x:-x[1]):
    if k not in files and not k.startswith('assets/'):
        print(f"  {k}: {v}  {sorted(where[k])[:4]}")
dups={s:p for s,p in files.items() if len(p)>1}
print("DUP basenames:",dups)
