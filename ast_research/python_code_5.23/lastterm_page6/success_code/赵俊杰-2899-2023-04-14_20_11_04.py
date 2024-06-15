n,m=map(int,input().split())
ls=[]
s=""
stext="illegal input"
if n>=m or m<0 or n<0:
    print(stext)
else:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a==b or b==c or a==c:
                    pass
                else:
                    d=a*100+b*10+c
                    ls.append(d)
    if len(ls)==0:
        print(stext)
    else:
        for f in ls:
            s=s+str(f)+" "
        print(s)

