a=eval(input())
b=[]
for i in a:
    for j in i:
        b.append(j)
b.sort()
c=[]
for x in b:
    if x not in c:
        c.append(x)
for i in c:
    print(i+","+str(b.count(i)))


