a = input() or "q"
b = []
while (a!="q"):
    b.append(a)
    a = input() or "q"
b.reverse()
c = []
for i in range(len(b)):
    c.append(b.count(b[i]))
d = max(c)
for i in range(len(b)):
    if b.count(b[i])==d:
        break
print(b[i],d)
