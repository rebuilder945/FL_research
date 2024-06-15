a=input().split()
n,m=input().split()
c=a[int(n)]
a[int(n)]=a[int(m)]
a[int(m)]=c
print(a)
