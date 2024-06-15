n,m = map(int,input().split())
if 0<=n<m<11 and m-n>=3:
    for x in range(n,m):
        for y in range(n,m):
            for r in range(n,m):
                if x!=y and y!=r and r!=x:
                    N=x*100+y*10+r
                    if N > 99:
                        print(N,end=' ')              
else:
    print("illegal input")
