lst = eval(input())
n,m = eval(input())
a = len(lst)
if n and m in range(0,a+1):
    del lst[n:m]
    print(lst)
else:
    print("error")
