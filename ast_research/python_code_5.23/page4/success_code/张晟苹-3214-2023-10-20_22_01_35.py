ls=eval(input())
ls2=[]
for i in ls:
    if i==0:
        ls2.append(i)
for i in ls:
    if i==0:
        ls.remove(i)
ls3=ls+ls2
print(ls3)
