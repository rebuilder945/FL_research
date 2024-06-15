strlist=eval(input())
Count={}
for str in strlist:
    for char in str:
        Count[char]=Count.get(char,0)+1
for i in sorted(count.keys()):
    print("%s,%d"%(i,Count(i)))
