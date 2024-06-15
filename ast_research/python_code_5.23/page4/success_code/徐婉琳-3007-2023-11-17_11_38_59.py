c=eval(input())
n,m=eval(input())
k=len(c)
if 0<=n<=m<=k:
    del c[n:m]
    print(c)
else:
    print('error')

