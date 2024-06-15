lst=eval(input())
n,m=eval(input())
if len(lst)>=m>n:
    del lst[n:m]
    print(lst)
else:print("error")
