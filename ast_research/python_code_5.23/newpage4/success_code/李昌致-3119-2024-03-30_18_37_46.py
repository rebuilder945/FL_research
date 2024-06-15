a = eval(input())
i = 0
while a.count(i) != 1:
    if i == len(a):
        break
    del a[i]
    i = i + 1
print(a)
