a = eval(input())
a.sort()
b = a.copy()
c = []
e = []
for i in range(len(a)):
    if a[i] not in c:
        c.append(a[i])
for x in range(len(c)):
    a.remove(c[x])
for x in range(len(b)):
    for z in range(len(a)):
        if a[z] not in b:
            e.append(a[z])
if e==[]:
    print("False")
else:
    print(e)
