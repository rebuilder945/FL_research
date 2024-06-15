lt=eval(input())
ii=list()
ls=[]
for i in lt:
    if i not in lt:
        a=lt.count(i)
        if a==1:
            ls.append(i)
if ls==[]:
    print("False")
else:
    l=len(ls)
    for i in range(l):
        m=min(ls)
        ii.append(m)
        ls.remove(m)
for x in ii:
    print(x,end=",")
