a=[]
n,m=eval(input())
if n<len(a) and m<len(a)
    if n<=m:
        del a[n:m]
        print(a)
    else:
        del a[n+1:m+1]
        print(a)
else:
    print('error')
    

