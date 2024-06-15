def countletter(letter,undertest):
    time = 0
    for i in undertest:
        if i == letter:
            time = time + 1
    return time
tList = eval(input())
pList = []
for i in "abcdefghijklmnopqrstuvwxyz":
    for j in range(len(tList)):
        time = countletter(i,tList[j])
        pList.append("{},{}".format(i,time))
print("\n".join(pList))
