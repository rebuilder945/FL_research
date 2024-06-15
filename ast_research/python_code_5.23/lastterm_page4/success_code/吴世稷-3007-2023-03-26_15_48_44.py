lst = eval(input())
n,m = eval(input())
if 0<=n<=(len(lst)-1) and 0<=m<=(len(lst)-1):
    for x in range(n,m):
        lst.pop(x)
    print(lst)
else:
    print("error")

