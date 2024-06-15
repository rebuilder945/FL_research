ls=list(map(int,input().split(",")))
n,m=map(int,input().split(","))
if n>=len(ls) or n<-len(ls):
    print("error")
else:
    ls2=[ls[n]]*m
    ls3=ls+ls2
    print(ls3) 

