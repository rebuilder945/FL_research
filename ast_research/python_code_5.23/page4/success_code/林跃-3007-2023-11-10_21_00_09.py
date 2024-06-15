lst=eval(input())
n,m=eval(input())
c=len(lst)
if n>=c or m>=c:
    print("error")
else:
    del lst[n:m]
    print(lst)
