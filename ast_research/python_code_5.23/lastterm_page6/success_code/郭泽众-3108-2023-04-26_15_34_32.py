def countletter(letter,undertest):
    time = 0
    for i in undertest:
        if i == letter:
            time = time + 1
    return time
tList = eval(input())
pList = []
for i in "abcdefghijklmnopqrstuvwxyz":
    for lst in tList:
        ltime = countletter(i,lst)
        if ltime != 0:
            pList.append("{},{}".format(i,ltime))
print("\n".join(pList))
