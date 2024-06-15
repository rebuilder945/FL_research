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
    money+=int(goods[i])

print(goodsNum,"%.2f"%(money))

