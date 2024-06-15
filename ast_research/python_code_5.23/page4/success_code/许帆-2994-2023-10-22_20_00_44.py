a = list(eval(input()))
n,m = eval(input())
if n > len(a) or n < -len(a) or n == 0:
    print(error)
else:
    a.extend(a[n-1]*m)
    print(a)
