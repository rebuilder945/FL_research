lst=eval(input())
n,m=eval(input())
L=len(lst)
if n<=m and m<L:
    del lst[n:m]
    print(lst)
else:
    print("error")
