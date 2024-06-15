a = eval(input())
for i in a[0:]:
    if a.count(i) > 1:
        a.remove(i)
print(a)
