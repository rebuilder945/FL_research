item = input()
goods = {}
while(item !="p"):
    goods[item]=goods.get(item,0)+1
    if goods[item]>max:
        max=goods[item]
    item = input()
    
for a,b in list(goods.items()):
    if b == max:
        print(a,b)


