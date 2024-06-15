n,m=map(int,input().split())
lst=[]
if n<=m-3 and n>=0 and m<10:
    for i in range(n,m):
        for j in range(n,m):
            for h in range(n,m):
                if i!=j and i!=h and j!=h and i!=0:
                    print(i,j,h,sep="",end=" ")
else:
    print("illegal input")

