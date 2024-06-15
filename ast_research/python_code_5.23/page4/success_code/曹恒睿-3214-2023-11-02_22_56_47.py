liebiao = eval(input())
cishu = liebiao.count(0)
if cishu == 0:
    pass
else:
    for i in (0,cishu):
        liebiao.remove(0)
    for i in (0,cishu):
        liebiao.append(0)

if liebiao[0]==0:  #发现这个remove有漏洞，0要是在第一个它不会删，会跳过
    del liebiao[0]
    liebiao.append(0)
else:
    pass
print(liebiao)
