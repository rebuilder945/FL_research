ls1=eval(input())
ls2=[]
for i in range(len(ls1)-1):
    if ls1[i] not in ls2:
        ls2.append(ls1[i])
print(ls2)
