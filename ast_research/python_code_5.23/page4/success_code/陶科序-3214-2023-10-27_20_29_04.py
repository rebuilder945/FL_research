a = eval(input())
b = []
for i in a:
    if i != 0:
        b.append(i)
    else:
        continue
d = a.count(0)
for i in range(d):
    b.append(0)
print(b)
