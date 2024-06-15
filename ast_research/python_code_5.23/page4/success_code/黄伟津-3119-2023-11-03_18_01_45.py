lstA = eval(input())
lstB = []
for x in lstA[::-1]:
    if x not in lstB:
        lstB.append(x)
print(lstB[::-1])
