s=input()
dic={}
for a in s:
    for b in a:
        if 'a'<=b<='z':
            dic[b]=dic.get(b,0)+1
for i in dic.keys():
    print('%s,%d'%((i),(dic[i])))
