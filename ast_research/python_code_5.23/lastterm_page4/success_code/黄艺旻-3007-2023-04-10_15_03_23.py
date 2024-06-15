a=eval(input())
n,m=eval(input())
if m<len(a) and n<len(a):
    if n<m:
        del a[n:m]
        print(a)
    else:
        del a[m+1:n+1]
        print(a)
else:
    print('error')
