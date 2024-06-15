item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =len(good)
money=0
for i in goods:
    print(goodsNum,"%.2f"%(money))

print(goodsNum,"%.2f"%(money))

