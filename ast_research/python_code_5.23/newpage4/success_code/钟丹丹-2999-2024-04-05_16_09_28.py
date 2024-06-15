a=input().split()
l = input().split()
n=int(l[0])
m=int(l[1])
acopy=a.copy()
a[n]=acopy[m]
a[m]=acopy[n]
print(a)
