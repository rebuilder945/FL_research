str=input()
Count={}
for s in str:
    for char in s:
        Count[char]=Count.get(char,0)+1
for i in sorted(Count.keys()):
    print("%s,%d"%(i,Count[i]))

