n=int(input())
a=list(range(1,n+1))
b=a[0]
del a[0]
a.append(b)
print(a)
