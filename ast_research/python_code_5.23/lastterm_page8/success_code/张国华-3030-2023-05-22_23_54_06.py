name=input().split(',')
score=input().split(',')
result=[]
for i in range(len(name)):
    result.append([name[i],int(score[i])])
result.sort(key=lambda x:x[1])
print(result)
