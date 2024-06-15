a = eval(input())
a.sort()
m=int(a.count(a[0]))
n=int(a.count(a[-1]))
del a[0,m+1]
del a[-1,-1-n]
print(a)
