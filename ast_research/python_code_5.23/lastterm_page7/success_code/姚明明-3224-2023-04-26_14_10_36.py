item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =len(item)-2
money=0
for i in goods:
    money+=goods.get(i,1)

print(goodsNum,"%.2f"%(money))

