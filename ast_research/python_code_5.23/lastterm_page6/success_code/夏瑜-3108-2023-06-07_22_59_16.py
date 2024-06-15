a=eval(input())
Count={}
for str in a:
    for char in str:
        Count[char]=Count.get(char,0)+1
for i in sorted(Count.keys()):
    print("%s,%d"% (i,Count[i]))
    
    


