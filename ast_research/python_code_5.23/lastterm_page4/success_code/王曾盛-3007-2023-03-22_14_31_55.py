lst=input().split(',')
n,m=input().split(",")
n=int(n)
m=int(m)
if n>m:
    del lst[n:m]
    print(lst)
    if n<=m:
        print('error')

