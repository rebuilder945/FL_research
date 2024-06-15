from distutils.log import error


a=eval(input())
n,m=eval(input())
a=a.split(",")
if 0<=n<=m<=len(a):
    print(a.remove(n,m))
else:
    print('error')
