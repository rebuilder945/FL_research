lst=list(eval(input()))
n,m=eval(input())
if n<=m:
    if m<=len(lst):
        del lst[n:m]
        print(lst)
    else:
        print('error')
else:
    print('error')
