ls1=eval(input())
ls2=[]
for x not in ls1:
    if ls1.count(x)==1:
        ls2.append(x)
if len(ls2)==0:
    print("False")
else:
    ls2.sort()
    print(ls2)
