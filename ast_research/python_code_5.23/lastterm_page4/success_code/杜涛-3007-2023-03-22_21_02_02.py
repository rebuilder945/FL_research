a=eval(input())
n,m=eval(input())
if n<=m:
    for i in range(m-n):
        del a[n]
    print(a)
else:
    print("error")
