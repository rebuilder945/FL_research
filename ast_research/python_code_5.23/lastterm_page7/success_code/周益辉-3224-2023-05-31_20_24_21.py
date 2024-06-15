item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =len(list(goods.keys()))
money=0
for i in goods:
    money+=float(goods[i])

print(goodsNum,"%.2f"%(money))

