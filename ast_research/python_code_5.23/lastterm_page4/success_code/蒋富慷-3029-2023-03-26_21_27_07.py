lstNames = input().split(",")
lstScores = eval(input())
lstR =[]
for i in range(len(lstNames)):
    lstR.append([lstNames[i],lstScores[i]])
print(lstR)
