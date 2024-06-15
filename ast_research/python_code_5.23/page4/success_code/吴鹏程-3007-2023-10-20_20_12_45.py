a=eval(input())
n,m=map(int,input().split(","))
if n<=len(a):
    for x in range(n,m):
        del a[x]
    print(a)
else:
    print("error")
