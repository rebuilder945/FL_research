ls=input().split()
n,m=tuple(input().split())
n=int(n)
m=int(m)
a=ls[n]
b=ls[m]
ls[n]=b
ls[m]=a
print(ls)

