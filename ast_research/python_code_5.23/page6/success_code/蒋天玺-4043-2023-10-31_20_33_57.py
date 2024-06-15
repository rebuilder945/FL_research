name = []
value = [0,0,0,0,0,0,0,0,0,0]
n = eval(input())
for i in n:
    a = sorted(i)
    for j in a:
        if j not in name:
            name.append(j)
            value[name.index(j)]+=1
        if j in name:
            value[name.index(j)]+=1
for i in range(len(name)):
    print("%s,%d"%(name[i],value[i]))


