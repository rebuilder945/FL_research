lst=eval(input())
n,m=eval(input())
a=len(lst)-1
if n<a and m<=a and n<m:
    del lst[n:m]
    print(list(lst))
else:
    print("error")
