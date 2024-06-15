a=list(input().split())
b=list(input().split())
c=a.copy()
n=int(b[0])
m=int(b[1])
c[n]=a[m]
c[m]=a[n]
print(c)
