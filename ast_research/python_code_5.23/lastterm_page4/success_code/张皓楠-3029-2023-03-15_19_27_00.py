a = list(eval(input()))
f = []
for i in a:
    e = str(i)
    f.append(e)
b = eval(input())
d = []
for i in range(len(b)):
    c = []
    c.append(a[i])
    c.append(b[i])
    d.append(c)
print(d)
