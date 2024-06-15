n,m=map(int,input().split())
if n>=m or m-n!=3 or n<0 or n>10 or m>10 :
    print("illegal input")
else:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=j and i!=k and j!=k:
                    c=100*i+10*j+k
                    print(c,end=" ")
                
