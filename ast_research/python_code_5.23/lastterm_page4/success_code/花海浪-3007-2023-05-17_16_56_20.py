lst=eval(input())
n,m=eval(input())
if n>len(lst)-1 or m>len(lst)-1:
    print("error")
else:
    if n<=m:
        del lst[n:m]
    else:
        del lst[n:m:-1]
    print(lst)

