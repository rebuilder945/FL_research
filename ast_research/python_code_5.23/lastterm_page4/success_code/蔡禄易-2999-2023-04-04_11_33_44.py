a = eval(input())
n,m = eval(input())
a = list(a)
n = int(n)
m = int(m)
i = a.index(n)
d = a.index(m)
a[i],a[d] = a[d],a[i]
print(a)
