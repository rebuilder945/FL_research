a=eval(input())
sum=0
for i in a:
    sum+=i
aver=sum/len(a)
if(aver%1==0):
    print(f"%d"%aver)
else:
    print(f"%.2f"%aver)
