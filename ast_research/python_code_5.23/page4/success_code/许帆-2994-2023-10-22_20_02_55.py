a = list(eval(input()))
n,m = eval(input())
if n > len(a) or n < -len(a) or n == 0:
    print('error')
else:
    for i in range(m):
        a.append(a[n-1])
    print(a)
