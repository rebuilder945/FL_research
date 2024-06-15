lst = eval(input())
n,m = eval(input())
if n <= m:
    for i in range(n,m):
        del lst[n:m]
    print(lst)
else:
    print("error")
