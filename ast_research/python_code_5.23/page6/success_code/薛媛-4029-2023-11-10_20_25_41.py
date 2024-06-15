n,m=input().split('')
n,m=int(n),int(m)
ls=[]
if type(n)!=int or type(m)!=int or n<0 or n>9:
    ls=[]
else:
    for a in range(n,m):
        sa=str(a)
        for b in range(n,m):
            sb=str(b)
            for c in range(n,m):
                sc=str(c)
                sabc=sa+sb+sc
                if int(sa)!=0 and sa!=sb and sb!=sc and sc!=sa and len(sabc)==3 and sabc not in ls:
                    ls.append(sabc)
if ls==[]:
    print("illegal input")
else:
    print(''.join(x for x in ls))
