a=input().split()
m,n = map(int,input().split())
b=a.copy()
a[m]=b[n]
a[n]=b[m]

print(a)

