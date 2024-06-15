item=input()or"q"
goods={}
while(item!="q"):
    goods[item]=goods.get(item,0)+1
    item=input()or"q"
list=[]
for k,v in goods.items():
    list.append([k,v])
list.sort(key=lambda x:x[1],reverse=True)
print('%s %s'%(list[1[0]],list[1[1]]))
