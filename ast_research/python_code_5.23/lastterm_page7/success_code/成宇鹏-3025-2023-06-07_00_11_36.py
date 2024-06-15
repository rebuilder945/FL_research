a = input().split()
dic = {}
for x in a:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
b = list(dic.keys())
k = list(dic.values())
c = []
for i in b:
    c.append([i,dic[i]])
c.sort(key = lambda x: x[0])
c.sort(key = lambda x: x[1])
j = k.count(max(k))
for n in range(len(b)-j,len(b)):
    print("%s %d"%(c[n][0],c[n][1]))


