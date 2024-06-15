n,m=map(int,input().split())
if 0<=n<m<11 and m-n>=3:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and a!=c and b!=c:
                    y = 100*a+10*b+c
                    if y >99:
                        print(y,end=" ")
else:
    print("illegal input")
