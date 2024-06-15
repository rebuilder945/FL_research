a = eval(input())
b = []
d = []
for x in a:
    for y in range(2, x):
        if x % y == 0:
            b.append(x)
            break
for c in a:
    if c not in b:
        d.append(c)
print(d)
