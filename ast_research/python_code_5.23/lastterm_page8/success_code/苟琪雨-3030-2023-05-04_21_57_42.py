names=input().split(',')
scores=input().split(',')
result=[]
for i in range(len(names)):
    result.append([names[i],scores[i]])
result=sorted(result,key=lambda x:x[1])
print(result)
