from re import L


L = eval(input())
n,m = eval(input())
if n>len(L)-1 or m>len(L)-1:
    print(error)
else:
    if n<=m:
        del L[n:m]
    else:
        del L[m:n:-1]
