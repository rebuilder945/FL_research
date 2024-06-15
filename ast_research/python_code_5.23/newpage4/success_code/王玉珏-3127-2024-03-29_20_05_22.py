n=eval(input())
cubes=[i for i in range(1,n+1)]




x=[i+1 for i in range(n)]
for i in range(n-1):
    x[i]=x[i+1]
x[n-1]=1
print(x)
