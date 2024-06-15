lst= eval(input())
n,m = input().split(',')
n=int(n)
m=int(m)
if n<len(lst) and m<len(lst):
    if n<m:
        del lst[n:m]
        print(lst)
    else:
        del lst[m+1:n+1]
else:
    print('error')

