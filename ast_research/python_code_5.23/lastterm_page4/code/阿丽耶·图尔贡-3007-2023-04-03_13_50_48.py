L = eval(input())
n,m = eval(input())
if n>len(L)-1 or m>len(L)-1:
    print(error)
else:
    if n<=m:
        del[n:m]
    else:
        del[m:n:-1]
