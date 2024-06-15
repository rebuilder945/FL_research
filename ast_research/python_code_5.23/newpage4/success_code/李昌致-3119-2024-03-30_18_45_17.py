a = eval(input())
i = 0
while i <= len(a) and a.count(a[i]) != 1:
    del a[i]
    i = i + 1
print(a)
