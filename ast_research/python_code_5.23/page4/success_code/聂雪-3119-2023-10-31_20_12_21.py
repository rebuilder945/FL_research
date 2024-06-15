a = eval(input())
x = a.copy()
for i in x:
    b = a.count(i)
    if b>=2:
        a.remove(i)
print(a)
