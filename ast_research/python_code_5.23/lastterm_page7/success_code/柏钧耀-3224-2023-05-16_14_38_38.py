item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =int(len(goods-1))
money=0
for i in goods:
    money+=int(goods[i].get())

print(goodsNum,"%.2f"%(money))

