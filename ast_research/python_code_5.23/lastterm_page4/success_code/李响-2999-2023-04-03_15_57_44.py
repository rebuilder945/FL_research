a =input().split(" ")
d= input().split(" ")
n,m = ",".join(d)
n = int(n)
m = int(m)
a[n],a[m] = a[m],a[n]
print(a)
print(d)

