lstA = eval(input())
lstB = [lstA.count(x) for x in lstA]
lstC = []

for i in range(0,len(lstB)):
    if lstB[i] == 1:
        lstC.append(lstA[i])
        lstC.sort()

if len(lstC) != 0:
    for i in range(len(lstC)-1):
        print(lstC[i],end=',')
    print(lstC[len(lstC)-1])

else:
    print(False)

