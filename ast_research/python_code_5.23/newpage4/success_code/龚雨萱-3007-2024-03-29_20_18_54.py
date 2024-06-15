lst=eval(input())
n,m=eval(input())
if n in lst and m in lst:
    del lst[n:m]
    print(lst)
else:
    print("error")
