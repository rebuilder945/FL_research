zimu = eval(input())
counts = {}
for i in zimu:
    counts[i] = counts.get(i,0)+1
list1 = list(counts.items())
for i in range(len(list1)):
    print(list1[i][0],list1[i][1])
