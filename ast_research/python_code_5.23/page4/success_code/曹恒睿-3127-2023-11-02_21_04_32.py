n = eval(input())
list = [x for x in range(1,n+1)]
xinliebiao = []
for x in list:
    if list.index(x)==0:
        pass
    else:
        xinliebiao.append(x)
a1 = list[0]
xinliebiao.append(a1)
print(xinliebiao)
