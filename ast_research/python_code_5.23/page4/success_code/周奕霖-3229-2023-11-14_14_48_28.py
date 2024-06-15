a = eval(input())
a.sort()
b = []
for x in a:
    if a.count(x) == 1:
        b.append(x)
b = ",".join(str() for i in b)
print(b)


