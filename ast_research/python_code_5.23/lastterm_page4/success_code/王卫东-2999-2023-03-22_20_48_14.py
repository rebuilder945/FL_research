a = input().split()
n,m = map(int,input().split())
s = a[n]
a[n]=a[m]
a[m]=s
print(a)
