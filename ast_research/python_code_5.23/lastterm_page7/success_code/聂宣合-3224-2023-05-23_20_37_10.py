item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =0
money=0
for i in goods:
    goodsNum+=goods[i]

print(goodsNum,"%.2f"%(money))

