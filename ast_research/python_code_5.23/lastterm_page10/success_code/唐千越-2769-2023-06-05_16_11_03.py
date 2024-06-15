def fanyi(dianwen):
    lst1 = "".join([chr(ord('a')+x) for x in range(0,26)])
    l = len(dianwen)
    for i in range(0,l):
        if dianwen[i] in lst1:
            dianwen[i] = lst1[26-i]
    lst2 = lst1.upper()
    for i in range(0,l):
        if dianwen[i] in lst2:
            dianwen[i] = lst1[26-i]
    return dianwen
dianwen = eval(input())
print(fanyi(dianwen))
