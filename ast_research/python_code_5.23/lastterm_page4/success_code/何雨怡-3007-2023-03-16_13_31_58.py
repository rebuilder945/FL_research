lst=eval(input())
n,m=eval(input())
max=len(lst)
index=max-1
if n>index or m>index:
    print('error')
else:
    del lst[n]
    del lst[m]
    print(lst)
