item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =len(goods)
money=0
for i in goods:
    a=goods[i]
    money+=a

print(goodsNum,"%.2f"%(money))

