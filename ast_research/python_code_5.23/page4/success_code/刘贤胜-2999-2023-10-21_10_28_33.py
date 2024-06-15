a=input().split()
n,m=map(int,input().split())
acopy=a.copy()
acopy[n]=a[m]
acopy[m]=a[n]
print(acopy)

