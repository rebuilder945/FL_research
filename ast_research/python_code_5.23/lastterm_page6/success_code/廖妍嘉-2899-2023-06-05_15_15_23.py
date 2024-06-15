n,m=map(int,input().split())
print(n,m)
if n>=m or m-n<=2 or n<0 or m<0:
    print("illegal input")
else:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and a!=c and a!=0:
                    print(100*a+10*b+c,end=' ')


