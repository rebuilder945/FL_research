a = eval(input())
b = a[:]
c = []
for x in a:
    if a != 0:
        c.append(a)
    if a == 0:
        del a
d = c + [0]*(len(b)-len(a))
print(d)

