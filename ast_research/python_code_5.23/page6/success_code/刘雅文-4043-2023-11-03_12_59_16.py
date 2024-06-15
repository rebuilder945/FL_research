a=eval(input())
b=[]
for x in a:
    for i in x:
        c=x.count(i)
        m=[]
        m.append(i)
        m.append(str(c))
        b.append(m)
for y in b[:]:
    d=b.count(y)
    if d>1:
        b.remove(y)
for j in b:
    print(','.join(j))
