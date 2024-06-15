ls=eval(input())
n,m=eval(input())
if 0<n<=m<=len(ls):
    del ls[n:m]
    print(ls)
else:
    print("error")
