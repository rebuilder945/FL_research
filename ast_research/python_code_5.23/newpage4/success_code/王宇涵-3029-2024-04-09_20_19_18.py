lname = input()
lscore = list(map(int,input()))
ls = []
for i in range(len(lname)):
    ls.append([lname[i],lscore[i]])
# print(ls)
ls.sort(key=lambda x: x[1])
print(ls)
