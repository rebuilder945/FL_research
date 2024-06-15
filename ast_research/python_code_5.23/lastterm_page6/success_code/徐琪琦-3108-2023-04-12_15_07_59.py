lst = eval(input())
lst1 = []
lst2 = []
for i in lst:
    for x in i:
            lst1.append(x)
            if not x in lst2:
                lst2.append(x)
lst2.sort()
for a in lst2:
    print("{},{}".format(a,lst1.count(a)))
