a=input().split(" ")
n,m=input().split( )
n=int(n)
m=int(m)
temp=a[n]
a[n]=a[m]
a[m]=temp
print(a)
