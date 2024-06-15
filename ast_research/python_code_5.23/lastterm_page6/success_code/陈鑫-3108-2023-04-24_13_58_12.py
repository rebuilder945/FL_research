a=eval(input())
b=[]
for i in range(len(a)):
    for x in range(len(a[i])):
        b.append(a[i][x])

c=[]
for i in range(len(b)):
    if b[i] not in c:
        c.append(b[i])
        c.sort()
d=[]

for i in range(len(c)):
    d.append(b.count(c[i]))
    print(c[i]+d[i])


