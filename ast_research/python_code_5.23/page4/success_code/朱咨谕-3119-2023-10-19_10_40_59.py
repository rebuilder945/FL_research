ls1=eval(input())
#[4,3,2,3,2,4,True]
#[4,3,2,3,2,4]
# 0 1 2 3 4 5 len=6
ls2=[]
l=len(ls1)
for i in range(l):
    tot=0 
    for j in range(i,l):
        if ls1[i]==ls1[j]:
            tot+=1
    if tot==1 : ls2.append(ls1[i])
print(ls2)
