lst=eval(input())
n,m=eval(input())
long=len(lst)
if n>m:
    print('error')
elif m>=long:
    print('error')
elif n==m:
    print(lst)
else:
    lst1=lst[:n+1]
    lst2=lst[m+1:]
    new=lst1+lst2
    print(new)
