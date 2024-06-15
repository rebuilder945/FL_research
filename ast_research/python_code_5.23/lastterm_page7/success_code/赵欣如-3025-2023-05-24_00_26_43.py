item=input().split()
dic={}
ls=[]
ls2=[]

for i in item:
    dic[i]=dic.get(i,0)+1
for x in dic.values():
    ls.append(x)
for a in dic:
    if dic[a]==max(ls):
        ls2.append(a)
ls2.sort()
for y in ls2:
    print(y,dic[y])
