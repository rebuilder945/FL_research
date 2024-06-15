name=input().split(',')
score=eval(input())
sums=list(name)
sums2=()
sums3=[]
for i in range(len(sums)):
    sums2=(sums[i],score[i])
    sums3.append(list(sums2))
print(sums3)

