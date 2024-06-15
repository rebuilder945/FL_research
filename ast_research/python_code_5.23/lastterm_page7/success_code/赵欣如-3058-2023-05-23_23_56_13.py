item=input() or"q"
dic={}
ls=[]
while (item !="q"):
    dic[item]=dic.get(item,0)+1
    item=input() or"q"
for x in dic.values():
    ls.append(x)
for i in dic.keys():
    if dic[i]==max(ls):
        print(i,dic[i])
