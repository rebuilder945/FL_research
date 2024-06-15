str=input().split()
a={}
for x in str:
    a[x]=a.get(x,0)+1
c=list(a.items())
c.sort(key=lambda x:x[1],reverse=True)
d=[]
for x in range(len(c)):
    if c[x][1]==c[0][1]:
        d.append(c[x])
d.sort(key=lambda x:x[0],reverse=False)
for x in d:
    print(x[0],x[1])


