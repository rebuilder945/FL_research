ls=eval(input())
ls1=[]
ls2=[]
for x in range(0,len(ls)):
    if ls[x]==0:
        ls1.append(ls[x])
    else:
        ls2.append(ls[x])
print(ls2+ls1)
