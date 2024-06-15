ls1=eval(input())
ls2=[]
for i in range(len(ls1)):
    if not ls1[i] in ls2:
        ls2.append(ls1[i])
if ls2==[]:
    print(False)
else:
    print(*ls2,sep=",")

