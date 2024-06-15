a=list(input().split())
m,n=map (int,input().split())
b=a[m]
a[m]=a[n]
a[n]=b
print(a)
