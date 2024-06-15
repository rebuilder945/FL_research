item = input() or "ok"
goods = {}
while(item !="ok"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "ok"

kd = list(goods.keys())
print(sorted(kd, reverse=False))
ke = list(goods.values())
print(sorted(ke, reverse=False))
if "India" in goods:
    print("yes")
else:
    print("no")
i=0
sums=0
while i < len(ke):
    sums += ke[i]
    i += 1
print(sums)


