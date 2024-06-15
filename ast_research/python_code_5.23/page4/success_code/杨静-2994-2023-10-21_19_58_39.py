ls=list(eval(input()))
s=len(ls)
ls1=[]
n,m=eval(input())
if n>=s or n<-s:
    print('error')
else:
    if n>0:
        ls1.append(ls[n-1])
        ls2=ls+ls1*m
        print(ls2)
    else:
        ls1.append(ls[n])
        ls2=ls+ls1*m
        print(ls2)
