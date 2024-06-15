n,m=input().split()
n,m=int(n),int(m)
if 0<=n <m <10 and m -n>2:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=0 and i!=j and j!=k and i!=k:
                    print(i,j,k,sep="",end=" ")
else:
    print("illegal input")

