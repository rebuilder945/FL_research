n,m = map(int,input().split(" "))
if (m-n)<3 or n<0 or m>9:
    print("illegal input")
elif n==0:
    lst4 = [x for x in range(n,m)]
    lst = []
    for x in lst4:
        lst.append(str(x))
    lst2 = []
    for x in lst[1:]:
        lst1 = lst.copy()
        lst1.remove(x)
        for y in lst1:
            lst3 = lst1.copy()
            lst3.remove(y)
            for z in lst3:
                lst2.append(x+y+z)
else:
    lst4 = [x for x in range(n,m)]
    lst = []
    for x in lst4:
        lst.append(str(x))
    lst2 = []
    for x in lst:
        lst1 = lst.copy()
        lst1.remove(x)
        for y in lst1:
            lst3 = lst1.copy()
            lst3.remove(y)
            for z in lst3:
                lst2.append(x+y+z)
print(" ".join(x for x in lst2))

