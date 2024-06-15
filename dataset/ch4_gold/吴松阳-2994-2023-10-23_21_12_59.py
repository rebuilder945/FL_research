a = list(map(int,input().split(',')))
n,m = map(int,input().split(','))
if n > len(a) - 1:
    print('error')
else:
    for i in range(m):
        a.append(a[n])
    print(a)
