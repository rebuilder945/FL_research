a=input().split(' ')
n,m=input().split(' ')
n=int(n)
m=int(m)
b=a[n]
a[n]=a[m]
a[m]=b
print(a)

