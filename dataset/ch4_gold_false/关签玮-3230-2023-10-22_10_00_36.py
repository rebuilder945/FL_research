ls1=eval(input())
ls2=[]
for i in range(len(ls1)):
    a=max(ls1)
    ls2.append(a)
    ls1.remove(a)
    print(a,end="")

