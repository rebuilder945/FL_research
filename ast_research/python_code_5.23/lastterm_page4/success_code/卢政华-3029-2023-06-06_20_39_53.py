sums=input().split(',')
score=eval(input())
name=list(sums)
sums4=[]
sums5=[]
for i in range(len(name)):
    sums4=(name[i],score[i])
    sums5.append(list(sums4))
print(sums5)
