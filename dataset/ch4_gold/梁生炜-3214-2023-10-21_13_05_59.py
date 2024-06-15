ls=eval(input())
a=[]
for i in ls:
    if i==0:
        ls.remove(i)
        a.append(i)
ls2=ls+a
print(ls2)
