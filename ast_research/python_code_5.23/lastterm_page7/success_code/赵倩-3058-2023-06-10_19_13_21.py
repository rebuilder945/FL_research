a=input() or "q"
d={}
l=[]
while a!="q":
    l.append(a)
    b=l.count(a)
    d[a]=b
    a=input() or "q"
c=[]
for i in d:
    c.append(d[i])
m=max(c)
for i in d:
    if d[i]==m:
        print(i,m)
    

























