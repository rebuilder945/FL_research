a = input()
n,m = input()
if n<len(a) and m<len(a):
    if n<m:
        del a[n,m]
        print(a)
    else:
        del a[m+1,n+1]
        print(a)
else:
    print("error")
