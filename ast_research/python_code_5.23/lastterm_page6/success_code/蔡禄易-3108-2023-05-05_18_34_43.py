zimu = eval(input())
counts = {}
for i in zimu:
    counts[i] = counts.get(x,0)+1
list1 = list(counts.items())
for i in list1:
    print("{},{}".format(list1[i][0],list1[i][1]))
