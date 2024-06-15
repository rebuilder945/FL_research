lt=eval(input())
ls=[]
ii=[]
for i in lt:
    c=lt.count(i)
    if c==1:
        ls.append(i)
if len(ls)!=0:
    l=len(ls)
    for i in range(l):
        a=min(ls)
        ii.append(a)
        ls.remove(a)
    print(ii)
else:
    print("False")
