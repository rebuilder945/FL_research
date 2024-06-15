a=input().split()
z=input()
y=z.strip()
n=int(y[0])
m=int(y[2])
b=a[n]
c=a[m]
a[n]=c
a[m]=b
print(a)

