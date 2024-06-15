ls=input().split()
count={}
m=0
for x in ls:
    count[x]=count.get(x,0)+1
    if count[x]>m:
        m=count[x]
countlist=list(count.items())
countlist.sort()
for k,v in countlist:
    if v==m:
        print(k,v)


