a=input().split(' ')
n,m=int(input())
c=a[n]
a[n]=a[m]
a[m]=c
print(a)
