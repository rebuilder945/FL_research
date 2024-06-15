name=input().split(',')
score=eval(input())
lst=[]
for i in range(len(name)):
    item=[]
    item.append(name[i])
    item.append(score[i])
    lst.append(item)
print(lst)



