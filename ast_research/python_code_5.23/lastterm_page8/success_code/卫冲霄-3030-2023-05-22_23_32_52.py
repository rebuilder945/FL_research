sName=input().split(",")
score=input().split(",")
ls=[[sName[i],score[i]] for i in range(len(sName))]
ls.sort(key=lambda x:x[1], reverse=False)
print(ls)
