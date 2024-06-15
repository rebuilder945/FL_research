item = input() or "p"
goods = {}
max=0
while(item !="p"):
    goods[item]=goods.get(item,0)+1
    if goods[item]>max:
        max=goods[item]
    item = input() or "p"

for a,b in list(goods.items()):
    if b == max:
        print(a,b)
