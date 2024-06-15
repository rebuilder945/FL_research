dic = {}
w = input().split()
for x in w:
    if x not in dic.keys():
        dic[x] = 1
    else:
        dic[x] += 1
d1 = list(dic.keys())
d2 = list(dic.values())
m = max(d2)
a = []
for x in w:
    if x not in a and dic[x] == m:
        print(x,a)
        a.append(x)
