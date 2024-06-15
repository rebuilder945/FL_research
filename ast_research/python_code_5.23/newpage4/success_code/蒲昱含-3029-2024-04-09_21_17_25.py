name=input().split(",")
score=eval(input())
c=[]
for i in range(len(name)):
    c.append([name[i],score[i]])
print(c)
