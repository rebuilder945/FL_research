list = eval(input())
sum=0
for i in range(0,len(list)):
    sum = list[i]+sum
aver=sum/len(list)
print("%.2f"%aver)
