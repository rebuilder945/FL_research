lis1=eval(input())
lis2=[]
for i in range(len(lis1)-1,-1,-1):
        if lis1.count(lis1[i])<2:
            lis2.append(lis[i])
print(lis2)
