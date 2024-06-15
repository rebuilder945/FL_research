n=eval(input())
a=range(n)
a=list(a)
del a[1]
del a[0]
a.append(1)
print(a)
