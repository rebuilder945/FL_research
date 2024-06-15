n,m= map(int,input().split())
if m-n!=3:
    print("illegal input")
else:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=j and j!=k and i!=k and 100<i*100+j*10+k<1000:
                    print(i*100+j*10+k,end=' ')
                else:
                    print("illegal input")
                
        

