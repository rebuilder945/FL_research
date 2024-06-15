a = eval(input())
b = a[::-1]
c = []
for x in b:
    if x not in c:
        c.append(x)
print(c)
