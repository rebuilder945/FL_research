lst = eval(input())
Count = {}
for str in lst:
    for char in str:
        if char not in Count:
            Count[char] = 1
        else:
            Count[char] += 1 
for x in sorted(Count.keys()):
    print("%c,%d"%(x,Count[x]))
    

