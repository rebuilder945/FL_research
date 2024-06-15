n,m=map(int,input().split())
n1=[]
n2=[]
if n<=m-3 and 0<=n<8 and 0<=m<10:
    for i in range(n,m):
        n1.append(i)
        for x in n1:
            for y in n1:
                for z in n1:
                    s=str(x)+str(y)+str(z)
                    if x!=y and x!=z and y!=z:
                        
                        if int(s)>100:
                            n2.append(int(s))
    n3=list(set(n2))
    print(" ".join(str(i) for i in n3))
                        

else:
    print("illegal input")

