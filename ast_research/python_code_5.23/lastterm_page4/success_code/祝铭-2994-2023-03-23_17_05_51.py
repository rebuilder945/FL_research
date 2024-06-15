numlist = eval(input())
numcopy = numlist[:]
intrep = eval(input())
if -len(numcopy)<=intrep[0]<=len(numcopy)-1:
    for i in range(intrep[1]):
        numlist.append(numcopy[intrep[0]])
    print(numlist)
else:
    print("error")
