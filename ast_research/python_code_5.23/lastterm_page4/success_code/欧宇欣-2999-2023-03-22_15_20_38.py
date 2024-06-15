def change(y,m,n):
    y[m],y[n]=y[n],y[m]
    print(y)
sums=input()
m,n=eval(input())
y=sums.split()
change(y,m,n)
