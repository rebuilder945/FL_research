a=list(input())
n,m=eval(input())
b=a[n]
c=a[m]
a[n]=c
a[m]=b
print(a)
