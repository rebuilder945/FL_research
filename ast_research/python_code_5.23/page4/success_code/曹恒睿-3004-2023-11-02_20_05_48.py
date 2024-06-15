shulie = eval(input())
sushulie = []
feisushu = []
for x in shulie:
    for i in range(2,x):
        if x%i==0: #x不为素数
            feisushu.append(x)
            break
        else:
            pass
for x in shulie:
    if x == 1:
        pass
    elif x == 0:
        pass
    elif x not in feisushu:
        sushulie.append(x)
    else:
        pass
print(sushulie)

