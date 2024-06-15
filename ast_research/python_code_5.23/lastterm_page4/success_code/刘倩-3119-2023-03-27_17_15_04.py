a = eval(input())
b = a.reverse()
c = []
for x in b:
    if x not in c:
        c.append(x)
print(c)
