ls=input().split(",")
a,b=eval(input())
if a>=len(ls):
    print("error")
if a<len(ls):
    x=ls[a]
    kong=[x]*b
    zhuhe=ls+kong
    print(ls)
