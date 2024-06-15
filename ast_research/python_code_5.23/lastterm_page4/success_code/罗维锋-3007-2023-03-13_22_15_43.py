a=eval(input())
n,m=eval(input())
if n<=m:
    if n in range(0,len(a)+1) and m in range(0,len(a)+1):
        for x in range(n,m):
            del a[x]
    else:
        print("error")
print(a)

