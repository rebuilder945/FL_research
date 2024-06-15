numlist = eval(input())
numlist.sort(key=chr)
maxint = 0
for x in range(len(numlist)):
    maxint+=(numlist[x]*pow(10,x))
print(maxint)
