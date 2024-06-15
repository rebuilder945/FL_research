ls = eval(input())
n,m = eval(input())
if n<=m:
    n,m = n,m
else:
    n,m = m,n
if m<len(ls):
    for i in range (n,m)：
        del ls[i]
    print(ls)
else:
    print("errror")

