lst=eval(input())
n,m=eval(input())
max=len(lst)
if n>=max-1 or m>=max-1:
    print('error')
else:
    del lst[n]
    del lst[m]
    print(lst)
