n,m=input().split()
n=int(n)
m=int(m)
if n>=m or m-n<3 or m>=10:
    print("illegal input")
else:
    m=[str(x) for x in range(n,m)]
    n=[]
    for x in m:
        for y in m:
            for z in m:
                n.append(x+y+z)
    a=[]
    for x in n:
        if x[0]!=0:
            if x[0]!=x[1] and x[0]!=x[2] and x[1]!=x[2]:
                a.append(x)
    if a==None:
        print("illegal input")
    else:
        for i in a:
            print(i,end=" ")
