name=list(input().split(","))
score=eval(input())
list=[]
for i in range(len(name)):
    list.append([name[i],score[i]])
print(list)
