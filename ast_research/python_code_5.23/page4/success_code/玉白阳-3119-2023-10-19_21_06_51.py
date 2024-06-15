ls1=eval(input())
ls2=ls1.copy()
for i in ls1:
    if len(ls2)==1:
        print(ls2)
    if len(ls2)>1 and ls2.count(i)>1:
        ls2.append(i)
        print(ls2)
