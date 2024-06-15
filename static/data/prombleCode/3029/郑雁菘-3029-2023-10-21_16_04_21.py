sum1 = input().split(',')
sum2 = eval(input())
sum3 = ()
sum4 = []
for i in range(len(sum1)):
    sum3 = (sum1[i],sum2[i])
    sum4.append(list(sum3))
print(sum4)
