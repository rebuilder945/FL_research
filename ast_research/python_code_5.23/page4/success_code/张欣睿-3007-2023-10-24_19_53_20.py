lst = eval(input())
n,m = eval(input())
if n <= m:
    del lst[n:m]
    print(lst)
else:
    print("error")
