a = eval(input())
sum = 0
for i in range(0,len(a)):
    sum+=a[i]
aver = sum / len(a)
print("%.2f"%aver)
