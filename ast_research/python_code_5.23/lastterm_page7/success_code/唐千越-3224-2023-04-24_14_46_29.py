item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =sum(eval(goods[name]))
money=0
for i in goods:
    money += goods[i]

print(goodsNum,"%.2f"%(money))

