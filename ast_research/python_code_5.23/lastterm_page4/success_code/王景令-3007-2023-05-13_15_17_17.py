a = eval(input())
n,m = sorted(input().split(','))
if m >= len(a):
    print('error')
else:
    print(a[:n] + a[m:])
