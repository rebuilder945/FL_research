l1 = eval(input())
a = max(l1)
b = min(l1)
c = []
for i in l1:
    if i != a and i != b:
        c.append(i)
print(c)

