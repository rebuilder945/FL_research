a=list(input().split(' '))
n,m=input().split(' ')
n=int(n)
m=int(m)
b=a.copy()
b[n]=a[m]
b[m]=a[n]
print(b)
