lst=eval(input())
n, m=map(int,input().split(','))
if n<len(lst) and len(lst)>m>=n:
    del lst[n:m]
    print(lst)
else:
    print('error')
