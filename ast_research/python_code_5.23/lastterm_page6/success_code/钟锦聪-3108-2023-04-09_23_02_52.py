strlist = eval(input())
count={}
for str in strlist:
    for char in str:
        count[char] = count.get(char,0)+1
for i in sorted(count.keys()):
    print("%s,%d"%(i,count[i]))

