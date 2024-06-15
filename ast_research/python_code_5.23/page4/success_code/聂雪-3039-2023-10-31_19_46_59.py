a = eval(input())
a.sort()
m=a.count(a[0])
n=a.count(a[-1])
del a[0:m]
del a[-n:]
print(a)
