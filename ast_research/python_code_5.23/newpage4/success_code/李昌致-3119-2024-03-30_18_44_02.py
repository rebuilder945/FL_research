a = eval(input())
i = 0
while a.count(a[i]) != 1 and i <= len(a):
    del a[i]
    i = i + 1
print(a)
