ls1 = list(map(str(input()).split(",")))
ls2 = eval(input())
for i in range(len(ls2)):
    a=ls1(i)
    b=[]
    b.append(a)
    a=ls2(i)
    b.append(a)
    ls3=[]
    ls3.append(b)
print(ls3)
