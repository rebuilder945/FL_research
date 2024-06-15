names=list(input())
scores=eval(input())
result=[]
for i in range(len(names)):
    sublist=[names[i],scores[i]]
    result.append(sublist)
print(result)
