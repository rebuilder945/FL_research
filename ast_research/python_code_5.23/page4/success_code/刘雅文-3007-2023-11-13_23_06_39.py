'''a=eval(input())
n,m=eval(input())
if n<=len(a):
    for x in range(n,m):
        del a[x]
    print(a)
else:
    print('error')'''


a=eval(input())
n,m=eval(input())
if n<=len(a):
    for i in range(n,m):
        del a[i]
    print(a)
else:
    print('error')
