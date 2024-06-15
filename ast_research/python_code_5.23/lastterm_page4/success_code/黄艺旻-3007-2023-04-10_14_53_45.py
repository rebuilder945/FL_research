a=eval(input())
n,m=eval(input())
if n<=m or m not in range(len(a)) or n not in range(len(a)):
    print('error')
else:
    del a[n,m]
    print(a)
