ist = eval(input())
n,m = eval(input())
if m >= len(ist) or n > m:
    print('error')
else:
    del ist[n:m]
    print(ist)
