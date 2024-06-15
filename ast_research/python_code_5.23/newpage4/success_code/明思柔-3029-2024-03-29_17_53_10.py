students=list(eval(input()))
scores=list(eval(input()))
result=[]
for i in range(len(students)):
    sublist=[students[i],scores[i]]
    result.append(sublist)
print(result)
