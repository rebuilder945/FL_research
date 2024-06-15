n,m = map(int,input().split())
if 0<=n < m<11 and m - n > 2:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a != b and b != c and c != a:
                    N = 100*a + 10*b + c
                    if N > 99:
                        print(N,end=' ')
else:
    print("illegal input")

