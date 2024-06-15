ls=eval(input())
ls2=[]
for i in ls:
    if ls.count(i)==1:
        ls2.append(i)
        a=ls2
    else:
        continue
if len(ls2)==0:
    a=False
a.sort()
print(a)
