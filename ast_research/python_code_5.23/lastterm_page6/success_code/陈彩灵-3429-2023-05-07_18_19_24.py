ls=list(input())
lsa=[]
lsk=[]
ls1=[]
lsq=[]
for i in ls:
    if i in "abcdefghijklmnopqrstuvwxyz":
        lsa.append(i)
    elif i ==' ':
        lsk.append(i)
    elif i in "0123456789":
        ls1.append(i)
    else:
        lsq.append(i)
print(len(lsa),len(lsk),len(ls1),len(lsq))
