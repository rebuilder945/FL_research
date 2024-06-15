a=eval(input())
n,m=eval(input())
if 0<n<m<len(a):
    del a[n:m]
    print(a)
elif len(a)>n>=m>0:
    print(a)
else:
    print("error")

