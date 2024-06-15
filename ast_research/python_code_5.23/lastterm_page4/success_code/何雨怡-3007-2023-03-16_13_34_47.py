lst=eval(input())
n,m=eval(input())
max=len(lst)
if n>=max or m>=max:
    print('error')
else:
    del lst[n]
    del lst[m]
    print(lst)
