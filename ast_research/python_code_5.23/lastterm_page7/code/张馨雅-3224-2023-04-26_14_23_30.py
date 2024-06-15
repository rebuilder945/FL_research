item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =[i for i in goods.values()]
money=0
for i in goods:
    money+=(goodsNum[i]

print(goodsNum,"%.2f"%(money))

