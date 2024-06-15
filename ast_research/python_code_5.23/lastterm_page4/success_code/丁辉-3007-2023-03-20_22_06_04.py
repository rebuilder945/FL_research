a=(eval(input()))
n,m=eval(input())
if n<=m:
    if m<len(a):
        a.remove(a[n:m])
        print(a)
    else:
        print("error")
else:
    print("error")
