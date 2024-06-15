lst=input()
n,m=eval(input())
if len(lst) <= m and len(lst) <= n:
    del lst[n,m]
    print(lst)
else:
    print("error")


