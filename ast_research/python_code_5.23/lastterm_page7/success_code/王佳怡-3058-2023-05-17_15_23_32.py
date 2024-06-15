a=input() or "q"
counts={}
while(a!="q"):
    counts[a]=counts.get(a,0)+1
    a=input() or "q"
l=list(counts.items())
l.sort(key=lambda x:x[1],reverse=True)
print("{} {}".format(l[0][0],l[0][1]))
