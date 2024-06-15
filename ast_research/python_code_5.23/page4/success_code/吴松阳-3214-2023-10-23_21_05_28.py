a = eval(input())
b = a.copy()
for i in b:
    if i == 0:
        a.remove(i)
        a.append(i)
print(a)
