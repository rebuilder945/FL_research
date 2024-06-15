liebiao = eval(input())
cishu = liebiao.count(0)
for i in (0,cishu):
    liebiao.remove(0)
for i in (0,cishu):
    liebiao.append(0)
print(liebiao)
