n = eval(input())
a = range(1,n+1)
a = list(a)
b = a[0]
del a[0]
a.append(b)
print(a)
