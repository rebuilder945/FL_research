lst=eval(input())
Count={}
for str in lst:
    for char in str:
        if char not in Count:
            Count[char]=1
        else:
            Count[char]=Count[char]+1
for i in sorted(Count.keys()):
    print("%s,%d"%(i,Count[i]))

