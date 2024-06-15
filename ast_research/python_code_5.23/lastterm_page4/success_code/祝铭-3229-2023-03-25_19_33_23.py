numlist = list(eval(input()))
numcopy = numlist[:]
only = []
for x in range(len(numcopy)):
    if numlist.count(numcopy[x])==1:
        only.append(numcopy[x])
    else:
        pass
if len(only)>=1:
    print(only.sort())
else:
    print("False")
