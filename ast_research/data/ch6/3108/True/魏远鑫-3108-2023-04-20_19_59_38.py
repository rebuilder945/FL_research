ls=eval(input())
count={}
for i in ls:
    for str in i:
        count[str]=count.get(str,0)+1
for i in sorted(count.keys()):
    print("%s,%d"%(i,count[i]))
