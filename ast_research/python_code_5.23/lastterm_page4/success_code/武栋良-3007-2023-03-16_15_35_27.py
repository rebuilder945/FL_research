lst = eval(input())
n,m = eval(input())
if n<=m:
    n,m = n,m
else:
    n,m = m,n
if m<len(lst):
    for i in range(n,m):
        del lst[i]
        print(lst)
else:
    print("error")

