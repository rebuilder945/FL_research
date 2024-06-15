names = input().split(",")
score = input().split(",")
iNames = {}
iNamesList = []
for i in range(len(names)):
    iNames[names[i]] = int(score[i])
for k,v in iNames.items():
    iNamesList.append([k,v])
iNamesList.sort(key=lambda x :x[1])
print(iNamesList)


