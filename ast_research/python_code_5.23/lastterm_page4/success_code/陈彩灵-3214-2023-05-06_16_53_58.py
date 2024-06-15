ls1=eval(input())
ls2=[]
a = ls1.count(0)
for i in ls1:
    if i !=0:
        ls2.append(i)
if a!=0:
    for j in range(a):
        ls2.append(0)
print(ls2)
