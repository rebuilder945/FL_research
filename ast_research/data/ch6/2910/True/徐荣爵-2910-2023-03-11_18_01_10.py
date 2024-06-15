h = float(input())
N = int(input())
N2 = N - 1
allhigh = 0
if N <= 1:
    allhigh = h
else:
    allhigh = allhigh + h
    for x in range(N2) :
        h = h / 2
        allhigh = allhigh + 2 * h
print("%.2f"%allhigh)
