lst=eval(input())
n,m=eval(input())
c=len(lst)-1
if m<=c:
    del lst[n:m]
    print(lst)
else:
    print("error")



