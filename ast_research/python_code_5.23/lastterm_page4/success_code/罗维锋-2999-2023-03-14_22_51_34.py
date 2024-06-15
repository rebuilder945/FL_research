a=input().split('')
m,n=input().split('')
b=a[:]
a[m]=b[n]
a[n]=b[m]
print(a)

