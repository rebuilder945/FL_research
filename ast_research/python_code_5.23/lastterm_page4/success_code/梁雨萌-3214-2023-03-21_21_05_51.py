lis1=eval(input())
lis2=[]
count=0
for i in lis1:
    if i==0:
        lis1.remove(i)
        count=count+1
lis2=lis1
for i in range(1,count+1):
    lis2.append(0)
print(lis2)
