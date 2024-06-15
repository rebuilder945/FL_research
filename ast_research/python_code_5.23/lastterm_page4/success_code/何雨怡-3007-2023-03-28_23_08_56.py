lst=eval(input())
lst2=lst.copy()
n,m=eval(input())
long=len(lst)
if n>m:
    print('error')
elif m>=long:
    print('error')
elif n>=long:
    print('error')
elif n==m:
    print(lst)
else:
    newlist=lst[n,m]
    for i in newlist:
        if i in lst2:
            lst.remove(i)
        else:
            pass
    print(lst)
