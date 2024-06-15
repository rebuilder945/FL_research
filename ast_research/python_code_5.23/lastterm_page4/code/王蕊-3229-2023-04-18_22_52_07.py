ls1=eval(input())
ls2=[]
for x in ls1:
    if (ls1.count(x)==1):
        ls2.append(x)
ls2.sort()
if ls2=[]:
    print("False")
else:
    print(",",jion(str(x)for x in ls2))

