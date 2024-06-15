n,m = map(int,input().split())
if 0<=n < m <11 and m - n >= 3:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and c!=b and a!=c:
                    k = a*100+b*10+c
                    if k>99:
                        print(k,end=' ')
else:
    print("illegal input")
