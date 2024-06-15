lst=eval(input())
n,m=eval(input())
if len(lst)-1>=m>=n>=0:
    lst[n:m]=[]
    print(lst)
else:
    print("error")
