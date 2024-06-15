a=input().split(" ")
d=input().split("")
n=d[0]
m=d[1]
b=a[n]
c=a[m]
a[n]=c
a[m]=b
print(a)
