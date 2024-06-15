b = input().split()
b.reverse()
c = []
for i in range(len(b)):
    c.append(b.count(b[i]))
d = max(c)
e = []
for i in range(len(b)):
    if b.count(b[i])==d:
        e.append(b[i])
f = []
for x in e:
    if not x in f:
        f.append(x)
        f.sort(reverse=False)
for y in range(len(f)):
    print(f[y],d)
