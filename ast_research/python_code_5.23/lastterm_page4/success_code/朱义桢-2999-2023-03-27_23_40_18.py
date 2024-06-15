a=input().split(" ")
d=input().split("")
n=int(d[0])
m=int(d[1])
b=a[n]
c=a[m]
a[n]=c
a[m]=b
print(a)
