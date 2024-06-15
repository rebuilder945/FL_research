from logging import error


ls=eval(input())
n,m=eval(input())
if m>len(ls):
    print(error)
else:
    for i in range(n,m):
        del ls[i]
    print(ls)
