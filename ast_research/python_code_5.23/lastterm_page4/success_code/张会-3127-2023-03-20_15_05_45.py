n = eval(input())
sum1 = range(1,n+1)
sum2 =[]
for i in range(len(sum1)-1):
    sum2.append(sum1[i+1])
sum2.append(sum1[0])
print(sum2)
