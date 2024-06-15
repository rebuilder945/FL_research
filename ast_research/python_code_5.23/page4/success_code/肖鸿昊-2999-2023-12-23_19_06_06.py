a=input().split()
m,n=eval(input())
b=a[m]
a[m]=a[n]
a[n]=b
print([a])
