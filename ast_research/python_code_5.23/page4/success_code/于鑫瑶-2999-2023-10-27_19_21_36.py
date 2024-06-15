a=input().split()
n,m=eval(input())
c=a[m]
a[m]=a[n]
a[n]=c
print(a)


