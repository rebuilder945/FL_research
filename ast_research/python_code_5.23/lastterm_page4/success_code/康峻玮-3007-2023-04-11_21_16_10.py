lst=list(input())
n,m=eval(input())
if len(lst) >= m+1 and len(lst) >= n+1:
    del lst[n,m]
    print(lst)
else:
    print("error")


