a = eval(input())
n,m = eval(input())
b = len(a)
if n > m:
    print('error')
elif m > b:
    print('error')
else:
    del a[n:m]
    print(a)
