name=input().split(",")
score=eval(input())
ls=[]
for i in range(len(name)-1):
    ls.append([name[i],score[i]])
print(ls)
