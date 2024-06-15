n = int(input())
lstA = [x for x in range(1,n+1)]
a = lstA[0]

for i in range(1,len(lstA)):
    lstA[i-1] = lstA[i]

lstA[i] = a
print(lstA)

