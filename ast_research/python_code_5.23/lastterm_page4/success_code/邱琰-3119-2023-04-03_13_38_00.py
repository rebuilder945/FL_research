ls=eval(input())
ls2=[]
for i in range(len(ls)):
    if ls[i:].count(ls[i])==1:
        ls2.append(ls[i])
print(ls2)
