ls=eval(input())
ls1=eval(input())
n=ls1[0]
m=ls[1]
if n>=len(ls) or n<-len(ls):
    print('error')
else:
    a=ls[n]*m
    ls2=ls+a
    print(ls2)
