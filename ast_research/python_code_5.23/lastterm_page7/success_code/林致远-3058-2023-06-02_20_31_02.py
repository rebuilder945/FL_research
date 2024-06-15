dic = {}
w = ''
while w != 'q':
    w = input()
    if w not in dic.keys():
        dic[w] = 1
    else:
        dic[w] += 1
d1 = list(dic.keys())
d2 = list(dic.values())
ind = d2.index(max(d2))
print(d1[ind],d2[ind])
