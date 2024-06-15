a=input().split(' ')
n,m=map(int,input().split())
c=a[n]
a[n]=a[m]
a[m]=c
print(a)
