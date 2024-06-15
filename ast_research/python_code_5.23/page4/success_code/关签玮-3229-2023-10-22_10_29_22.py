ls1=eval(input())
ls2=[]
for i in ls1:
    a=ls1.count(i)
    if a==1:
        ls2.append(i)
ls3=sorted(ls2)
ls3.reverse()
print(ls3)

