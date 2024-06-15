item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =goodsNum=len(goods.keys())
money=0
for i in goods:
        money=sum(goods.values())

print(goodsNum,"%.2f"%(money))

