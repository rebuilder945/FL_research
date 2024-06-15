name=input().split(",")
score=eval(input())
ls=[]
for i in range(len(name)):
    ls.append([name[i],score[i]])
print(ls)
