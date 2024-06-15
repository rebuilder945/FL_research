item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =dic["goods"]
money=0
for i in goods:
    money += goodsNum*cost

print(goodsNum,"%.2f"%(money))

