lst1 = input().split(',')
lst2 = input().split(',')
for i in range(len(lst2)):
    lst2[i] = eval(lst2[i])

d3 = dict([])
lst3 = []
for i in range(len(lst1)):
    d3[lst1[i]] = lst2[i]
for k,v in d3.items():
    lst3 += [[k,v]]
lst3.sort(key = lambda x:x[1])
print(lst3)


