name = input()
score = input()
name = name.split(',')
score = score.split(',')
res = []
for i in range(len(name)):
    temp = []
    temp.append(name[i])
    temp.append(int(score[i]))
    res.append(temp)
res.sort(key = lambda res: res[1])
print(res)

