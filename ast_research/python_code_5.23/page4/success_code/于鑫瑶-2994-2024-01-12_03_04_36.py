a=map(int,input().split(","))
ls=list(a)
n,m=eval(input())
if n<=len(ls):
    ls1=[ls[n]]
    ls2=ls1*m
    l=ls+ls2
    print(l)
else:
    print("error")
