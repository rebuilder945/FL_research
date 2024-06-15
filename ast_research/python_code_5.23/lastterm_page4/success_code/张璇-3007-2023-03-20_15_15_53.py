a=eval(input())
n,m=eval(input())
b=len(a)
if n<m<b:
    del a[n-1:m]
    print(a)
elif n>m or n>b:
    print("error")
