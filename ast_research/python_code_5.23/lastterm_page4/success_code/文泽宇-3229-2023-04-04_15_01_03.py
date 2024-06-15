lst = eval(input())
lst1 = [lst.count(x) for x in lst]
lst2 = []
if 1 in lst1:
    for i in lst:
        if lst.count(i) == 1:
            lst2.append(i)
    lst2.sort()
    result = ",".join(map(str,lst2))
    print(result)
else:
    print(False)

