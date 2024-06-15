lstA = eval(input())
lstB = []
n = 0
for i in range(len(lstA)):
    if(lstA[i] == 0):
        n += 1
    else:
        lstB.append(lstA[i])
for i in range(n):
    lstB.append(0)
print(lstB)
