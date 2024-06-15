tList = eval(input())
pList = []
for i in tList:
    if tList.count(i) == 1:
        pList.append(str(i))
if pList is False:
    print("False")
else:
    pList.sort()
    num = ",".join(pList)
    print(num)
