n,m = map(int,input().split())
if m - n >3 and n>=0 and m <= 10:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a != b and a != c and b != c:
                    sb = a*100 + b*10 + c
                    print(sb,end=" ")
