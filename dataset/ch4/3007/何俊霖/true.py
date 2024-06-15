x=list(eval(input()))
n,m=eval(input())
if (0<=n<=len(x)-1 and 0<=m<=len(x)):
    del x[n:m]
    print(x)
else:
    print("error")
