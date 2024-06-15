lst=eval(input())
n,m=eval(input())
if n>len(lst) or m>len(lst):
    print('error')
else:
    if n<=m:
        del lst[n:m]
    else:
        del lst[m+1:n+1]
    print(lst)
