lname=input().split(",")
lscore=list(map(int,input().split(',')))
ls=[]
for i in range(len(lname)):
    ls.append([lname[i],lscore[i]])
ls.sort(key=lambda x: x[1])
print(ls)
