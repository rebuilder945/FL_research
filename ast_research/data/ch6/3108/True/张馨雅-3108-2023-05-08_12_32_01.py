s=eval(input())
dic={}
for a in s:
    for b in a:
        if 'a'<=b<='z':
            dic[b]=dic.get(b,0)+1
dic=sorted(dic.items(), key=lambda x:x[0])
for i in dic:
    print('%s,%d'%((i[0]),(i[1])))
# for i in dic.keys():
#     print('%s,%d'%((i),(dic[i])))
