ls=eval(input())
n,m=tuple(input().split())
a=ls[n]
b=ls[m]
ls[n]=b
ls[m]=a
print(ls)

