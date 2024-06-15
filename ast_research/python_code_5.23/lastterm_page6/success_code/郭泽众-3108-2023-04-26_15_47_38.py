def countletter(letter,undertest):
    time = 0
    for i in undertest:
        if i == letter:
            time = time + 1
    return time
tList = eval(input())
pList = []
for i in "abcdefghijklmnopqrstuvwxyz":
    if len(tList) == 1:
        time = countletter(i,tList[0])
        if time != 0:
            pList.append("{},{}".format(i,time))
    elif len(tList) == 2:
        time1 = countletter(i,tList[0])
        time2 = countletter(i,tList[1])
        atime = time1 + time2
        if atime != 0:
            pList.append("{},{}".format(i,atime))
    else:
        time11 = countletter(i,tList[0])
        time22 = countletter(i,tList[1])
        time33 = countletter(i,tList[2])
        aatime = time11 + time22 + time33
        if aatime != 0:
            pList.append("{},{}".format(i,aatime))
print("\n".join(pList))
