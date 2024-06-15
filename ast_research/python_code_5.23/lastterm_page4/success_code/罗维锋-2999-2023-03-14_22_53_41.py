a=input().split('')
m,n=input().split('')
b=a[:]
m=int(m)
n=int(n)
a[m]=b[n]
a[n]=b[m]
print(a)

