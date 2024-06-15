a = list(eval(input()))
b = a.copy()
b.sort()
for i in a:
    if i==b[0] or i==b[-1]:
        a.remove(i)
print(a)
