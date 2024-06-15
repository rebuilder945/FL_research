strlist = eval(input())
Count = {}
for str in strlist:
    for char in str:
        if char not in Count:
            Count[char] = 1
        else:
            Count[char] = Count[char]+1
for i in sorted(Count.key()):
    print("%s,%d"%(i,Count[i]))
