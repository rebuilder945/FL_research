z = eval(input())
numlist = []
for i in range(z):
    numlist.append(i+1)
numcopy = numlist[:]
numlist.remove(numlist[0])
numlist.append(numcopy[0])
print(numlist)
