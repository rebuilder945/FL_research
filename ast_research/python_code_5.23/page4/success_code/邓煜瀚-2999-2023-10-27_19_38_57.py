a=input().split()
z=input()
y=z.split()
n=int(y[0])
m=int(y[1])
b=a[n]
c=a[m]
a[n]=c
a[m]=b
print(a)

