n=eval(input())
a=range(n+1)
a=list(a)
del a[1]
del a[0]
a.append(1)
print(a)
