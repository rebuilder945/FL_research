item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =sum(list(goods.values()))
money=0
for i in goods:
    len(list(goods.keys()))

print(goodsNum,"%.2f"%(money))

