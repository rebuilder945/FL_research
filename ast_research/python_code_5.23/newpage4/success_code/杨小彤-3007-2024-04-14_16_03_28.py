a = eval(input())
n,m = eval(input())
b = len(a)
if m-1 > b:
    print('error')
elif n > m:
    print('error')
else:
    del a[n:m]
print(a)
