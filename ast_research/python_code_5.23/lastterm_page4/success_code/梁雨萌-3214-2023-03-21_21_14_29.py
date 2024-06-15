lis1=eval(input())
lis2=lis1.copy()
count=0
for i in range(0,len(lis1)):
    if lis1[i]==0:
        lis2.remove(lis1[i])
        count=count+1
if count!=0:
    for i in range(1,count+1):
        lis2.append(0)
print(lis2)
