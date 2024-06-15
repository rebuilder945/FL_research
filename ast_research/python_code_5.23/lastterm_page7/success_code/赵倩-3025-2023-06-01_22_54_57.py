a=input().split()
a.sort()
d={}
for x in a:
    if x in d:
        d[x]+=1
    else:
        d[x]=1
l=[]
for n in d:
    b=d[n]
    l.append(b)
c=max(l)
for x in d:
    if d[x]==c:
        print(x,c)

                    




