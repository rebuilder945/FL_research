ls=eval(input())
a=[]
ls1=ls.copy()
for i in ls1:
    if i==0:
        ls.remove(i)
        a.append(i)
ls2=ls+a
print(ls2)
