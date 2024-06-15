ls1=eval(input())
ls2=[]
c=ls1.count(0)
if c==len(ls1):
    print(0)
else :
    for i in range(len(ls1)):
        a=max(ls1)
        ls2.append(a)
        ls1.remove(a)
        print(a,end="")

