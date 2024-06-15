n,m=map(int,input().split())
n1=[]
if n<=m-3 and 0<=n<8 and 0<=m<10:
    # for i in range(n,m):
    #     n1.append(i)
        for x in range(n,m):
            for y in range(n,m):
                for z in range(n,m): 
                    if x!=y and x!=z and y!=z:
                        s=str(x)+str(y)+str(z)
                        if int(s)>100:
                            print(s,end=" ")
else:
    print("illegal input")

