x=list(eval(input()))
n,m=eval(input())
if (0<=n<=len(x)-1 and 0<=m<=len(x)):
    e=x[n:m]
    print(e)
else:
    print("error")
