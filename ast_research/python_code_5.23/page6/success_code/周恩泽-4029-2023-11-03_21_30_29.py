n,m=map(int,input().split())
if n<=m-3 and 0<=n<=7 and type(m)==int and type(n)==int:
    a=[]
    for x in range(n,m):
        a.append(str(x))
    m=[]
    for i in a:
        for x in a:
            for y in a:
                c=i+x+y
                if i!=x and i!=y and x!=y:
                    if int(c)>=100:
                        m.append(c)
    print(m)
    # if len(m)==0:
    #     print("illegal input")
    # else:
    #     l=[]
    # for x in m:
    #     if int(x[0])==0:
    #         l.append(x)
    # p=[x for x in m if x not in l]
    # print(" ".join(str(x) for x in p))
else:
    print("illegal input")

