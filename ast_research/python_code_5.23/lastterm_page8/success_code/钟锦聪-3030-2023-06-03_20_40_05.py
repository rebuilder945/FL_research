names = input()
score = input()
iNames = {}
iNamesList = []
iList1 = names.split(",")
iList2 = score.split(",")
for i in range(len(iList1)):
    iNames[iList1[i]] = int(iList2[i])
for k,v in iNames.items():
    iNamesList.append([k,v])
iNamesList.sort(key=lambda x :x[1])
print(iNamesList)
