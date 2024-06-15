a = eval(input())
b = a.copy()
for i in a:
    if i == 0:
        b.remove(i)
        b.append(0)
print(b)
