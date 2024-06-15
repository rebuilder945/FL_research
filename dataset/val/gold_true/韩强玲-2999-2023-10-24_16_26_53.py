a = list(map(str,input().split()))
m,n = map(int,input().split())
b = a.copy()
b[m] = a[n]
b[n] = a[m]
print(b)

