n,m=map(int,input().split())
if 0<= n < m < 11 and m - n >=3:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z:
                    N = 100*x + 10*y + z
                    if N > 99:
                        print(N,end=' ')
else:
    print('illegal input')
