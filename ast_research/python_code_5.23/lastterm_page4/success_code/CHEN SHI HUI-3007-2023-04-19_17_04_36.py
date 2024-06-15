lst=eval(input())
n,m=eval(input())
n<=m
if n in lst and m in lst:
    print(lst[:n]+lst[m:])
else:
    print("error")

