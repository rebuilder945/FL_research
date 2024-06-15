a=eval(input())
n,m=eval(input())
if n<=len(a):
    if n<=m:
        del a[n:m]
    else:
        print("error")
else:
    print("error")
print(a)
