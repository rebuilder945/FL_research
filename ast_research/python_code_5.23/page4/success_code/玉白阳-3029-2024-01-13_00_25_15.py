name=list(input().split(","))
score=eval(input())
list=[]
for i in range(len(name)-1):
    list.append([name[i],score[i]])
print(list)
