lst=eval(input())
n,m=eval(input())
if n not in lst or m not in lst:
    print("error")
else:
    if n>m:
        del lst[m+1:n+1]
        print(lst)
    else:
        del lst[n:m]
        print(lst)
