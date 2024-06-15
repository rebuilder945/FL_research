a=input().split(' ')
n,m=input()
c=a[n]
a[n]=a[m]
a[m]=c
print(a)
