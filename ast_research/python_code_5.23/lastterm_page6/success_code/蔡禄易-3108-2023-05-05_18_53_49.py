zimu = eval(input())
counts = {}
for i in zimu:
    counts[i] = counts.get(i,0)+1
list1 = []
for k,v in counts.items():
    list1.append([k,v])
for i in list1:
    print(str(list1[i]))

