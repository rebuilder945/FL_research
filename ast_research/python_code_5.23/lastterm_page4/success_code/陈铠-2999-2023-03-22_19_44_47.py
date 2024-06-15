a=list(input())
n,m=eval(input).split(",")
b=a[n]
c=a[m]
a[n]=c
a[m]=b
print(a)
