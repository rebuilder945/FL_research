a = input().split()
n,m = input().split()
a = list(a)
n = int(n)
m = int(m)
i = a.index(n)
d = a.index(m)
a[i],a[d] = a[d],a[i]
print(a)
