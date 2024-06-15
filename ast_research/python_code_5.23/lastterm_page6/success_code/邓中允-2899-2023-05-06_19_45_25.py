n,m=map(int,input().split())
if 0<=n<m<11 and m-n>=3:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and c!=a:
                    qq=a*100+b*10+c
                    if qq>99:
                        print(qq,end=' ')
else:
    print("illegal input")
