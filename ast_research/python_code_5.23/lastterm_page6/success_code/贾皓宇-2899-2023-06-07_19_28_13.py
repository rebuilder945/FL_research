a,b=input().split(' ')
a=int(a)
b=int(b)
lst=[x for x in range(a,b)]
LST=[]
if a<b and a>0 and a<10 and b<10:
    for x in lst:
        for y in lst:
            for z in lst:
                if x!=y and x!=z and y!=z:
                    sabc=int(str(x)+str(y)+str(z))
                    if sabc not in LST:
                        LST.append(sabc)
print(LST[0],LST[1],LST[2],LST[3],LST[4],LST[5])
