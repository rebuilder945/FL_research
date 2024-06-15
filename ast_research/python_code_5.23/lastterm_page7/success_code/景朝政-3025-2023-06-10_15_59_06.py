a=list(input().split(' '))
d={}
for i in a:
    d[i]=a.count(i)
jishu=0
b=max(d.values())
c=[]
for i in d:
    if d[i]==b:
        c.append(i)
c.sort()
for i in c:
    print("{} {}".format(i,b))


