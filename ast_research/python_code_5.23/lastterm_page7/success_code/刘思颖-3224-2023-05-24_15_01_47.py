item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =goods.count(name)
money=0
for i in goods:
      money+=coat

print(goodsNum,"%.2f"%(money))

