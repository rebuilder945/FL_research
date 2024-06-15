list = eval(input())
sum=0
for i in range(0,len(list)):
    sum = list[i]+sum
aver=sum/len(list)
if aver%1==0:
    print(int(aver))
else:
    print("%.2f"%aver)
# 记得先设一个sum=0
