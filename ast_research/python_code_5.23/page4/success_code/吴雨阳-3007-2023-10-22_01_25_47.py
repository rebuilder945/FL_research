ls=eval(input())
n,m=eval(input())
if 0<=n<len(ls) and 0<=m<len(ls):
    for i in range(n,m):
        del ls[i]
    print(ls)
else:
    print('error')
