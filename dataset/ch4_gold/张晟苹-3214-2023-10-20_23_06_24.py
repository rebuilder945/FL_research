ls=eval(input())
ls2=[]
for i in ls:
    if i==0:
        ls2.append(i)
n=ls.count(0)
for i in range(n):
    ls.remove(0)
ls3=ls+ls2
print(ls3)
