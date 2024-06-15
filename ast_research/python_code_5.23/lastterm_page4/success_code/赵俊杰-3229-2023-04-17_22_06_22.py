ls=eval(input())
ls2=[]

for x in ls:
    if ls.count(x)==1:
        ls2.append(x)
    else:
        pass
if len(ls2)==0:
    print("False")
else:
    ls2.sort()
    s=str(ls2[0])
    for m in ls2[1:]:
        s=s+","+str(m)
    print(s)
