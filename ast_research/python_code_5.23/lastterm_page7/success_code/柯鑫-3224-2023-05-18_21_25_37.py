item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =len(good.keys())
money=0
for i in goods:
    money+=good[i]

print(goodsNum,"%.2f"%(money))

