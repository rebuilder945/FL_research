a = eval(input())
b = a.copy()
for i in  range(len(a)):
    if a[i] == 0:
        b.remove(a[i])
        b.append(0)
print(b)
