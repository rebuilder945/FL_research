a = input().split()
b =a.copy()
n,m = input().split()
m=int(m)
n = int(n)
b[n] = a[m]
b[m] = a[n]
print(b)
