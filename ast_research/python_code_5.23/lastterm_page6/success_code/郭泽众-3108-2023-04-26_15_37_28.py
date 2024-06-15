def countletter(letter,undertest):
    time = 0
    for i in undertest:
        if i == letter:
            time = time + 1
    return time
tList = eval(input())
pList = []
for i in "abcdefghijklmnopqrstuvwxyz":
    time1 = countletter(i,tList[0])
    time2 = countletter(i,tList[1])
    atime = time1 + time2
    if atime != 0:
        pList.append("{},{}".format(i,atime))
print("\n".join(pList))
