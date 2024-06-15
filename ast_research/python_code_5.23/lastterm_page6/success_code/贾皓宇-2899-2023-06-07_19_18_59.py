a,b=input().split(' ')
a=int(a)
b=int(b)
lst=[x for x in range(a,b)]
LST=[]
if a<b:
    while True:
        lst2=list(set(lst))
        sabc=int(str(lst2[0])+str(lst2[1])+str(lst2[2]))
        if sabc not in LST:
                LST.append(sabc)
        if len(LST)==6:
            print(LST[0],LST[1],LST[2],LST[3],LST[4],LST[5])
            break
