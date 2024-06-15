ls=eval(input())
n,m=eval(input())
if n>len(ls)-1 or m>len(ls)-1:
    print("error")
else:
    if n<=m:
        del ls[n:m]  #del删除
    else:
        del ls[m:n]
    print(ls)
