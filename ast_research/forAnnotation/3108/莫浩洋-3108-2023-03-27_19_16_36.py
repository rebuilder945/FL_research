a = eval(input())
d = {}
for i in a:
    for x in i:
        d[x] = d.get(x,0)+1
b = list(d.items())
for i in b:
    print("{},{}".format(i[0],i[1]))
