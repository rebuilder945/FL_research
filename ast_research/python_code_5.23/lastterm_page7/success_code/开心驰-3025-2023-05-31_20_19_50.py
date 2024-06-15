ans=input().split()
d={}
c=[]
for i in ans:
    d[i]=ans.count(i)
b=max(d.values())
for i in d:
    if d[i]==b:
        c.append(i)
        c.sort()
for i in c:
    print(i,b)

