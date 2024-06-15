item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =float(item[1])
money=0
for i in goods:
    goods[item] += good

print(goodsNum,"%.2f"%(money))

