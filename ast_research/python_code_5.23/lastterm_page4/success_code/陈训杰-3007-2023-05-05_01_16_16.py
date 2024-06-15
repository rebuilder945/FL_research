lst=eval(input())
n,m=eval(input())
if len(lst)>=m and len(lst)>=n and n<=m:
    del lst[n:m]
    print(lst)
else:
    print('error')
