ls=eval(input())
n,m=eval(input())
if n>len(ls)-1 or m>len(ls)-1:
    print("error")
else:
    if n<=m:
        del ls[n:m]
    else:
        del ls[n:m:-1]
    print(ls)
