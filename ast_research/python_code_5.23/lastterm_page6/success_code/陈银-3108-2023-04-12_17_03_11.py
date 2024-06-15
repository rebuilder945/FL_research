strlist = eval(input())
count = {}
for str in strlist:
    for i in str:
        count[i]=count.get(i,0)+1
for i in sorted(count.keys()):
    print("%s,%d"%(i,count[i]))
