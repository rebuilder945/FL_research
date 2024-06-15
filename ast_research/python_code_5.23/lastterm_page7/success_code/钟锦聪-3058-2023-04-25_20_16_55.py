item  =  input() 
numbers  =  {}
while item  != "q":
    numbers[item] = numbers.get(item,0) +1
    item  =  input() 
numbersList = []
for k,v in numbers.items():
    numbersList.append([k,v])
numbersList.sort(key=lambda x :x[1],reverse=True)
print(*numbersList[0],sep = " ") 
