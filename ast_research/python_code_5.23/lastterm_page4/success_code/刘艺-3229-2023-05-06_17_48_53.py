list = eval(input())
list2 = []
for x in list:
    if list.count(x) == 1:
        list2.append(x)
    else:
        pass
list2.sort()
if len(list2) != 0:
    ista = ','.join(str(i) for i in list2)
    print(ista)
elif len(list2) == 0:
    print("False")

    
