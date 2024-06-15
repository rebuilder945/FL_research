list1=list(input().split())
d={}
for i in list1:
    d[i]=list1.count(i)
    a=0
    b=max(d.values())
    c=[]
for i in d:
    if d[i]==b:
        c.append(i)
        c.sort()
for i in c:
    print("{} {}".format(i,b)
