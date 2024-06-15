name=input().split(',')
score=input().strip('[]').split(',')
n=len(name)
result=[]
for i in range(n):
    result.append([name[i],int(score[i])])
print(result)
