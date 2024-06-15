lst=list(input()).split(' ')
d={}
for i in lst:
    d[i]=lst.count(i)
x=0
b=max(d.values())
c=[]
for i in d:
    if d[i]==b:
        c.append(i)
c.sort()
for i in c:
    print("{},{}".format(i,b))
