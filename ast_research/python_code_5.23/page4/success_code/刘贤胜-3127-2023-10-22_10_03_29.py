n=eval(input())
a=[x*1 for x in range(1,n+1)]
b=a.copy()
del a[0]
a.append(b[0])
print(a)

