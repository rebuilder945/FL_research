lt=eval(input())
ls=[]
aa=[]
for i in lt:
    lt.remove(i)
    if i not in lt:
        ls.append(i)
if ls==[]:
    print("False")
else:
    for x in range(len(ls)):
        a=min(ls)
        if x<=a:
            aa.append(x)
            ls.remove(a)
for y in aa:
    print(y,end=",")

    
