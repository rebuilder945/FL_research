slist=input().split()
count={}
max=0
for x in slist:
    count[x]=slist.get(x,0)+1
    if count[x]>max:
        max=count[x]
countlist=list(count.items())
countlist.sort()
for k,v in countlist:
    if v==max:
        print(k,v)
