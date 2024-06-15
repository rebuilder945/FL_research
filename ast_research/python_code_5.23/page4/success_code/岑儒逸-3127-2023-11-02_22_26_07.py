n=eval(input())
x=range(1,n+1)
x=list(x)
x.append(x[-1])
y=x.copy()
for i in range(0,n):
    x[i]=x[i+1]
x.remove(x[-1])
x[-1]=y[0]
print(x)
