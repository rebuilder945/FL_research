name=eval(input()).split
score=eval(input())
list=[]
for i in range(len(score)):
    element=[name[i],score[i]]
    list.append(element)
print(list)
