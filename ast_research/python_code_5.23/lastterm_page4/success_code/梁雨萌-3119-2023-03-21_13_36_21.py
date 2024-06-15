lis1=eval(input())
lis2=[]
for i in range(len(lis1),0,-1):
        if lis1.count(lis1[i])==1:
            lis2.append(lis1[i])
print(lis2)
