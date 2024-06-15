names = input().split(",") #split 设定分隔符
nameslist = list(names)
scoreslist = eval(input())
namescoreslist = []
for i in range(len(nameslist)):
    ls = (nameslist[i],scoreslist[i])
    namescoreslist.append(list(ls))
print(namescoreslist)




