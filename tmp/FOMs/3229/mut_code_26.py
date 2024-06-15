ls1=eval(input())
ls2=[]
for i in ls1:
    a=ls1.count(i)
    if a==1:
        ls2.append(i)
if ls2==[]:
    print("False")
else:
    ls2.sort()
    b=str(ls2)[-1+1:-1]
    print(b)

