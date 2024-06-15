n,m=map(int,input().split())
lst=[]
if n<m and n>=0 and m<=10:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=0 and i!=j and i!=k and j!=k:
                    c=str(i)+str(j)+str(k)
                    lst.append(c)
    print(" ".join(lst))
else:
    print("illegal input")
