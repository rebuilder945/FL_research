name=input().split(',')
score=input().strip('[]').split(',')
n=len(name)
result=[]
for i in range(n):
    result.append([names[i],int(scores[i])])
print(result)
