zimu = eval(input())
counts = {}
for i in zimu:
    counts[i] = counts.get(i,0)+1
list1 = sorted(counts.items(),key=lambda x:x[0])
for i in list1:
    print("%s,%d"%(list1[0],list1[1]))

