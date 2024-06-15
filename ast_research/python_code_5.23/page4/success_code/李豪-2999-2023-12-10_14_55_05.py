def change(y,m,n):
    y[m],y[n]=y[n],y[m]
    print(y)
sums=input()
m,n=list(map(int,input().strip().split()))
y=sums.split()
change(y,m,n)    
