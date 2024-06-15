a=input().split()
n,m=eval(input())
acopy=a.copy()
acopy[n]=a[m]
acopy[m]=a[n]
print(acopy)

