sums = input().split(',')
sums2 = eval(input())
sums3 = list(sums)
sums4 = ()
sums5 = []
for i in range(len(sums3)):
    sums4 = (sums3[i],sums2[i])
    sums5.append(list(sums4))
print(sums5)

