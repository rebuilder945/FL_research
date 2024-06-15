lst=input().split(" ")
counts={}
counts2={}
for x in lst:
    counts[x]=counts.get(x,0)+1
lst2=list(counts.items())
lst2.sort(key=lambda x:x[1],reverse=True)
for k,v in counts.items():
    if v==lst2[0][1]:
        counts2[k]=v
lst3=list(counts2.items())
lst3.sort()
for i in lst3:
    print(i[0],i[1])
