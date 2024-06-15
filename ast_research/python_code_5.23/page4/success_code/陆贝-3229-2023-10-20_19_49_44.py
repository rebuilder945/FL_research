lt=eval(input())
ls=[]
ii=[]
for i in lt:
    c=lt.count(i)
    if c==1:
        ls.append(i)
if ls!=[]:
    for i in ls:
        a=max(ls)
        ii.append(a)
        ii.remove(a)
    print(ii)
else:
    print("False")
