s=input().split()
a=input().split()
n,m=int(a[0]),int(a[1])
scopy=s.copy()
s[n]=scopy[m]
s[m]=scopy[n]
print(s)
