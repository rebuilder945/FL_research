item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =count(goods[name])
money=0
for i in goods:
    money = money + cost

print(goodsNum,"%.2f"%(money))

