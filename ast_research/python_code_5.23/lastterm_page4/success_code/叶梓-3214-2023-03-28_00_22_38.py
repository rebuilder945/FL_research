ls1=eval(input())
ls2=[]
for i in ls1:
    if i!=0:
        ls2.append(i)
n=ls1.count(0)
for i in range(n):
    ls2.append(0)
print(ls2)

