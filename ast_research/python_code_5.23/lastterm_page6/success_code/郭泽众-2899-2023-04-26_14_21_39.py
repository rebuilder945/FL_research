bList = str(input()).split(" ")
n = int(bList[0])
m = int(bList[1])
pList = []
if n < m:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i != j and j != k and i != k:
                    pList.append(str(i)+str(j)+str(k))
else:
    print("illegal input")
print(" ".join(pList))
