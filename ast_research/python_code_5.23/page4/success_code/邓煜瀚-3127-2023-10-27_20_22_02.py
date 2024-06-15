n=eval(input())
a=[x for x in range(1,n)]
b=a[0]
del a[0]
a.append(b)
print(a)


