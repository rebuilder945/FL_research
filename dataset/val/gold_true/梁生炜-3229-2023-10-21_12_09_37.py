ls1=eval(input())
ls2=[]
for i in ls1:
    if ls1.count(i)>1:
        for j in range(ls1.count(i)):
            ls1.remove(i)
ls1.sort()
ls2=','.join(str(j) for j in ls1)
if len(ls1)>0:
    print(ls2)
else:
    print("False")
