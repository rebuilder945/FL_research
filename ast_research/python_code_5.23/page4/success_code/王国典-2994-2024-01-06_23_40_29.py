ls=input().split(",")
a,b=eval(input())
if a>=len(ls):
    print("error")
if a<len(ls):
    x=ls[a]
    kong=[x]*b
    zhongjian=ls+kong
    zhuhe=[int(x) for x in zhongjian]
    print(zhuhe)
