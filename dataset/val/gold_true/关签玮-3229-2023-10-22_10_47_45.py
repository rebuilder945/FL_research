ls1=eval(input())
ls2=[]
for i in ls1:
    a=ls1.count(i)
    if a==1:
        ls2.append(i)
if ls2==[]:
    print("False")
else:
    ls3=sorted(ls2)
    for i in ls3:
        if ls3[-1]!=i:
           print(i,end=",")
        else:
            print(i)

