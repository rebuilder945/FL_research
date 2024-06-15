sName=input().split(",")
score=eval(input())
sName1=list(sName)
l1=()
l2=[]
for i in range(len(sName1)):
    l1=(sName1[i],score[i])
    l2.append(list(l1))
l2.sort(key=lambda x:x[1])
print(l2)
