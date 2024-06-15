ls=list(eval(input()))
n,m=eval(input())
ls2=[]
if n>len(ls) or n<-len(ls):
    print("error")
else:
    a=ls[n]
    ls2.append(a)
    ls3=ls2*m
    print(ls+ls3)
