lst = eval(input())
n,m=eval(input())
if len(lst)>=m>=n>=0:
    del lst[n:m-1]
    print(lst)
else:
    print("error")
