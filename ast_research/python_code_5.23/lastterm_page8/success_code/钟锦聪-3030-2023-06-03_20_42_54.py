names = input().split(",")
score = input().split(",")
# iNames = {}
# iNamesList = []
# for i in range(len(iList1)):
#     iNames[iList1[i]] = int(iList2[i])
# for k,v in iNames.items():
#     iNamesList.append([k,v])
iNamesList = list(zip(names,score))
iNamesList.sort(key=lambda x :x[1])
print(iNamesList)
