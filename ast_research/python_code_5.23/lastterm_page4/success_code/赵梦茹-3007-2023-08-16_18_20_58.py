list=eval(input())
n,m=input().split(',')
n=int(n)
m=int(m)
if n<len(list) and m<len(list):
    if n<=m:
        del list[n:m]
        print(list)
    else:
        print('error')
else:
    print('error')


