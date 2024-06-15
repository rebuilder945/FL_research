a = eval(input())
b = []
c = []
for k in a:
    if k == 0:
        b.append(k)
    else:
        c.append(k)
print(c+b)
