a=eval(input())
count={}
for i in a:
    for x in i:
        if x not in count:
            count[x]=1
        else:
            count[x]+=1
for i in sorted(count.keys()):
    print("%s,%d"%(i,count[i]))
