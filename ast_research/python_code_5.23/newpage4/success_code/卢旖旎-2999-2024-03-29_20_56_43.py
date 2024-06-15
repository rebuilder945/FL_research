a=list(input().split())
n,m=map(int,input().split())
b=a[:]
b[n]=a[m]
b[m]=a[n]
print(b)
