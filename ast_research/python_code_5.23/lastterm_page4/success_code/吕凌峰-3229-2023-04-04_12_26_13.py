lstA = eval(input())
lstB = [x for x in lstA if lstA.count(x) == 1]
lstB.sort()
if lstB:
    for i in range(len(lstB)-1):
        print("%d,"%lstB[i],end="")
    print(lstB[-1])
else:
    print("False")
