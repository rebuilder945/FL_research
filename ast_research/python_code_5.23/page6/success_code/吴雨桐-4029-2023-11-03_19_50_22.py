N,M=input().split()
n=int(N)
m=int(M)
if m-n<3:
    print("illegal input")
else:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z and x!=0:
                    ls=0
                    ls=str(x)+str(y)+str(z)
                    print(ls,end=' ')
    
