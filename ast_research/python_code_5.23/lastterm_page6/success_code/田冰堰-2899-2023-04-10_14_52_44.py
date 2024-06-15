n,m=map(int,input().split())
if 0<=n<m<11 and m-n>=3:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=j and j!=k and k!=i:
                    N=100*i+10*j+k
                    if N>99:
                        print(N,end='')
else:
    print("illegal input")
                
