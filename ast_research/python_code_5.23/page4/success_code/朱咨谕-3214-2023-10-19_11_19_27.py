ls1=eval(input())
ls2=[]
tot=0
for x in ls1:
    if x==0 : tot+=1
    else : ls2.append(x)
for y in range(tot) : ls2.append(0)
print(ls2)
