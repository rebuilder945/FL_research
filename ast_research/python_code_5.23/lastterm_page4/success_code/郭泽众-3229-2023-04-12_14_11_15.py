tList = eval(input())
pList = []
for i in tList:
    if tList.count(i) == 1:
        pList.append(str(i))
if len(pList) == 0:
    print("False")
else:
    pList.sort()
    num = ",".join(pList)
    print(num)
