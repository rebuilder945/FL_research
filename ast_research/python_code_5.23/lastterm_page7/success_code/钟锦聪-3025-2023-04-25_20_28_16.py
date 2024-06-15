item  =  input() 
numbers  =  {}
num = item.split()
for x in num:
    numbers[x] = numbers.get(x,0) +1
numbersList = []
for k,v in numbers.items():
    numbersList.append([k,v])
numbersList.sort(key=lambda x :x[1],reverse=True)
print(*numbersList[0],sep = " ")
for i in range(1,len(numbersList)):
    if numbersList[i][1]==numbersList[0][1]:
        print(*numbersList[i],sep = " ") 
