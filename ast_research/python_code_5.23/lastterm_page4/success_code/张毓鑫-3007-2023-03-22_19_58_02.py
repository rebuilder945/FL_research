from distutils.log import error


a=input()
n,m=eval(input())
if 0<=n<=m<=len(a):
    del a[n:m]
    print(a)
else:
    print('error')
