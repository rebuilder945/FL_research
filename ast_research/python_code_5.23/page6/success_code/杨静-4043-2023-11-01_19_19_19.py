n=eval(input())
ls=[]
for x in n:
    for i in x:
        ls.append(i)
lsset=set(ls)
lsdel=list(lsset)
lsdel.sort()
ls.sort()
for j in lsdel:
    print(j,ls.count(j))
