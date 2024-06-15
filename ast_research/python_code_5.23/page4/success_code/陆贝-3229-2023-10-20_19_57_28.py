lt=eval(input())
ls=[]
ii=[]
for i in lt:
    c=lt.count(i)
    if c==1:
        ls.append(i)
aa=ls.copy()
if len(aa)!=0:
    for i in range(len(aa)):
        a=min(aa)
        ii.append(a)
        aa.remove(a)
    print(ii)
else:
    print("False")
