ls=eval(input())
n,m=eval(input())
if n > m:
    print('error')
elif n==m:
    print(ls)
else:
    for i in range(n,m):
        del ls[i]
    print(ls)
