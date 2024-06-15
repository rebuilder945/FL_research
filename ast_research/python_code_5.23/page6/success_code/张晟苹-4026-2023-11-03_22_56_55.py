n=eval(input())
ls1=[0,1]
for i in range(n):
    a=ls1[-1]+ls1[-2]
    ls1.append(a)
del ls1[0]
ls2=list(ls1)
while 1 in ls2:
    ls2.remove(1)
ls2.append(ls1[-1]+ls1[-2])
ls1.remove(1)
c=0
for i in range(n):
    b=ls2[i]/ls1[i]
    c=c+b
print('%.4f'%(c))

