a = eval(input())
n,m = eval(input())
i = a.index(n)
d = a.index(m)
a[i],a[d] = a[d],a[i]
print(a)
