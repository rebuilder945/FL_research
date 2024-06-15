a = list(eval(input()))
n,m = eval(input())
if n > len(a) or n < -len(a) or n == 0:
    print('error')
else:
    if n > 0:
        for i in range(m):
            a.append(a[n])
        print(a)
    if n < 0:
        n = len(a)+n
        for i in range(m):
            a.append(a[n])
        print(a)

