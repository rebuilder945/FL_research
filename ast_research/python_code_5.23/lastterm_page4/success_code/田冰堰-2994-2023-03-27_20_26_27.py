ls=eval(input())
n,m=eval(input())
a=len(ls)
if n>=a:
    print("error")
else:
    b=ls[n]
    ls1=[b]
    ls2=[ls1]*m
    print(ls+ls2)
