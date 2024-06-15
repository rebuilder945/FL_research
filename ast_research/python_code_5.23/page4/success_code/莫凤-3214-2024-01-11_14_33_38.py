a=eval(input())
n=a.count(0)
for x in range(n):
    del a[a.index(0)]
    a.append(0)
print(a)
