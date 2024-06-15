n,m=map(int,input().split())
if m-n<3 or n>=m:
    print("illegal input")
else:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=j and i!=k and j!=k and i!=0:
                    num=100*i+10*j+k
                    print(num,end=" ")
