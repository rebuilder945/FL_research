lst=eval(input())
n,m=eval(input())
n<=m
if n in lst and m in lst:
    del lst[n]
    print(lst)
else:
    print("error")

