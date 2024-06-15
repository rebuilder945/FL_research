names=list(input())
scores=eval(input())
result=[]
for i in range(len(names)):
    sublist=[names[i-1],scores[i-1]]
    result.append(sublist)
print(result)
