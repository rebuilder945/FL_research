liebiao = eval(input())
xinliebiao = []
for x in liebiao:
    if liebiao.count(x)==1:
        xinliebiao.append(x)
    else:
        pass
xinliebiao.sort()
if xinliebiao == []:
    print("False")
else:
    xin = str(xinliebiao)
    xin1 = xin.strip("[]")
    print(xin1)
    
