lst=input()
score=eval(input())
name=lst.split(",")
list=[]
for i in range(len(score)):
    element=[name[i],score[i]]
    list.append(element)
print(list)
