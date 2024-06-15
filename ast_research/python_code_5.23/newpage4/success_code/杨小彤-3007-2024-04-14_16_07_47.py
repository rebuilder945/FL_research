a = eval(input())
n,m = eval(input())
b = len(a)
if n > m:
    print('error')
elif m-1 > b-1:
    print('error')
else:
    del a[n:m]
print(a)
