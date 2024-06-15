a = eval(input())
b = []
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    d = a.count(i)-1
    if d > 0:
        for x in range(d):
            a.remove(i)
print(a)


