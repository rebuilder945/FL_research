stu=input().split(',')
score=input().split(',')
sum=[]
for x in range(len(stu)):
    sum.append([stu[x],int(score[x])])
sum.sort(key=lambda x:x[1])
print(sum)

