n,m = map(int,input().split())
if m-n>=3 and 0<=n<m<11:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and c!=a:
                    m = a*100+b*10+c
                    if m>99:
                        print(m,end=" ")
else:
    print("illegal input")


