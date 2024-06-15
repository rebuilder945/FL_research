item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =sum(goods)
money=0
for i in goods:
    money = money + goods[i]

print(goodsNum,"%.2f"%(money))

