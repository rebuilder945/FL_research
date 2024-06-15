lst = eval(input())
n,m = eval(input())
if n and m in range(len(lst)):
    del lst[n:m]
    print(lst)
else:
    print("error")
