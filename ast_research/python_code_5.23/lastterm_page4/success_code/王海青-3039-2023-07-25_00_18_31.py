a=eval(input())
n=max(a)
m=min(a)
a.remove(n)
a.remove(m)
a.sort()
del a[0]
del a[-1]
print(a)
