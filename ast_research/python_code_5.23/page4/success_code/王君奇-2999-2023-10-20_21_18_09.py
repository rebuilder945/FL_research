x=input().split(' ')
m,n=list(map(int,input().strip().split()))
x[m],x[n]=x[n],x[m]
print(x)
