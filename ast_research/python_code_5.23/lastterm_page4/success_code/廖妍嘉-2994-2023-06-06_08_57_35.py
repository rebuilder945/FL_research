ls=eval(input())
n,m=input().split()
if n>=len(ls) or n<-len(ls):
    print("error")
else:
    ls2=ls[n]*m
    del ls[n]
    ls3=ls+ls2
    print(ls3) 

