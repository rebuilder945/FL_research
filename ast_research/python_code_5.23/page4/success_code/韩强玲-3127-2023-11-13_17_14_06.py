n = eval(input())
a = []
for i in range(1,n+1):
    if i not in a:
        a.append(i)
a.append(a[0])
del a[0]
print(a)
