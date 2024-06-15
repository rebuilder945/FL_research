lst = eval(input())
lst1 = [lst.count(x) for x in lst]
lst2 = []
if 1 in lst1:
    for i in lst:
        if lst.count(i) == 1:
            lst2.append(i)
        else:
            None
    print(lst2.sort())
else:
    print(False)

