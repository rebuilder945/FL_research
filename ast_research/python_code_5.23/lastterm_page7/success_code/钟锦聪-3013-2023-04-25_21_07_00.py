item  =  input() 
numbers  =  {}
numbersList = []
while item  != "ok":
    num = item.split()
    numbersList.append(num)
    item  =  input()
numbersList.sort(key=lambda x:x[1])
a = []
for x in range(len(numbersList)):
    a.append(numbersList[x][0])
c = []
for x in range(len(numbersList)):
    c.append(int(numbersList[x][1]))
print(a)
print(c)
if "India" in a:
    print("yes")
else:
    print("no")
print(sum(c))
