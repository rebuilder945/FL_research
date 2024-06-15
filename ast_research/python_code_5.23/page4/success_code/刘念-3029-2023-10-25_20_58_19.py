lname = input().split(',')
lscore= eval(input())
ls=[]
for i in range(len(lname)):
    ls.append([lname[i],lscore[i]])
print(ls)
