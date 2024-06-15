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
        print(*xinliebiao, sep=',')
    
