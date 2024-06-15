str = str(input()).split(" ")
d1 = {}
for x in str:
    d1[x] = str.count(x)
m = max(d1.values())
l = []
for i in d1.keys():
    if d1[i] == m:
        l.append(i)
l.sort()
for x in l:
    print("{} {}".format(x,m))
