lst=eval(input())
n,m=eval(input())
if len(lst)>=m>=n>=0:
    del lst[n:m]
    print(lst)
else:print("error")
