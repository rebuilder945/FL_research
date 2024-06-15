a =eval(input())
n,m = eval(input())
if m<len(a) and n<=m :
    del a[n:m]
    print(a)
else :
    print("error")
