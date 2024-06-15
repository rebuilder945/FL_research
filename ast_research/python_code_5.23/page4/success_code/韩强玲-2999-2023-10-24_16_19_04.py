a = list(map(str,input().split()))
m,n = eval(input())
b = a.copy()
b[m] = a[n]
b[n] = a[m]
print(b)

