lst = list(input().split(","))
n,m = eval(input())
if n>len(lst)-1 or m>len(lst)-1:
    print(error)
else:
    if n<=m:
        del lst[n:m]
    else:
        del lst[m:n:-1]
