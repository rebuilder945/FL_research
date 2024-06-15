sName=input().split(',')
lscore=eval(input())
ls=[]
for i in range(len(sName)):
    ls.append([sName[i],lscore[i]])
ls.sort(key=lambda x: x[1])
print(ls)
