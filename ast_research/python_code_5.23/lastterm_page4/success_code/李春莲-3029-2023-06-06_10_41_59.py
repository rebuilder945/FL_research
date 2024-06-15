sName=input().split(',')
iScore=eval(input())
ls=[]
for i in range(len(sName)):
    ls.append([sName[i],iScore[i]])
print(ls)
