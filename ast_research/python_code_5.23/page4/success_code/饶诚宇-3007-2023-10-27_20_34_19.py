lst=eval(input().split())
n,m=eval(input())
if n<=m:
    lst.remove(n,m)
    print(lst)
else:
    print("error")

