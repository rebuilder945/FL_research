ls1=eval(input())
ls1.reserve()
ls2=[]
for i in range(len(ls1)-1):
    if ls1[i] not in ls2:
        ls2.append(ls1[i])
ls2.reserve()
print(ls2)
