item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =goods.keys()count
money=0
for i in goods:
    money+=sum(goods.values())

print(goodsNum,"%.2f"%(money))

