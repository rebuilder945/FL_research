name=input().split(",")
score=list(eval(input()))
ls=[]
for i in range(len(name)):
    ls.append([name[i],score[i]])
ls.sort(key=lambda x:x[1])
print(ls)
