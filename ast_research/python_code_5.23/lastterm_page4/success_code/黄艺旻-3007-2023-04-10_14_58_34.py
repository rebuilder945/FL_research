a=eval(input())
n,m=eval(input())
if n>=m or m>len(a) or n>len(a):
    print('error')
else:
    del a[n,m]
    print(a)
