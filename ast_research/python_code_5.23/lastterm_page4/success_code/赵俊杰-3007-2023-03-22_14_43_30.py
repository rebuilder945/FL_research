ls=eval(input())
n,m=eval(input())
a=len(ls)
if 0<=n<=m<=a:
    del ls[n:m]
    print(ls)
else:
    print("error")
