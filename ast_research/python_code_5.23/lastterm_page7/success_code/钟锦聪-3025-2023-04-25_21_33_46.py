item  =  input() 
numbers  =  {}
num = item.split()
for x in num:
    numbers[x] = numbers.get(x,0) +1
numbersList = []
for k,v in numbers.items():
    numbersList.append([k,v])
numbersList.sort(key=lambda x :x[1],reverse=True)
sortList = []
sortList.append(numbersList[0])
for i in range(1,len(numbersList)):
    if numbersList[i][1]==numbersList[0][1]:
        sortList.append(numbersList[i])
sortList.sort(key=lambda x :x[0])
for x in range(len(sortList)):
    print(sortList[x],sep = " ")
