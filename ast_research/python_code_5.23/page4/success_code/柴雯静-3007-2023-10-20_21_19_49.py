jack = eval(input())
n,m = int(input())
b = len(jack)
if b < n and b <= m:
    if n <= m:
        del jack[n,m]
        print(jack)
    else:
        print('error')
else:
    print('error')
