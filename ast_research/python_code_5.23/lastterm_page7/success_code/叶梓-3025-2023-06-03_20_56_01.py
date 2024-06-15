lst=list(input().split())
count={}
for x in lst:
    count[x]=count.get(x,0)+1 #
vmax=max(count.values())
kmax=[]
for i in count:
    if count[i]==vmax:
        kmax.append(i)
kmax.sort()
for y in kmax:
    print(y,vmax)
