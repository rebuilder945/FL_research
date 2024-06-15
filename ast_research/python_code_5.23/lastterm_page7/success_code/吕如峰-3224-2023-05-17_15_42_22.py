item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =len(name)
money=0
for i in goods:
    money+=cost[i]

print(goodsNum,"%.2f"%(money))

