numlist = eval(input())
numcopy = list(numlist[:])
intrep = eval(input())
if -len(numlist)<=intrep[0]<=len(numlist)-1:
    for i in range(intrep[1]):
        numcopy.append(numlist[intrep[0]])
    print(numcopy)
else:
    print("error")
