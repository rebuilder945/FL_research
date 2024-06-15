a = eval(input())
n,m = sorted(input().split(','))
n = int(n)
m = int(m)
if m >= len(a):
    print('error')
else:
    print(a[:n] + a[m:])
