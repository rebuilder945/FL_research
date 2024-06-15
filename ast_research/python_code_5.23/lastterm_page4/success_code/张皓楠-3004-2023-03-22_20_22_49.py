a = eval(input())
b = []
c = []
for i in a:
    b.append(i)
for i in a:
    for x in range(2,i):
        if i%x==0:
            c.append(i)
c.append(0)
c.append(a)
for i in c:
    if i in b:
        b.remove(i)
print(b)
