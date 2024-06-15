numlist = eval(input())
numcopy = numlist[:]
only = []
for x in range(len(numcopy)):
    if numlist.count(numcopy[x])==1:
        only.append(numcopy[x])
    else:
        pass
only.sort()
if len(only)>=0:
    only2 = str(only)
    print(only2[1:-1])
else:
    print("False")
