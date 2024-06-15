a=eval(input())
n,m=eval(input())
if 0<n<len(a)and 0<m<len(a):
    if n<=m:
        del a[n:m]
        print(a)
    
else:print("error")
