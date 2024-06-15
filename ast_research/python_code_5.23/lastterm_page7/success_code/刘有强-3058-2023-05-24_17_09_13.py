item = input() or "q"
goods = {}
max=0
while(item !="p"):
    goods[item]=goods.get(item,0)+1
    if goods[item]>max:
        max=goods[item]
    item = input() or "q"

for a,b in list(goods.items()):
    if b == max:
        print(a,b)
