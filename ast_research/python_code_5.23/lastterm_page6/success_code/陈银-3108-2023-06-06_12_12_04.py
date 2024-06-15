a = eval(input())
dic = {}
for x in a:
    for y in x:
        dic[y]=dic.get(y,0)+1
for i in sorted(dic.keys()):
    print("{},{}".format(i,dic[i]))


