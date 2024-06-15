a=list(map(str.input().split()))
n,m=map(eval,input().split())
b=a[n]
a[n]=a[m]
a[m]=b
print(a)
