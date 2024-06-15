ls1=eval(input())
ls2=[]
for i in range(-1,-len(ls1),-1):
    if ls1[i] not in ls2:
        ls2.append(ls1[i])
ls2.reverse()
print(ls2)
