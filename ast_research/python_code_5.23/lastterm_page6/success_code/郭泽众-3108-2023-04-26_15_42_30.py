def countletter(letter,undertest):
    time = 0
    for i in undertest:
        if i == letter:
            time = time + 1
    return time
tList = eval(input())
pList = []
timeList = []
for i in "abcdefghijklmnopqrstuvwxyz":
    for j in range(len(tList)):
        time = countletter(i,tList[j])
        timeList.append(time)
        atime = sum(timeList)
        if atime != 0:
            pList.append("{},{}".format(i,atime))
print("\n".join(pList))
