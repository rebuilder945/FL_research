QAQ=input()
N=QAQ[0]
M=QAQ[2]
if N.isnumeric() and M.isnumeric() and int(M)-int(N)>=3:
    n=int(N)
    m=int(M)
    a=[]
    for x in range(n,m): 
        if x!=0:
            for y in range(n,m):
                if x!=y:
                    for z in range(n,m):
                        if z!=y and z!=x:
                            a.append(str(x)+str(y)+str(z))
                        else:
                            continue
                else:
                    continue

    print(" ".join(a))
else:
    print("illegal input")








        



    








