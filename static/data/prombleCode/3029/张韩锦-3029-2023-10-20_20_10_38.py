name=input().split(",")
score=eval(input())
lst=[]
for i in range(len(name)):
    lst2=[]
    lst2.append(name[i])
    lst2.append(score[i])
    lst.append(lst2)
print(lst)
lst=[[name[i],score[i]] for i in range(len(name))]

