lst=list[input()].split(',')
n,m=int(input())
if n>m:
    del lst[n:m]
    print(lst)
    if n<=m:
        print('error')

