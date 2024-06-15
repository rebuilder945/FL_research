sums=list(input().split(','))
sums2=eval(input())
sums4=()
sums5=[]
for i in range(len(sums)):
    sums4=(sums[i],sums2[i])
    sums5.append(list(sums4))
print(sums5)
