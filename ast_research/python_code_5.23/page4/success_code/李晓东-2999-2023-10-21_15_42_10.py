a = eval(input())
n,m = eval(input())
d = a.copy()
d[n] = a[m]
d[m] = a[n]
print(d)

