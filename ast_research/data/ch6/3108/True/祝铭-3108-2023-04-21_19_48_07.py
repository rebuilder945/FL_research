p = eval(input())
slist = []
num = []
for i in p:
    for j in range(len(i)):
        if i[j] not in slist :
            slist.append(i[j])
for x in range(len(slist)):
    num.append(0)
slist.sort(key=str.lower)
for s in p:
    for t in range(len(s)):
        for u in range(len(slist)):
            if s[t] == slist[u]:
                num[u] += 1
for v in range(len(num)):
    print('%s,%s'%(slist[v],num[v]))
