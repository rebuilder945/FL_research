a=input().split(' ')
n,m=eval(input())
c=a[n]
a[n]=a[m]
a[m]=c
print(a)
