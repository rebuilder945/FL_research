n,m=map(int,input().split())
if n>=m or m-n<=2:
    print("illegal input")
else:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and a!=c:
                    print(100*a+10*b+c)


