a=input().split()
z=input()
y=" ".join(z)
n=int(y[0])
m=int(y[1])
b=a[n]
c=a[m]
a[n]=c
a[m]=b
print(a)

