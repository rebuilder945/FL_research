item  =  input() 
numbers  =  {}
numbersList = []
while item  != "ok":
    num = item.split()
    numbers[num[0]]=num[1]
    item  =  input()
for k,v in numbers.items():
    numbersList.append([k,v])
numbersList.sort(key=lambda x:x[1])
print(numbersList)
print(list(numbers.keys()))
a = []
for x in range(len(numbersList)):
    a.append(numbersList[x][0])
c = []
for x in range(len(numbersList)):
    c.append(int((numbersList[x][1])))
print(a)
print(c)
if "India" in a:
    print("yes")
else:
    print("no")
print(sum(c))
