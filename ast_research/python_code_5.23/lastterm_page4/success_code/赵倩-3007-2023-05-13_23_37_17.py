a=eval(input())
n,m=map(int,input().split(","))
if n<=m and n<=len(a)-1:
    del a[n,m]
    print(a)
else:
    print("error")







