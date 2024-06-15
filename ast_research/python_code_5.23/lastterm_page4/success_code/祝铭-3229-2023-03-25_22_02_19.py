numlist = eval(input())
numcopy = numlist[:]
only = []
for x in range(len(numcopy)):
    if numlist.count(numcopy[x]) == 1:
        only.append(numcopy[x])
    else:
        pass
only.sort()
if len(only) >= 2:
    print("%d,%d"%((only[0]),only[1]))
elif len(only) == 1:
    print('%d'%(only[0]))
else:
    print("False")
