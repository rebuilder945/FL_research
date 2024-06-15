nStr = str(input())
nLen = len(nStr)
tList = []
for i in nStr:
    tList.append(str((int(i) + 5) % 10))
tList.reverse()
nCod = ''.join(tList)
print(nCod)
