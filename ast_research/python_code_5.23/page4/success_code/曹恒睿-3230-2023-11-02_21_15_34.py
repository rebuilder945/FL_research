liebiao = eval(input())
z = ""
cishu = len(liebiao)
for i in range (0,cishu):
    zuida = max(liebiao)
    liebiao.remove(zuida)
    jia=str(zuida)
    z=z+jia
    m=int(z)
print(m)
