lis1=eval(input())
lis2=[]
for i in range(len(lis1)-1,-1,-1):
        if lis2.count(lis1[i])==0:
            lis2.append(lis1[i])
lis2.reverse()
print(lis2)
