a = eval(input())
dic = {}
for x in a:
    for y in x:
        dic[y]=dic.get(y,0)+1
for k,v in dic.items():
    print("{},{}".format(k,v))

