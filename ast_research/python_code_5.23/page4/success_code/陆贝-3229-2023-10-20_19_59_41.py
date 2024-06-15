lt=eval(input())
ls=[]
ii=[]
for i in lt:
    c=lt.count(i)
    if c==1:
        ls.append(i)
aa=ls.copy()
if len(aa)!=0:
    l=len(aa)
    for i in range(l):
        a=min(aa)
        ii.append(a)
        aa.remove(a)
    print(ii)
else:
    print("False")
