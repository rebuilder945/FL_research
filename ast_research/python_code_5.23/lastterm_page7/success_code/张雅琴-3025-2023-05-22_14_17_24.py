q=input().slpit()
p={}
for i in q:
    p[i]=q.count(i)
a=0
b=max(p.values())
c=[]
for i in p:
    if p[i]==b:
        c.append(i)
c.sort()
for j in c:
    print("{} {}".format(j,b))

