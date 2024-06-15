instr=input()
counter={}
for s in instr.split():
    counter[s]=counter.get(s,0)+1
maxcount=max(counter.values())
maxstr=sorted ([s for s in counter if counter[s]==maxcount])
for s in maxstr:
    print(s,maxcount)
