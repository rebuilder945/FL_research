ls1=eval(input())
a=ls1.count(0)
ls1.remove(0)
ls2=ls1.copy()
i=0
while i <a:
    i+=1
    ls2.append(0)
print(ls2)

