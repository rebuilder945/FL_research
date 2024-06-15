item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =item
money=0
for i in goods:
    money=money+i

print(goodsNum,"%.2f"%(money))

