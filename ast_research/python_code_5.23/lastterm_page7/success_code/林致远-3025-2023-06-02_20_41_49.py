dic = {}
w = input().split()
for x in w:
    if w not in dic.keys():
        dic[w] = 1
    else:
        dic[w] += 1
d1 = list(dic.keys())
d2 = list(dic.values())
for x in range(d2.count(max(d2))):
    ind = d2.index(max(d2))
    print(d1[ind],d2[ind])
    del d1[ind]
    del d2[ind]
