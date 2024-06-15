a = eval(input())
n,m = map(int,input().split(','))
if n>m or m>=len(a):
    print('error')
else:
    n = int(n)
    m = int(m)
    for i in range(n,m):
        del a[i]
    print(a)
