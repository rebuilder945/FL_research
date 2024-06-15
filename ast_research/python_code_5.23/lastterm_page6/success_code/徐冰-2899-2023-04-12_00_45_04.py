n,m=map(int,input().split())
if 0<=n<m-2<=8:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=j and j!=k and i!=k and i!=0:
                    ls=[str(i),str(j),str(k)]
                    print("".join(ls),end=" ")
else:
    print("illegal input")
