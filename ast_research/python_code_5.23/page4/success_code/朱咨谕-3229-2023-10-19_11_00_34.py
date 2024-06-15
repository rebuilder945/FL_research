ls1=eval(input())
l=len(ls1)
ls2=[]
a=0
for i in range(l):
    tot=0
    for j in range(l):
        if ls1[i]==ls1[j] : tot+=1
    if tot==1 : 
        ls2.append(ls1[i])
        a=1
if(a==1) : 
    ls2.sort()
    print(ls2)
else : print('False')
