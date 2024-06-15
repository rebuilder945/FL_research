name=input().split(",")
score=eval(input())
list1=[]
for i in range(len(name)):
    list2=[]
    list2.append(name[i])
    list2.append(score[i])
    list1.append(list2)
print(list1)
