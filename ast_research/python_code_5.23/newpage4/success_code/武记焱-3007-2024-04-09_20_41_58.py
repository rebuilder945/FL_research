lst=list(eval(input()))
n,m=eval(input())
if n<=m and m<=(len(lst)-1):
    del lst[n:m]
    print(lst)
else:
    print("error")
