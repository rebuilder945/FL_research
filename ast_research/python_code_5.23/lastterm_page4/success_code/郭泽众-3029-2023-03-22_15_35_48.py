nList = input().split(",")
sList = eval(input())
tList = [[nList[x],sList[x]] for x in range(0,len(nList))]
print(tList)
