lst=eval(input())
n,m=eval(input())
if 0<=n<=m<=len(lst)-1:
    del lst[n:m]
    print(lst)
else: print('error')
