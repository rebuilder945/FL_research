lname = input().split(',')
lscore=eval(input())
ls=[]
for i inrange(len(lname)):
ls.append([lname[i],lscore[i]])
ls.sort(key=lambda x: x[1])
print(ls)
