a=input().split()
n,m=eval(input())
b=a[m]
a[n]=a[m]
a[m]=b
print(a)
