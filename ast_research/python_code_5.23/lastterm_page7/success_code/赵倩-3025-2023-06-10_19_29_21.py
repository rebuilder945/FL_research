a=input().split()
d={}
for i in a:
    b=a.count(i)
    d[i]=b
l=[]
for i in d:
    l.append(d[i])
m=max(l)
c=[]
for i in d:
    if d[i]==m:
        c.append([i,m])
c.sort()
for i in c:
    print(*i)




