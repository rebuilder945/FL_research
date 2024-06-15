item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =goods.get(nume)
money=0
for i in goods:
    money += goods[i]

print(goodsNum,"%.2f"%(money))

