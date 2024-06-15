a = eval(input())
b = a[:]
for i in b:
    c = a.count(i)
    if c != 1:
        a.remove(i)
print(a)
