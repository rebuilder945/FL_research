numlist = eval(input())
numlistcopy = numlist[:]
for x in range(len(numlist)):
    if numlistcopy[x]==0:
        numlist.remove(0)
        numlist.append(0)
print(numlist)
