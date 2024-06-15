a = eval(input())
d = {}
for i in a:
    for x in i:
        d[x] = d.get(x,0)+1
b = list(d.items())
b. sort(key = lambda x:(x[0]),reverse=False)
for i in b:
    print("{},{}".format(i[0],i[1]))
