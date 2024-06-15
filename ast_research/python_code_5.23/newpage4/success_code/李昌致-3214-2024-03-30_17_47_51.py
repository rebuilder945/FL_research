a = eval(input())
b = a.count(0)
c = []
for i in a:
    if i != 0:
        c.append(i)
    else:
        pass
print(c + [0]*b)
