a = eval(input())
i = 0
while i < len(a):
    if a.count(a[i]) != 1:
        del a[i]
    if a.count(a[i]) == 1:
        i = i + 1
    else:
        del a[i]
print(a)
