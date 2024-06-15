lst=eval(input())
lst.sort()
lst2=[]
for x in lst:
    if lst.count(x)==1:
        lst2.append(x)
L=len(lst2)
if L>0:
    print(lst2[0],end='')
    for i in range(1,L):
        print(',%d'%(lst2[i]),end='')
else:
    print('False')
