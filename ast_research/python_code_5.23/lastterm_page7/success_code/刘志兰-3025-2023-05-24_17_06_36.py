lst = list(input().split(""))
dic = {}
for i in lst:
    if i in dic:
       dic[i]+=1
    else:
        dic[i]=1
items=[]
for x,y in dic.items():
    items.append([x,y])
items.sort(key=lambda x: x[1], reverse=True)
items.sort(key=lambda x: x[0])
for i in items:
    if i[1]==items[0][1]:
        print('%s %i'%(i[0],i[1]))
