n = int(input())
a = [i for i in  range(1,n+1)]
b=a[0]

a.append(a[0])
del a[0]
print(a)

