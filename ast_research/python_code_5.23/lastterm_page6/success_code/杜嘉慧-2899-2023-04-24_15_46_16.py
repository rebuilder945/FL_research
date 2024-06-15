n = int()
m = int()
sums = []
sums1 = []
if (m - n) <2:
    print("illegal input")
else:
    for x in range(n, m):
        sums.append(x)
    for x in range(len(sums)):
        for y in range(len(sums)):
            for z in range(len(sums)):
                if x != y and y != z and x != z and sums[x] != 0:
                    s1 = str(sums[x]) + str(sums[y]) + str(sums[z])
                    if s1 not in sums1:
                        sums1.append(s1)
                    else:
                        pass
                else:
                    pass
    for y in sums1:
        y = int(y)
        print("%d"%y,end="")


