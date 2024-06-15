lis1=eval(input())
lis2=lis1.copy()
for i in range(0,len(lis1)):
    if lis1[i]==max(lis1) or lis1[i]==min(lis1):
        lis2.remove(lis1[i])
print(lis2)
