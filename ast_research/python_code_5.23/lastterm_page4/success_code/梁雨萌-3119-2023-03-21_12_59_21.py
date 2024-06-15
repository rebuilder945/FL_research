lis1=eval(input())
lis2=lis1.copy()
for i in range(0,len(lis1)):
    for j in range(i,len(lis2)):
        if lis1[i]==lis2[j]:
            del lis2[j]
            break
print(lis2)
