item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =len(goods[name])
money=0
for i in goods:
    money = money + cost

print(goodsNum,"%.2f"%(money))

