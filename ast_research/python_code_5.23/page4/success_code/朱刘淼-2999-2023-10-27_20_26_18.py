def Change(y,m,n):y[m],y[n]=y[n],y[m]
sums=input()
m,n=list(map(int,input().strip().split()))
y=sums.split()
Change(y,m,n)
print(y)
