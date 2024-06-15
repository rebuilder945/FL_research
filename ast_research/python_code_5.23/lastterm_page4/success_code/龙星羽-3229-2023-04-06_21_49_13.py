shu=eval(input())
shu.sort()
ls=[]
for x in shu:
    if shu.count(x)==1:
        ls.append(x)
if ls==[]:         
    print("False")
else:
    ls=list(map(str,ls))
    print(",".join(ls))

