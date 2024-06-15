x=list(eval(input()))
n,m=eval(input())
if -len(x)<=n<=-1 or 0<=n<=len(x)-1:
    y=[]
    for i in range(0,m):
        y.append(x[n])
    e=x+y
    print(e)
else:
    print("error")
