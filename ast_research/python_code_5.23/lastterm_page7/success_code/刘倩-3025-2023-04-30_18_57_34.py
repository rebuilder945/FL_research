s = input().split()
dic = {}
for x in s:
    if x in dic:
        dic[x]+=1
    else:
        dic[x]=1
zuida = max(dic.values())
zuida2 = [x for x,y in dic.items() if dic[y] == zuida]
for k in sorted(zuida2):
    print(k,zuida)
