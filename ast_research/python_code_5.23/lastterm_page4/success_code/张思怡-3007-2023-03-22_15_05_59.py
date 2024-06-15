a=eval(input())
n,m=eval(input())
if n<=m<=len(a):
    a[n:m]={}
    print(a)
else:
    print("error")


