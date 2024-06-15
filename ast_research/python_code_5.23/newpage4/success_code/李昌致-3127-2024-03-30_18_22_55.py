n = eval(input())
a = [x for x in range(1,n+1)]
del a[0]
a.append(1)
print(a)
