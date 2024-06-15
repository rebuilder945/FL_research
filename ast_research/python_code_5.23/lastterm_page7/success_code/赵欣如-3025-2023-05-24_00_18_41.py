item=input().split()
dic={}
ls=[]
for i in item:
    dic[i]=dic.get(i,0)+1
for x in dic.values():
    ls.append(x)
ls.sort()
for a in dic:
    if dic[a]==max(ls):
        print(a,dic[a])
