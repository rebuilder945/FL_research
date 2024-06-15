a = eval(input())
n,m = map(int,input().split(","))
if (n+1) < len(a):
    x = a[n]
    for i in range(m):
        a.append(x)
else:
    print("error")
