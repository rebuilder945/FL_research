numlist = list(eval(input()))
numcopy = numlist[:]
for i in range(len(numcopy)):
    if numlist.count(numcopy[i]) >=2:
        numlist.remove(numcopy[i])
    else:
        pass
print(numlist)
