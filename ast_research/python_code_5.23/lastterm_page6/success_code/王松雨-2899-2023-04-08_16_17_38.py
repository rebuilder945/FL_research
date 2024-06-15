n,m= map(int,input().split())
if n>=m:
    print("illegal input")
else:
    flag=False
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=j and j!=k and i!=k:
                    if 100<i*100+j*10+k<1000:
                        flag=True
                        print(i*100+j*10+k,end=' ')
if flag==False:
    print("illegal input")
        

