a=eval(input())
n,m=int(input().split())
x=a[n]
y=a[m]
a[m]=x
a[n]=y
print(a)
