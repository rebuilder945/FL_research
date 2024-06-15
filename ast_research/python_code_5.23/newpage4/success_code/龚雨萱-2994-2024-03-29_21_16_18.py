ls=list(eval(input()))
n,m=eval(input())
a=len(ls)
if n>=a or n<-1*a:
    print("error")
else:
    b=[ls[n]]*m
    ls=ls+b
    print(ls)
