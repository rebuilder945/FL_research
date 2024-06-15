item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =len(goods)+1
money=0
for i in goods:
    

print(goodsNum,"%.2f"%(money))

