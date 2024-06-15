n,m=map(eval,input().split())
if n>=m or m-n<=2 or n<0 or m<0 or n>8:
    print("illegal input")
else:
    lst=[]
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=j and j!=k and i!=k:
                    a=str(i)+str(j)+str(k)
                    a=str(int(a))
                    if a not in lst and len(a)==3:
                        lst.append(a)
    lst=map(eval,lst)
    for x in lst:
        print("%d"%(x),end=" ")
