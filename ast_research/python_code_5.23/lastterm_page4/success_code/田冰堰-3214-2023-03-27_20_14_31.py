ls=eval(input())
ls1=[]
ls2=[]
for i in range(len(ls)):
    if ls[i]==0:
        ls1.append(0)
    else:
        ls2.append(ls[i])
print(ls1+ls2)

